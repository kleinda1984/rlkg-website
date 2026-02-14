"""
Update footer Practice Area links on all pages to point to individual
practice area pages instead of /practice-areas.
"""
import os
import re
import glob

replacements = [
    ("Business Bankruptcy", "/business-bankruptcy"),
    ("Personal Bankruptcy", "/personal-bankruptcy"),
    ("Debtor / Creditor", "/debtor-creditor"),
    ("Litigation", "/litigation"),
]

fixed = 0
skipped = 0

print(f"Working directory: {os.getcwd()}")
all_files = glob.glob('*.html') + glob.glob('blog/*.html')
print(f"Found {len(all_files)} HTML files")

for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for label, new_href in replacements:
        pattern = r"""<a\s+href=["']/practice-areas["']>\s*""" + re.escape(label) + r"""\s*</a>"""
        replacement = f'<a href="{new_href}">{label}</a>'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed += 1
        print(f"  Fixed: {fpath}")
    else:
        skipped += 1

print(f"\nDone: {fixed} files updated, {skipped} files skipped.")
