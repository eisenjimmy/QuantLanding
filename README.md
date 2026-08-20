# Quantactic Landing

Static marketing + legal site for Quantactic and App Store Connect.

Product: **Quantactic — market intelligence that shows its work.**

Locales:
- English
- Korean
- Japanese
- Simplified Chinese
- Spanish

U.S. subscription reference:
- Quantactic Pro Monthly — **$4.99/month**
- Quantactic Pro Annual — **$39.99/year** (about 33% savings)

The content dictionaries in `scripts/build_site.py` are the source of truth. The generated site includes canonical and hreflang metadata, Open Graph and Twitter cards, `SoftwareApplication` and `FAQPage` JSON-LD, a sitemap, robots rules, a web manifest, and an experimental `llms.txt` discovery summary.

## Build

```bash
python3 scripts/build_site.py
```

## Verify

```bash
python3 scripts/verify_site.py
```

The root English aliases `/`, `/privacy.html`, and `/terms.html` remain stable for App Store Connect and GitHub Pages. The `/en/` pages canonicalize to those root URLs; the other four locale folders use self-canonical URLs.
