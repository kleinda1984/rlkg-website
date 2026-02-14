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

    content = content.replace("/practice-areas\x27>Business Bankruptcy</a>", "/business-bankruptcy\x27>Business Bankruptcy</a>")
    content = content.replace("/practice-areas\x27>Personal Bankruptcy</a>", "/personal-bankruptcy\x27>Personal Bankruptcy</a>")
    content = content.replace("/practice-areas\x27>Debtor / Creditor</a>", "/debtor-creditor\x27>Debtor &amp; Creditor Rights</a>")
    content = content.replace("/practice-areas\x27>Litigation</a>", "/litigation\x27>Litigation</a>")
    content = content.replace("/practice-areas\x22>Business Bankruptcy</a>", "/business-bankruptcy\x22>Business Bankruptcy</a>")
    content = content.replace("/practice-areas\x22>Personal Bankruptcy</a>", "/personal-bankruptcy\x22>Personal Bankruptcy</a>")
    content = content.replace("/practice-areas\x22>Debtor / Creditor</a>", "/debtor-creditor\x22>Debtor &amp; Creditor Rights</a>")
    content = content.replace("/practice-areas\x22>Litigation</a>", "/litigation\x22>Litigation</a>")

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        fixed += 1
        print("  Fixed:", fpath)

print("Done:", fixed, "files updated,", len(all_files) - fixed, "skipped.")
