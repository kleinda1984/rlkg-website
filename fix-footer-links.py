import os
import glob

print("Working directory:", os.getcwd())
all_files = glob.glob("*.html") + glob.glob("blog/*.html")
print("Found", len(all_files), "HTML files")

fixed = 0
for fpath in all_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    content = content.replace("practice-areas\">Business Bankruptcy", "business-bankruptcy\">Business Bankruptcy")
    content = content.replace("practice-areas\">Personal Bankruptcy", "personal-bankruptcy\">Personal Bankruptcy")
    content = content.replace("practice-areas\">Debtor / Creditor", "debtor-creditor\">Debtor &amp; Creditor Rights")
    content = content.replace("practice-areas\">Litigation", "litigation\">Litigation")
    content = content.replace("practice-areas'>Business Bankruptcy", "business-bankruptcy'>Business Bankruptcy")
    content = content.replace("practice-areas'>Personal Bankruptcy", "personal-bankruptcy'>Personal Bankruptcy")
    content = content.replace("practice-areas'>Debtor / Creditor", "debtor-creditor'>Debtor &amp; Creditor Rights")
    content = content.replace("practice-areas'>Litigation", "litigation'>Litigation")

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        fixed += 1
        print("  Fixed:", fpath)

print("Done:", fixed, "files updated,", len(all_files) - fixed, "skipped.")
