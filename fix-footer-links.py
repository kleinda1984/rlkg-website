"""
Update footer Practice Area links on all pages to point to individual
practice area pages instead of /practice-areas.

Run via GitHub Actions workflow.
"""
import os
import glob

old_links = [
    "<li><a href='/practice-areas'>Business Bankruptcy</a></li>",
    "<li><a href='/practice-areas'>Personal Bankruptcy</a></li>",
    "<li><a href='/practice-areas'>Debtor / Creditor</a></li>",
    "<li><a href='/practice-areas'>Litigation</a></li>",
]

new_links = {
    "<li><a href='/practice-areas'>Business Bankruptcy</a></li>": "<li><a href='/business-bankruptcy'>Business Bankruptcy</a></li>",
    "<li><a href='/practice-areas'>Personal Bankruptcy</a></li>": "<li><a href='/personal-bankruptcy'>Personal Bankruptcy</a></li>",
    "<li><a href='/practice-areas'>Debtor / Creditor</a></li>": "<li><a href='/debtor-creditor'>Debtor &amp; Creditor Rights</a></li>",
    "<li><a href='/practice-areas'>Litigation</a></li>": "<li><a href='/litigation'>Litigation</a></li>",
}

fixed = 0
skipped = 0

print(f"Working directory: {os.getcwd()}")
all_files = glob.glob('*.html') + glob.glob('blog/*.html')
print(f"Found {len(all_files)} HTML files")

for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for old, new in new_links.items():
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed += 1
        print(f"  Fixed: {fpath}")
    else:
        skipped += 1

print(f"\nDone: {fixed} files updated, {skipped} files skipped.")
