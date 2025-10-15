import json
import pandas as pd

# problem data used is shared by GitHub user musoke

with open("Problems/2016problems.json", "r") as file:
    mdata = json.load(file)

#number of climbs total
tclimbs = mdata["total"]

#all holds used by every climb (large)
holds = []
for i in range(len(mdata["data"])):
    for j in range(len(mdata["data"][i]["moves"])):
        holds.append(mdata["data"][i]["moves"][j]["description"])

#list of every type of hold
letters = ["A","B","C","D","E","F","G","H","I","J","K"]
hold_types = []
for i in range(11):
    for j in range(18):
        hold_types.append(f"{letters[i]}{j + 1}")

#For 2016
remove = ["A1", "A2", "A3", "A4", "B6", "A7", "A8", "A17", "B1", "B2", "B5", "B14", "B17", "C1", "C2", "C3", "C4", "C17", "D1", "D2", "D4", "E1", "E2", "E3", "E4", "E5", "E17", "F1", "F2", "F3", "F4", "F17", "F18", "G1", "G3", "G5", "H1", "H2", "H3", "H4", "H6", "H17", "I1", "I2", "I3", "I17", "J1", "J3", "J4", "J15", "J17", "J18", "K1", "K2", "K3", "K4", "K15", "K17"]
for hold in remove:
    hold_types.remove(hold)

#list of amount of a hold type in every climb
hold_type_count = []
for i in range(len(hold_types)):
    hold_type_count.append(holds.count(hold_types[i]))

#create final dictionary of percent of hold types in all climbs
tpercent = {}
for i in range(len(hold_types)):
    tpercent.update({hold_types[i]: f"{round((hold_type_count[i] / tclimbs) * 100, 2)}%"})


hold_type_per_grade = {}
grades = ["6A+", "6B", "6B+", "6C", "6C+", "7A", "7A+", "7B", "7B+", "7C", "7C+", "8A", "8A+", "8B", "8B+"]


#list of holds by grade
hold_type_per_grade_list_temp = []
for k in range(len(grades)):
    for i in range(len(mdata["data"])):
        if mdata["data"][i]["grade"] == grades[k]:
            for j in range(len(mdata["data"][i]["moves"])):
                hold_type_per_grade_list_temp.append(mdata["data"][i]["moves"][j]["description"])
    hold_type_per_grade.update({grades[k]: hold_type_per_grade_list_temp})
    hold_type_per_grade_list_temp = []


#Create final dictionary
product = {}
holds_by_grade_list = []
for hold in hold_types:
    holds_by_grade_list = []
    for grade in grades:
            
        holds_by_grade_list.append(round((hold_type_per_grade[grade].count(hold)/holds.count(hold)) * 100, 2))
    product.update({hold: holds_by_grade_list})



Analysis_Data = pd.DataFrame(product)

Analysis_Data.to_csv("Analysis_Data")