#!/usr/bin/env python3
"""
Update all site pages to add Jonathan Clements to the Our Team dropdown menu.

Usage: Place this script in the root of your website repo and run:
    python3 update_all_nav_dropdowns.py

It will find all .html files and add Jonathan Clements to the Associates 
dropdown section (after William D. Matthews).
"""

import os
import glob

# The line to find (last associate currently in dropdown)
FIND_LINE = "<a href='/william-matthews'>William D. Matthews</a>"

# What to replace it with (same line + new entry)
REPLACE_WITH = """<a href='/william-matthews'>William D. Matthews</a>
                  <a href='/jonathan-clements'>Jonathan Clements</a>"""

# Skip files that have already been updated
SKIP_CHECK = "jonathan-clements"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already updated
    if SKIP_CHECK in content and 'jonathan-clements.html' not in filepath:
        print(f"  SKIPPED (already updated): {filepath}")
        return False
    
    # Skip Jonathan's own page
    if filepath.endswith('jonathan-clements.html'):
        print(f"  SKIPPED (Jonathan's own page): {filepath}")
        return False
    
    if FIND_LINE not in content:
        print(f"  SKIPPED (no matching nav found): {filepath}")
        return False
    
    new_content = content.replace(FIND_LINE, REPLACE_WITH)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  UPDATED: {filepath}")
    return True

def main():
    # Find all HTML files in current directory and subdirectories
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
