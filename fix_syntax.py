import os

files_to_update = ['index.html', 'catalog.html', 'materials.html', 'care.html']

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix the syntax error from previous script in different indentations
        broken_1 = "}\n                  } else if (pageId === 'care') {"
        fixed_1 = "} else if (pageId === 'care') {"
        
        broken_2 = "}\n          } else if (pageId === 'care') {"
        fixed_2 = "} else if (pageId === 'care') {"
        
        broken_3 = "}\n        } else if (pageId === 'care') {"
        fixed_3 = "} else if (pageId === 'care') {"

        if broken_1 in content:
            content = content.replace(broken_1, fixed_1)
        if broken_2 in content:
            content = content.replace(broken_2, fixed_2)
        if broken_3 in content:
            content = content.replace(broken_3, fixed_3)
            
        # specifically in care.html:
        broken_4 = "        }\n        } else if (pageId === 'care') {"
        fixed_4 = "        } else if (pageId === 'care') {"
        
        broken_5 = "                  }\n                  } else if (pageId === 'care') {"
        fixed_5 = "                  } else if (pageId === 'care') {"

        if broken_4 in content:
            content = content.replace(broken_4, fixed_4)
        if broken_5 in content:
            content = content.replace(broken_5, fixed_5)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Syntax errors fixed.")
