import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Fix Mobile Navigation (Add Pubs and Conferences)
mobile_nav_start = content.find('<!-- Mobile Bottom Navigation -->')
mobile_nav_end = content.find('<!-- Main Content -->')
if mobile_nav_start != -1 and mobile_nav_end != -1:
    mobile_nav_html = """
    <!-- Mobile Bottom Navigation -->
    <nav class="md:hidden fixed bottom-0 left-0 w-full bg-white/90 backdrop-blur-md border-t border-teal-100 z-50 flex justify-around py-3 dark:bg-black/90 dark:border-teal-900">
        <a href="#about" class="flex flex-col items-center gap-1 text-outline nav-link active" data-target="about">
            <span class="material-symbols-outlined text-[20px]">person</span>
            <span class="text-[9px] font-bold uppercase">About</span>
        </a>
        <a href="#experience" class="flex flex-col items-center gap-1 text-outline nav-link" data-target="experience">
            <span class="material-symbols-outlined text-[20px]">work</span>
            <span class="text-[9px] font-bold uppercase">Exp</span>
        </a>
        <a href="#projects" class="flex flex-col items-center gap-1 text-outline nav-link" data-target="projects">
            <span class="material-symbols-outlined text-[20px]">analytics</span>
            <span class="text-[9px] font-bold uppercase">Work</span>
        </a>
        <a href="#skills" class="flex flex-col items-center gap-1 text-outline nav-link" data-target="skills">
            <span class="material-symbols-outlined text-[20px]">school</span>
            <span class="text-[9px] font-bold uppercase">Skills</span>
        </a>
        <a href="#publications" class="flex flex-col items-center gap-1 text-outline nav-link" data-target="publications">
            <span class="material-symbols-outlined text-[20px]">menu_book</span>
            <span class="text-[9px] font-bold uppercase">Pubs</span>
        </a>
        <a href="#conferences" class="flex flex-col items-center gap-1 text-outline nav-link" data-target="conferences">
            <span class="material-symbols-outlined text-[20px]">groups</span>
            <span class="text-[9px] font-bold uppercase">Conf</span>
        </a>
    </nav>
    """
    content = content[:mobile_nav_start] + mobile_nav_html + content[mobile_nav_end:]

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
