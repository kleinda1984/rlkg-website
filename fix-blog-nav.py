import glob
import re

count = 0
for f in glob.glob("**/*.html", recursive=True):
    if f.startswith("blog/") or f.startswith("."):
        continue

    with open(f, "r") as fh:
        content = fh.read()

    pattern = r'(<div class="dropdown-section">)\s*\n\s*(<a href=.elizabeth-childers)'
    
    def fix(m):
        global count
        count += 1
        return m.group(1) + '\n                            <div class="dropdown-label">Associates</div>\n                            ' + m.group(2)

    new_content = re.sub(pattern, fix, content)
    if new_content != content:
        with open(f, "w") as fh:
            fh.write(new_content)
        print(f"Fixed: {f}")

print(f"\nTotal files fixed: {count}")
