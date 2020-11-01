states_abb = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

import csv
import os

# Files
file_to_load = os.path.join("raw_data", "people.csv")
file_to_output = os.path.join("raw_data", "people_reformatted.csv")

# Placeholders 
person_ids = []
person_first_names = []
person_last_names = []
person_dobs = []
person_ssns = []
person_states = []

# Read and converst csv to dicts
with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    for row in reader:
        
        person_ids = person_ids + [row[0]]

        split_name = row[1].split(" ")

        person_first_names = person_first_names + [split_name[0]]
        person_last_names = person_last_names + [split_name[1]]

        # DOB
        dob = row[2].split("-")
        year = dob[0]
        month = dob[1]
        day = dob[2]
        reformatted_dob = f"{month}/{day}/{year}"

        person_dobs.append(reformatted_dob)

        # SSN
        split_ssn = list(row[3])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        person_ssns.append(joined_ssn)

        # States
        state_abbrev = states_abb[row[4]]

        person_states.append(state_abbrev)



# Zip 
empdb = zip(person_ids, person_first_names, person_last_names,
            person_dobs, person_ssns, person_states)

# Write to csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                    "DOB", "SSN", "State"])
    writer.writerows(empdb)
