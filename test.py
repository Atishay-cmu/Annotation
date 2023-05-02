import streamlit as st
from PIL import Image
from datetime import datetime
from random import choice, randint, shuffle
import pickle as pkl
import os

# Define a function that will only be executed once
def setup():
    image = set()
    while(len(image) < 4):
        img_path = choice(["b-f", "b-m", "w-f", "w-m"])
        img_name = choice(os.listdir(img_path)[1:])
        image.add(os.path.join(img_path, img_name))
    image = list(image)
    shuffle(image)
    st.session_state["page"] = "intro"
    st.session_state["image"] = image
    st.session_state["current image"] = image[0]
    st.session_state["counter"] = 0
    st.session_state["saved_data"] = []

# Use session state to keep track of whether setup has been run
if "setup_has_run" not in st.session_state:
    st.session_state.setup_has_run = True
    setup()

def intro():
    # The rest of your app goes here
    st.title("Welcome to the survey!")
    st.write("In this survey, you will be shown 5 images, one at a time. You would be asked a series of questions for each question, " +
            "which you are supposed to answer based solely on the image. Some of these may be subjective, but we would like you to answer them as best as you can. " + 
            "All questions are mandatory and you will not be able to complete the survey until you have answered all of them. Thank you for your time and participation.")
    st.write("Please note that you may be shown the same image multiple times, in that case, please try to answer the questions as closely as possible.")
    st.write("Thank you for your time and participation.")
    st.write("Please enter you prolific ID below.")
    prolific_id = st.text_input("Prolific ID")
    st.write("Please click on the button below to start the survey.")
    if st.button("Start"):
        if prolific_id == "":
            st.error("Please enter your prolific ID.")
        else:
            st.session_state['saved_data'].append(["prolific_id", prolific_id])
            st.session_state["page"] = "survey"
            st.experimental_rerun()

def logic():
    st.session_state["counter"] += 1
    if st.session_state["counter"] == 4:
        st.session_state["current image"] = st.session_state["image"][0]
    elif st.session_state["counter"] < 4:
        st.session_state["current image"] = st.session_state["image"][st.session_state["counter"]]
    else:
        st.session_state["page"] = "extra notes"

def survey():
    with st.form("my_form"):
        st.title('Image annotation survey: Image ' + str(st.session_state["counter"] + 1))
        image = Image.open(st.session_state["current image"])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            st.image(image, use_column_width=False)
        with col3:
            st.write(' ')

        question = "Please select the perceived gender of the person in this picture?" + (" "*st.session_state["counter"])
        answers = ["", "Male", "Female", "Other"]
        gender = st.selectbox(question, answers)

        question = "Please the perceived race of the person?" + (" "*st.session_state["counter"])
        answers = ["", "African-American", "White", "Hispanic", "Asian", "Other/Prefer not to say"]
        race = st.selectbox(question, answers)

        question = "Please enter the perceived age of the person in the picture?" + (" "*st.session_state["counter"])
        answer = ["", "18-25", "26-30", "31-35", "36-40", "41-60", "60+"]
        age = st.selectbox(question, answer)
        
        options = ["Very Low", "Low", "Moderate", "High", "Very High"]
        attractive = st.select_slider("Please rate how attractive you think the person is?" + (" "*st.session_state["counter"]), options)
        intelligent = st.select_slider("Please rate how intelligent you think the person is?" + (" "*st.session_state["counter"]), options)
        trustworthy = st.select_slider("Please rate how trustworthy you think the person is?" + (" "*st.session_state["counter"]), options)
        credible = st.select_slider("Please rate how credible you think the person is?" + (" "*st.session_state["counter"]), options)
        confident = st.select_slider("Please rate how confident you think the person is?" + (" "*st.session_state["counter"]), options)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            if gender == "":
                st.error("Please select a valid gender")
            elif race == "":
                st.error("Please select a valid race")
            elif age == "":
                st.error("Please select a valid age")
            else:
                st.session_state["saved_data"].append([st.session_state["current image"], gender, race, age, attractive, intelligent, trustworthy, credible, confident])
                logic()
                st.experimental_rerun()
        

def extra_notes():
    st.title("Extra notes")
    with st.form("extra_notes_form"):
        st.write("Please enter (if any) extra notes/observations about the image that you would like to share with us.")
        notes = st.text_area("Notes")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state['saved_data'].append(["extra", notes])
            st.session_state["page"] = "background"
            st.experimental_rerun()

def background(): 
    with st.form("background_form"):
        st.title("Your Background Information")
        st.write("Please enter your background information. " +
                 "Any information you aren't comfortable sharing, please select the option 'Prefer not to say'.")
        question = "Please choose your gender."
        answer = ["", "Male", "Female", "Other", "Prefer not to say"]
        gender = st.selectbox(question, answer)

        question = "What is your age group?"
        answer = ["", "18-25", "26-40", "40-60", "60+", "Prefer not to say"]
        age = st.selectbox(question, answer)

        question = "Please specify your ethinicity."
        answer = ["", "Black or African-American", "White", "Hispanic or Latino", "Asian or Pacific Islander", "Native American", "Other", "Prefer not to say"]
        ethinicity = st.selectbox(question, answer)

        question = "What is your annual income?"
        answer = ["", "Less than $15,000", "$15,000 - $34,999", "$35,000 - $49,999", "$50,000 - $74,999", "$75,000 - $99,999", "$100,000 or more", "Prefer not to say"]
        income = st.selectbox(question, answer)

        question = "What is the highest level of education you have completed?"
        answer = ["", "High school graduate", "College degree or equivalent", "Graduate degree or equivalent", "Prefer not to say"]
        education = st.selectbox(question, answer)

        question = "Please select your location (state) of residence."
        answer = ["", "Outside of US", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colarado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", 
                  "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
                  "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
                  "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "Washington DC", "West Virginia", "Wisconsin", "Wyoming", "Prefer not to say"]
        residence = st.selectbox(question, answer)

        question = "Which one better describes your political views – even if neither is exactly right?"
        answer = ["", 'Liberal', 'Moderate', 'Conservative', 'Prefer not to say']
        political = st.selectbox(question, answer)

        submitted = st.form_submit_button("Submit")
        if submitted:
            if gender == "":
                st.error("Please select a valid gender")
            elif age == "":
                st.error("Please select a valid age group")
            elif ethinicity == "":
                st.error("Please select a valid ethinicity")
            elif income == "":
                st.error("Please select a valid income bracket")
            elif education == "":
                st.error("Please select a valid education level")
            elif residence == "":
                st.error("Please select a valid residence")
            elif political == "":
                st.error("Please select a valid political view")
            else:
                st.session_state["page"] = "end"
                st.session_state["saved_data"].append([gender, age, ethinicity, income, education, residence, political])
                current_time = str(datetime.now())
                with open('results/' + current_time + '.pkl', 'wb') as f:
                    pkl.dump(st.session_state["saved_data"], f)
                st.experimental_rerun()


def thank_you():
    st.title("Thank you")
    st.session_state["completion_code"] = str("C15J0ZO0")
    st.write("Your participation is greatly appreciated. Please proceed to the following link to complete the study.")
    st.write("https://app.prolific.co/submissions/complete?cc=C15J0ZO0")

print("Test")

if st.session_state["page"] == "intro":
    intro()
elif st.session_state["page"] == "survey":
    survey()
elif st.session_state["page"] == "extra notes":
    extra_notes()
elif st.session_state["page"] == "background":
    background()
elif st.session_state["page"] == "end":
    thank_you()
else:
    st.write("Error")
