import json

def insert_line_at(filename, text, line_number=4):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        lines[3] = "test_code: " + text + "\n---\n"
        
        with open(filename, 'w') as file:
            file.writelines(lines)
        
        print(f'Tekst succesvol ingevoegd op lijn {line_number}')
    except FileNotFoundError:
        print(f'Fout: Bestand "{filename}" niet gevonden.')
    except Exception as e:
        print(f'Er is een fout opgetreden: {e}')


with open("_data/test_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for year, yeardata in data.items():
    for period, perioddata in yeardata.items():
        for item in perioddata:
            if item["summary_link"]:
                file_path = item["summary_link"][1:] + ".md"
                insert_line_at(file_path, item["test_code"])