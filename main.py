import streamlit as st
#set the title of the web page
st.write("Hello, World!")

#set a header
st.header("Header")
#set a subheader
st.subheader("Sub-header")

#text input for name
name=st.text_input("enter your name:")
 #dropdown menu for selecting an option
options=["option1","option2","option3"]
selected_option=st.selectbox("choose an option:", options)
#slider for selecting a value 
slider_vaule=st.slider('select a vaule',1,100,50)
#sumbit button 
if st.button("submit"):
    st.write(f"name:{name}")
    st.write(f"secected options:{selected_option}")
    st.write(f"Slider vaule:{slider_vaule}")
#additional information 
    st.subheader("summary")
    st.write("fill out the form above and click the submit button")
#footer