import re

with open('index.html', 'r') as f:
    content = f.read()

# 2. Fix Duplicate Section Tag (Remove extra conferences section)
# I'll look for the specific block I saw earlier:
# <section id="conferences" class="content-section">
# <section id="conferences" class="content-section">
content = re.sub(r'<section id="conferences" class="content-section">\s*<section id="conferences" class="content-section">',
                 '<section id="conferences" class="content-section">', content)

# 3. Ensure Publications and Conferences titles are full and descriptive
# Already seem okay in the current version based on my previous cat, but let's double check.

with open('index.html', 'w') as f:
    f.write(content)

print("Portfolio fixed.")
