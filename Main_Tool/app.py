#Plausible
import streamlit as st

st.components.v1.html("""
<script defer data-domain="moonboard-holds-vwbjgpy3ocg24djaqtzmkw.streamlit.app"
        src="https://plausible.io/js/script.js"></script>
""", height=0)
#Plausible

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    remove = ["A1", "A2", "A3", "A4", "B6", "A7", "A8", "A17", "B1", "B2", "B5", "B14", "B17", "C1", "C2", "C3", "C4", "C17", "D1", "D2", "D4", "E1", "E2", "E3", "E4", "E5", "E17", "F1", "F2", "F3", "[...]
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
