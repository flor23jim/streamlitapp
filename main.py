import streamlit as st
from datetime import datetime,date

def calcuate_age(birthdate):
    today= date.today()
    age=today.year - birthdate.year -((today.month, today.day)<(birthdate.month,birthdate.day))
#set the title of the web page
st.write("Hello, World!")

#set a header
st.header("Header")
#set a subheader
st.subheader("Sub-header")

#text input for name
st.subheader("Personal Details")
name=st.text_input("enter your name:")
 #dropdown menu for selecting an option
options=["option1","option2","option3"]
selected_option=st.selectbox("choose an option:", options)
#slider for selecting a value 
slider_vaule= st.slider("select a vaule",1,100,50)
#radio button for selecting gender
gender=st.radio("selecting your gender:",("male","female"))
#Checkbox for selecting hobbies 
hobbies=[]
st.header("select your hobbies")
if st.checkbox("Reading"):
    hobbies.append("reading")
if st.checkbox('traveling'):
    hobbies.append("Traveling")
    if st.checkbox("cooking"):
        hobbies.append("cooking")

#Date pciker for selecting a birthdate
birthdate=st.date_input("Select your birthdate:",datetime(200,1,1))
#sumbit button 
if st.button("submit"):
    age=calcuate_age(birthdate)
    st.subheader("submitted information")
    st.write(f"name:{name}")
    st.write(f"secected options:{selected_option}")
    st.write(f"Slider vaule:{slider_vaule}")
    st.write(f"Gender:{gender}")
    st.write(f"hobbies:{','.join(hobbies)if hobbies else 'None'}")
    st.write(f"birthdate:{birthdate}")
    st.write(f"Age:{age}")
#additional information 
    st.subheader("summary")
    st.write("fill out the form above and click the submit button")
#footer