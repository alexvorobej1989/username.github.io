import os
import re

files_to_update = ['index.html', 'catalog.html', 'materials.html', 'care.html']

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix missing bracket after `classList.remove('hidden');` for the care page routing block.
        # Let's target the exact injection we did
        
        # Replace 1
        bad_1 = "if(care) care.classList.remove('hidden');\n                  if (anchorId) {"
        good_1 = "if(care) care.classList.remove('hidden');\n                  }\n                  if (anchorId) {"
        
        # Replace 2 (incase of different indentation)
        bad_2 = "if(care) care.classList.remove('hidden');\n          if (anchorId) {"
        good_2 = "if(care) care.classList.remove('hidden');\n          }\n          if (anchorId) {"
        
        bad_3 = "if (care) care.classList.remove('hidden');\n          if (anchorId) {"
        good_3 = "if (care) care.classList.remove('hidden');\n          }\n          if (anchorId) {"

        if bad_1 in content:
            content = content.replace(bad_1, good_1)
        if bad_2 in content:
            content = content.replace(bad_2, good_2)
        if bad_3 in content:
            content = content.replace(bad_3, good_3)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Missing bracket syntax errors fixed.")
