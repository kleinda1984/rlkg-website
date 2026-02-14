"""
Update footer Practice Area links on all pages.
"""
import os
import glob

print(f"Working directory: {os.getcwd()}")
all_files = glob.glob('*.html') + glob.glob('blog/*.html')
print(f"Found {len(all_files)} HTML files")

# Debug: show what's actually in the first file
with open(all_files[0], 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('practice-areas')
if idx >= 0:
    print(f"DEBUG sample from {all_files[0]}:")
    print(repr(text[idx-20:idx+40]))
else:
    print(f"DEBUG: 'practice-areas' not found in {all_files[0]}")

fixed = 0
for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = content.replace("/practice-areas'>Business Bankruptcy</a>", "/business-bankruptcy'>Business Bankruptcy</a>")
    content = content.replace("/practice-areas'>Personal Bankruptcy</a>", "/personal-bankruptcy'>Personal Bankruptcy</a>")
    content = content.replace("/practice-areas'>Debtor / Creditor</a>", "/debtor-creditor'>Debtor &amp; Creditor Rights</a>")
    content = content.replace("/practice-areas'>Litigation</a>", "/litigation'>Litigation</a>")
    content = content.replace('/practice-areas">Business Bankruptcy</a>', '/business-bankruptcy">Business Bankruptcy</a>')
    content = content.replace('/practice-areas">Personal Bankruptcy</a>', '/personal-bankruptcy">Personal Bankruptcy</a>')
    content = content.replace('/practice-areas">Debtor / Creditor</a>', '/debtor-creditor">Debtor &amp; Creditor Rights</a>')
    content = content.replace('/practice-areas">Litigation</a>', '/litigation">Litigation</a>')

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed += 1
        print(f"  Fixed: {fpath}")

print(f"\nDone: {fixed} files updated, {len(all_files) - fixed} skipped.")
