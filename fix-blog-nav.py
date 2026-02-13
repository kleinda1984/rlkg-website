import glob
import re

count = 0
for f in glob.glob("**/*.html", recursive=True):
    with open(f, "r") as fh:
        content = fh.read()

    pattern = r"(>Associates</div>)(.*?)(</div>\s*</div>\s*</li>)"

    def reorder(m):
        global count
        prefix = m.group(1)
        block = m.group(2)
        suffix = m.group(3)

        links = re.findall(r"<a\s+href=['\"][^'\"]*['\"]>[^<]+</a>", block)
        if len(links) != 4:
            return m.group(0)

        link_map = {}
        for link in links:
            name = re.search(r">([^<]+)<", link).group(1)
            last = name.strip().split()[-1].lower()
            link_map[last] = link

        desired = ["childers", "powers", "eisenberg", "matthews"]
        if not all(k in link_map for k in desired):
            return m.group(0)

        current = [re.search(r">([^<]+)<", l).group(1).strip().split()[-1].lower() for l in links]
        if current == desired:
            return m.group(0)

        indent = "\n                            "
        new_block = indent + indent.join(link_map[k] for k in desired) + "\n                        "
        count += 1
        return prefix + new_block + suffix

    new_content = re.sub(pattern, reorder, content, flags=re.DOTALL)
    if new_content != content:
        with open(f, "w") as fh:
            fh.write(new_content)
        print(f"Fixed: {f}")

print(f"\nTotal files fixed: {count}")
