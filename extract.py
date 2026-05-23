import os

src_path = "/Users/slowtyper/.gemini/antigravity/brain/57af01dc-eb29-4c88-88f9-eb184acf3b15/.system_generated/steps/6/content.md"
dest_dir = "themes/neon/layouts/posts"
dest_path = os.path.join(dest_dir, "unsafe-audit.html")

print(f"Reading source from {src_path}...")
if not os.path.exists(src_path):
    # Fallback to check relative or alternative paths if needed
    raise FileNotFoundError(f"Source file not found at: {src_path}")

with open(src_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the start of the HTML page
html_start = content.find("<!DOCTYPE html>")
if html_start == -1:
    raise ValueError("Could not find start of HTML document in source file!")

html_content = content[html_start:]

# Inject home link in navigation bar
# Original: <span class="brand"><span class="dot"></span>unsafe in Bun</span>
old_nav = '<span class="brand"><span class="dot"></span>unsafe in Bun</span>'
new_nav = '<a href="/" class="brand" style="color:var(--tx);text-decoration:none"><span class="dot"></span>unsafe in Bun · ~/blog</a>'

if old_nav in html_content:
    print("Found navigation brand in source. Injecting homepage backlink...")
    html_content = html_content.replace(old_nav, new_nav)
else:
    print("WARNING: Could not find original navigation brand text for replacement!")

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Write out the processed HTML as the Hugo layout template
print(f"Writing layout template to {dest_path}...")
with open(dest_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Extraction completed successfully!")
print("Next steps: Run 'hugo server' and visit http://localhost:1313/posts/bun-unsafe-audit/ to see it live!")
