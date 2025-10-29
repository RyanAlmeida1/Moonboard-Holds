import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st


df17 = pd.read_csv("Main_Tool/Data/Analysis_Data2017")
df19 = pd.read_csv("Main_Tool/Data/Analysis_Data2019")
df16 = pd.read_csv("Main_Tool/Data/Analysis_Data2016")

user_set = st.selectbox("Enter Moonboard Set", ['2016','2017','2019'])
user_hold = st.text_input("Enter Hold (Ex. 'J12'): ") 
    
year = ""

if user_set == "2017":
    year = df17
    st.image("Main_Tool/Set_Images/mbsetup-mbm2017.jpg", width=500)
elif user_set == "2019":
    year = df19
    st.image("Main_Tool/Set_Images/mbsetup-mbm2019.jpg", width=500)
else:
    year = df16
    st.image("Main_Tool/Set_Images/mbsetup-2016.jpg", width=500)

letters = ["A","B","C","D","E","F","G","H","I","J","K"]
hold_types = []
for i in range(11):
    for j in range(18):
        hold_types.append(f"{letters[i]}{j + 1}")
        
#For 2016
if user_set == "2016":
    remove = ["A1", "A2", "A3", "A4", "B6", "A7", "A8", "A17", "B1", "B2", "B5", "B14", "B17", "C1", "C2", "C3", "C4", "C17", "D1", "D2", "D4", "E1", "E2", "E3", "E4", "E5", "E17", "F1", "F2", "F3", "F4", "F17", "F18", "G1", "G3", "G5", "H1", "H2", "H3", "H4", "H6", "H17", "I1", "I2", "I3", "I17", "J1", "J3", "J4", "J15", "J17", "J18", "K1", "K2", "K3", "K4", "K15", "K17"]
    for hold in remove:
        hold_types.remove(hold)

if user_hold not in hold_types:
    st.text("Hold Doesn't Exist")

grades = ["6A+", "6B", "6B+", "6C", "6C+", "7A", "7A+", "7B", "7B+", "7C", "7C+", "8A", "8A+", "8B", "8B+"]

figure = plt.figure()
plt.bar(grades, year[user_hold], color="blue")
plt.title(user_hold)
plt.xlabel("Grade")
plt.ylabel("Frequency (Out of 100)")

st.pyplot(figure)
