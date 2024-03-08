import json


def remove_keys_recursively(data, keys_to_remove):
    if isinstance(data, dict):
        for key in data.keys():
            if key in keys_to_remove:
                data[key] = ""
            else:
                remove_keys_recursively(data[key], keys_to_remove)
    elif isinstance(data, list):
        for item in data:
            remove_keys_recursively(item, keys_to_remove)


def remove_keys(input_file, output_file, keys_to_remove):
    # opening the initial json for reading
    with open(input_file, 'r') as f:
        data = json.load(f)

    # deleting the 'keys_to_remove'
    remove_keys_recursively(data, keys_to_remove)

    # writing the changed data into a new json file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)



keys_to_remove = ["City","MAMMAL 4","Follow-up","Month","Other Witnesses", "Environment","State","MAMMAL 1","Headline","Nearest NP","Nearest Town","Location Details","Time and Conditions","Other Stories","Formatted Address","Nearest Road","County","MAMMAL 3","MAMMAL 2","Observed","Follow-up Report","Season"]  # list of keys for deletion
input_file = "/Users/ekaterinashtyrkova/PycharmProjects/pythonProject1/removing columns/o.json"  # initial json file path
output_file = "notext.json"  # new json file without the keys_to_remove

remove_keys(input_file, output_file, keys_to_remove)