import glob
import re

pages = {
    "practice-areas.html": "https://www.rlkglaw.com/practice-areas.html",
    "our-team.html": "https://www.rlkglaw.com/our-team.html",
    "reviews-ratings.html": "https://www.rlkglaw.com/reviews-ratings.html",
    "contact.html": "https://www.rlkglaw.com/contact.html",
    "will-rountree.html": "https://www.rlkglaw.com/will-rountree.html",
    "hal-leitman.html": "https://www.rlkglaw.com/hal-leitman.html",
    "david-klein.html": "https://www.rlkglaw.com/david-klein.html",
    "will-geer.html": "https://www.rlkglaw.com/will-geer.html",
    "mike-bargar.html": "https://www.rlkglaw.com/mike-bargar.html",
    "ceci-christy.html": "https://www.rlkglaw.com/ceci-christy.html",
    "william-matthews.html": "https://www.rlkglaw.com/william-matthews.html",
    "shawn-eisenberg.html": "https://www.rlkglaw.com/shawn-eisenberg.html",
    "elizabeth-childers.html": "https://www.rlkglaw.com/elizabeth-childers.html",
    "caitlyn-powers.html": "https://www.rlkglaw.com/caitlyn-powers.html",
}

count = 0
for filename, url in pages.items():
    try:
        with open(filename, "r") as fh:
            content = fh.read()
    except FileNotFoundError:
        print(f"NOT FOUND: {filename}")
        continue

    if "og:url" in content:
        print(f"ALREADY HAS og:url: {filename}")
        continue

    tag = f'    <meta property="og:url" content="{url}">'
    new_content = content.replace(
        '<meta property="og:site_name" content="Rountree Leitman Klein & Geer, LLC">',
        '<meta property="og:site_name" content="Rountree Leitman Klein & Geer, LLC">\n' + tag
    )

    if new_content != content:
        with open(filename, "w") as fh:
            fh.write(new_content)
        count += 1
        print(f"Fixed: {filename}")
    else:
        print(f"NO MATCH for og:site_name: {filename}")

print(f"\nTotal files fixed: {count}")
