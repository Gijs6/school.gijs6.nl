import os
import re

def extract_indexname(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'indexname:\s*(.+)', content)
        if match:
            return match.group(1).strip()
    return None

def sort_main_dirs(dirs):
    # Sort class folders in descending order (6VWO, 5VWO, ..., 1VWO)
    return sorted(dirs, key=lambda x: int(re.search(r'(\d)VWO', x).group(1)), reverse=True)

def sort_sub_dirs(dirs):
    # Sort the period folders according to the pattern TW4, P4, TW3, P3, TW2, P2, TW1, P1
    def custom_sort_key(name):
        match = re.match(r'([A-Z]+)(\d+)', name)
        if match:
            prefix, number = match.groups()
            number = int(number)
            return (number, 0 if prefix == 'P' else 1)  # P's come after (wel this wil put it first but it is reversed at the end) TW's for the same number
        return (float('inf'), float('inf'))

    return sorted(dirs, key=custom_sort_key, reverse=True)

def generate_markdown():
    directory = os.getcwd()
    output_file = "index.md"
    markdown_content = ["---", "layout: default", "---\n", "# Samenvattingsoverzicht\n"]

    main_dirs = [d for d in os.listdir(directory) if re.match(r'\dVWO', d)]
    sorted_main_dirs = sort_main_dirs(main_dirs)

    for main_dir in sorted_main_dirs:
        markdown_content.append(f"## {main_dir}\n")
        main_path = os.path.join(directory, main_dir)

        sub_dirs = [d for d in os.listdir(main_path) if os.path.isdir(os.path.join(main_path, d))]
        sorted_sub_dirs = sort_sub_dirs(sub_dirs)

        for sub_dir in sorted_sub_dirs:
            markdown_content.append(f"### {sub_dir}\n")
            sub_path = os.path.join(main_path, sub_dir)

            files = sorted([f for f in os.listdir(sub_path) if f.endswith('.md')])  # Sort alphabetically and only md files
            for file in files:
                file_path = os.path.join(sub_path, file)
                indexname = extract_indexname(file_path)
                relative_file_path = os.path.relpath(file_path, directory).replace("\\", "/")
                if indexname:
                    markdown_content.append(f"- [{indexname}]({relative_file_path})\n")
                else:
                    markdown_content.append(f"- [{file}]({relative_file_path})\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_content))

    print("Updated homepage!")

if __name__ == "__main__":
    generate_markdown()
