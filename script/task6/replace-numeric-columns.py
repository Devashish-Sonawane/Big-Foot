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



keys_to_remove = ["Precipitation(in)","ZipCode","Location","Gallons of ethanol per capita age 21 and older",
                  "EndTime","index","Year-Month","Census Rank","Population (age 14 and older)",
                  "Year","State Resident Population","Date","YEAR 4","Gallons of ethanol per capita age 14 and older",
                  "YEAR 1","YEAR 3","Submitted Date","jaccard_score","Gallons of ethanol derived from time-varying ABV",
                  "Submitted Date Time","Gallons of ethanol (absolute alcohol)",
                  "Witness Count","National Park Visitation Count","Fixed Year",
                  "Population (age 21 and older)","LocationLng","State Population Density","LocationLat",
                  "YEAR 2","StartTime","Submitted Year","Id"]  # list of keys for deletion
input_file = "/Users/ekaterinashtyrkova/PycharmProjects/pythonProject1/removing columns/o.json"  # initial json file path
output_file = "nonumerical.json"  # new json file without the keys_to_remove

remove_keys(input_file, output_file, keys_to_remove)