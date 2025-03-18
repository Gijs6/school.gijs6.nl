import json
import os
import yaml
import re

def sort_years(yearstr):
    match = re.match(r"(\d)(VWO)", yearstr)
    return -int(match.group(1)) if match else float("inf")

def sort_period(period):
    match = re.match(r"([A-Z]+)(\d+)", period)
    if match:
        return (int(match.group(2)), match.group(1))
    return (float("inf"), period)

def sort_subjects(subjectdata):
    return subjectdata["subject"]

def extract_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1))
    return []

def extract_test_code(file_path):
    front_matter = extract_front_matter(file_path)
    if front_matter and 'test_code' in front_matter:
        test_code = front_matter['test_code']
        if isinstance(test_code, str):
            test_code = [test_code]
        return test_code
    return []

def main():

    with open("_data/test_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    directory = os.getcwd()

    main_dirs = [d for d in os.listdir(directory) if re.match(r'\dVWO', d)]

    for main_dir in main_dirs:
        main_path = os.path.join(directory, main_dir)
        sub_dirs = [d for d in os.listdir(main_path) if os.path.isdir(os.path.join(main_path, d))]
        for sub_dir in sub_dirs:
            sub_path = os.path.join(main_path, sub_dir)
            files = [f for f in os.listdir(sub_path) if f.endswith('.md')]
            for file in files:
                file_path = os.path.join(sub_path, file)
                test_code = extract_test_code(file_path)
                for filedata in filter(lambda t: t["test_code"] in test_code, data[main_dir][sub_dir]):
                    filedata["summary_link"] = f"/{main_dir}/{sub_dir}/{file.replace(".md", "")}"

    sorted_data = {}
        
    for year in sorted(data.keys(), key=sort_years):
        year_data = {}
        
        for period in sorted(data[year].keys(), key=sort_period, reverse=True):
            if [test for test in data[year][period] if test.get("summary_link") or test.get("resources")]: # If in the entire period there are tests with a summary or any other resource
                tests_to_include = [test for test in data[year][period] if test.get("make_summary") or test.get("resources")]
                year_data[period] = sorted(tests_to_include, key=sort_subjects)
        
        if year_data:
            sorted_data[year] = year_data

    with open("_data/homepage_data.json", "w", encoding="utf-8") as f:
        json.dump(sorted_data, f, indent=4)

if __name__ == "__main__":
    main()