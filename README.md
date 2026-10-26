# RLKG Law Website

Static site for Rountree Leitman Klein & Geer, LLC (https://www.rlkglaw.com), deployed by Netlify from the `main` branch of this repository. There is no build step: the HTML files in the repo are served as-is.

## Layout

- Root `*.html` pages: homepage, practice areas, attorney profiles, team, reviews, contact
- `blog/*.html`: one file per post; `blog.html` is the index
- `images/`: site images; attorney headshots are `images/{first}-{last}-profile.png` at 600x600
- `_redirects`: legacy Weebly slugs, canonicalization, and extensionless-to-.html rules
- `netlify.toml`: HTTPS/www redirects and cache/security headers
- `sitemap.xml`, `rss.xml`, `robots.txt`

## Publishing a blog post

1. Add `blog/<slug>.html` (copy a recent post as the template; blog pages link to root pages with a `../` prefix).
2. Add the card and the `BlogPosting` entry in `blog.html`.
3. Add the URL to `sitemap.xml` and the item to `rss.xml` (bump `lastBuildDate`; the RSS feed drives the social auto-poster).
4. Commit and push to `main`; Netlify deploys automatically.

## Roster changes

Update, in this order: the nav dropdown on every page, `our-team.html` (grid class so no row has an orphan card), the paralegal sidebar box on affected attorney pages, the attorney-count stat on `index.html`, and any directory listings.
