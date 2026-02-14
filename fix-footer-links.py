"""
Update footer Practice Area links on all pages to point to individual
practice area pages instead of /practice-areas.

Run via GitHub Actions workflow.
"""
import os
import glob

old_footer = """                    <li><a href='/practice-areas'>Business Bankruptcy</a></li>
                    <li><a href='/practice-areas'>Personal Bankruptcy</a></li>
                    <li><a href='/practice-areas'>Debtor / Creditor</a></li>
                    <li><a href='/practice-areas'>Litigation</a></li>"""

new_footer = """                    <li><a href='/business-bankruptcy'>Business Bankruptcy</a></li>
                    <li><a href='/personal-bankruptcy'>Personal Bankruptcy</a></li>
                    <li><a href='/debtor-creditor'>Debtor &amp; Creditor Rights</a></li>
                    <li><a href='/litigation'>Litigation</a></li>"""

fixed = 0
skipped = 0

# Process all HTML files in root and blog/
patterns = ['*.html', 'blog/*.html']
for pattern in patterns:
    for fpath in glob.glob(pattern):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_footer in content:
            content = content.replace(old_footer, new_footer)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1
            print(f"  Fixed: {fpath}")
        else:
            skipped += 1

print(f"\nDone: {fixed} files updated, {skipped} files skipped (already correct or different format).")
