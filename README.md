# Quantfox Landing

Static marketing + legal site for App Store Connect.

## URLs (GitHub Pages style)

| Language | Product | Privacy | Terms |
|---|---|---|---|
| English (default ASC) | `/` or `/en/` | `/privacy.html` or `/en/privacy.html` | `/terms.html` or `/en/terms.html` |
| Spanish | `/es/` | `/es/privacy.html` | `/es/terms.html` |
| Japanese | `/ja/` | `/ja/privacy.html` | `/ja/terms.html` |
| Korean | `/ko/` | `/ko/privacy.html` | `/ko/terms.html` |
| Simplified Chinese | `/zh-Hans/` | `/zh-Hans/privacy.html` | `/zh-Hans/terms.html` |

## Pricing (U.S. reference)

- Quantfox Pro Monthly: **$4.99**
- Quantfox Pro Annually: **$39.99**

## Rebuild after content edits

```bash
python3 scripts/build_site.py
```

Edit `scripts/build_site.py` `CONTENT` dict, then regenerate.
