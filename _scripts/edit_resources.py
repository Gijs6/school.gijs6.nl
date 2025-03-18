import json
from home import main

current_year = "4VWO"

def choose(choice_list, things_to_choose, choice_output_list):
    for i in range(len(choice_list)):
        print(f"{i}: {choice_list[i]}")
    choice_input_because_sem_wants_this = input(f"Choose a {things_to_choose}: ")
    try:
        choice_input_int = int(choice_input_because_sem_wants_this)
    except ValueError:
        raise ValueError("Not an int!")
    if choice_input_int < len(choice_list) and choice_input_int >= 0:
        return choice_output_list[choice_input_int], choice_input_int
    else:
        raise IndexError("Not a choice!")

with open("_data/test_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

periods = list(data[current_year].keys())

print(f"Avaiable periods: {periods}")

chosen_period_input = input("Choose a period: ").upper()

if chosen_period_input in periods:
    chosen_period = chosen_period_input
else: 
    raise IndexError("Not a choice!")

tests_this_period = data[current_year][chosen_period]
test_names_this_period = [f"{item['subject']} - {item['test_material']}" for item in tests_this_period]

print(f"Choose a test from {chosen_period}")

chosen_test, chosen_test_index = choose(test_names_this_period, "test", tests_this_period)

res = chosen_test["resources"]

if res:
    print("Current resources")
    for resitem in res:
        print(f"{resitem['title']} ({resitem['link']})")
else:
    print("No resources yet.")

new_res_title = input("Title: ")
new_res_link = input("Link: ")

res.append({
    "link": new_res_link,
    "title": new_res_title
})


data[current_year][chosen_period][chosen_test_index]["resources"] = res

with open("_data/test_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Updating homepagedata...")

main()
