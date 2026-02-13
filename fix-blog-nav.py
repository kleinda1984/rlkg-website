import glob

count = 0
for f in glob.glob("**/*.html", recursive=True):
    if f.startswith("blog/") or f.startswith("."):
        continue

    with open(f, "r") as fh:
        content = fh.read()

    if "\x01" in content:
        content = content.replace("\x01", '<div class="dropdown-label">Associates</div>')
        with open(f, "w") as fh:
            fh.write(content)
        count += 1
        print(f"Fixed: {f}")

print(f"\nTotal files fixed: {count}")
