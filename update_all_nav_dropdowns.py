#!/usr/bin/env python3
"""
Update all site pages to add Jonathan Clements to the Our Team dropdown menu.
Handles both URL formats (double-quote .html and single-quote root-relative).
Handles blog/ subdirectory relative paths.

Usage: python3 update_all_nav_dropdowns.py
"""

import os
import re
import glob

SKIP_CHECK = "jonathan-clements"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if filepath.endswith('jonathan-clements.html'):
        print(f"  SKIPPED (Jonathan's own page): {filepath}")
        return False
    
    if SKIP_CHECK in content:
        print(f"  SKIPPED (already updated): {filepath}")
        return False
    
    pattern = re.compile(
        r'(<div\s+class=["\']dropdown-label["\']>Associates</div>\s*'
        r'(?:\s*<a\s+href=["\'][^"\']+["\']>[^<]+</a>\s*)+)'
        r'(\s*</div>)',
        re.DOTALL
    )
    
    match = pattern.search(content)
    if not match:
        print(f"  SKIPPED (no Associates dropdown found): {filepath}")
        return False
    
    associates_block = match.group(1)
    
    # Detect if we're in a subdirectory (blog/) and need ../ prefix
    prefix = "../" if filepath.startswith("blog/") or "/blog/" in filepath else ""
    
    # Detect quote style and URL format from existing links
    if 'href="' in associates_block:
        jonathan_link = f'<a href="{prefix}jonathan-clements.html">Jonathan Clements</a>'
    else:
        jonathan_link = f"<a href='{prefix}jonathan-clements.html'>Jonathan Clements</a>"
    
    link_pattern = re.compile(r'^(\s*)<a\s+href=', re.MULTILINE)
    link_matches = list(link_pattern.finditer(associates_block))
    indent = link_matches[-1].group(1) if link_matches else "                  "
    
    new_link = f"\n{indent}{jonathan_link}"
    new_content = content[:match.end(1)] + new_link + content[match.start(2):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  UPDATED: {filepath}")
    return True

def main():
    html_files = glob.glob('**/*.html', recursive=True)
    if not html_files:
        print("No HTML files found. Make sure you're running this from the website root directory.")
        return
    
    print(f"Found {len(html_files)} HTML files. Updating nav dropdowns...\n")
    updated = 0
    for filepath in sorted(html_files):
        if update_file(filepath):
            updated += 1
    print(f"\nDone! Updated {updated} files.")

if __name__ == '__main__':
    main()
