// Read-only tag and funnel scan. Paste into the page console or run with a browser tool's
// JavaScript executor. Changes nothing, sends nothing. Returns one JSON object to save as evidence.
(() => {
  const html = document.documentElement.outerHTML;
  const uniq = (re) => [...new Set((html.match(re) || []))];
  const scripts = [...document.scripts].map((s) => s.src).filter(Boolean);
  const host = (u) => { try { return new URL(u, location.href).hostname; } catch (e) { return null; } };
  return {
    url: location.href.split('#')[0],
    checked_at: new Date().toISOString(),
    consent_hint: /cookie|consent/i.test(document.body.innerText.slice(0, 5000))
      ? 'banner text present: record which choice was made before this scan'
      : 'no consent text detected near top',
    meta_pixel: { fbq_loaded: typeof window.fbq === 'function', ids: uniq(/fbq\(\s*['"]init['"]\s*,\s*['"](\d{8,20})/g) },
    gtm: uniq(/GTM-[A-Z0-9]{4,9}/g),
    gtm_runtime: Object.keys(window.google_tag_manager || {}).filter((k) => /^(GTM|G|AW)-/.test(k)),
    ga4: uniq(/\bG-[A-Z0-9]{6,12}\b/g),
    google_ads: uniq(/\bAW-\d{6,12}\b/g),
    tiktok: { ttq_loaded: typeof window.ttq === 'object', script: scripts.some((s) => /analytics\.tiktok\.com/.test(s)) },
    linkedin_insight: scripts.some((s) => /snap\.licdn\.com/.test(s)),
    first_party_gtm: scripts.filter((s) => /gtm\.js/.test(s) && !/googletagmanager\.com/.test(s)).map(host),
    third_party_hosts: [...new Set(scripts.map(host).filter((h) => h && h !== location.hostname))].sort(),
    iframe_hosts: [...new Set([...document.querySelectorAll('iframe')].map((f) => host(f.src)).filter(Boolean))],
    forms: [...document.forms].map((f) => ({ action_host: host(f.action), fields: [...f.elements].map((e) => e.name || e.type).filter(Boolean).slice(0, 25) })),
    url_param_keys: [...new URLSearchParams(location.search).keys()],
    utm: Object.fromEntries([...new URLSearchParams(location.search)].filter(([k]) => k.startsWith('utm_'))),
    note: 'Absence here is bounded to this page, this load and this consent state. Server-side events are invisible.'
  };
})();
