from xml.dom.minidom import Notation
import streamlit as st

st.title("User information form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

with st.form(key="user_form"):
    form_values["name"] = st.text_input("Enter your name:")
    form_values["height"] = st.number_input("Enter your Height (in cms):")
    form_values["gender"] = st.selectbox("Select your gender:", ["Male", "Female", "Others"])
    form_values["dob"] = st.date_input("Enter your date of birth:")

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill out all the fields in the form")
        else:
            st.balloons()
            st.write("##Form submitted successfully!")
            for (key,value)in form_values.items():
                st.write(f"{key}: {value}")


