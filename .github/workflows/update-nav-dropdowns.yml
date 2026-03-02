#!/usr/bin/env python3
"""
Update all site pages to add Jonathan Clements to the Our Team dropdown menu.
Uses regex to handle all formatting variations across pages.

Usage: python3 update_all_nav_dropdowns.py
"""

import os
import re
import glob

SKIP_CHECK = "jonathan-clements"
JONATHAN_LINK = "<a href='/jonathan-clements'>Jonathan Clements</a>"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip Jonathan's own page
    if filepath.endswith('jonathan-clements.html'):
        print(f"  SKIPPED (Jonathan's own page): {filepath}")
        return False
    
    # Skip if already updated
    if SKIP_CHECK in content:
        print(f"  SKIPPED (already updated): {filepath}")
        return False
    
    # Strategy: Find the Associates dropdown section using regex.
    # Match the Associates label, then all associate links, then the closing </div>.
    # Insert Jonathan's link just before the closing </div>.
    pattern = re.compile(
        r'(<div\s+class="dropdown-label">Associates</div>\s*'
        r'(?:\s*<a\s+href=\'[^\']+\'>[^<]+</a>\s*)+)'
        r'(\s*</div>)',
        re.DOTALL
    )
    
    match = pattern.search(content)
    if not match:
        print(f"  SKIPPED (no Associates dropdown found): {filepath}")
        return False
    
    # Figure out the indentation used by existing links
    associates_block = match.group(1)
    link_pattern = re.compile(r'^(\s*)<a\s+href=', re.MULTILINE)
    link_matches = list(link_pattern.finditer(associates_block))
    
    if link_matches:
        indent = link_matches[-1].group(1)
    else:
        indent = "                  "
    
    # Insert Jonathan's link after the last associate link
    new_link = f"\n{indent}{JONATHAN_LINK}"
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
