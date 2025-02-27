import os
import re

def extract_indexname(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'indexname:\s*(.+)', content)
        if match:
            return match.group(1).strip()
    return None

def generate_markdown():
    directory = os.getcwd()
    output_file = "index.markdown"
    markdown_content = []
    
    for root, dirs, files in os.walk(directory):
        if "VWO" in root:
            relative_path = os.path.relpath(root, directory)
            depth = relative_path.count(os.sep)
            if relative_path != ".":
                header_level = "#" * (depth + 1)
                markdown_content.append(f"{header_level} {os.path.basename(root)}\n")
            
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    indexname = extract_indexname(file_path)
                    relative_file_path = os.path.relpath(file_path, directory).replace(".md", "")
                    if indexname:
                        markdown_content.append(f"- ({indexname})[{relative_file_path}]\n")
                    else:
                        markdown_content.append(f"- ({file})[{relative_file_path}]\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_content))

    print("Updated homepage!")

if __name__ == "__main__":
    generate_markdown()
