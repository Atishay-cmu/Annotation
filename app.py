import streamlit as st
from PIL import Image
from random import choice, seed, randint, shuffle
import pandas as pd
import os

# Define the pages
def home():
    st.write("This is the home page")

def about():
    st.write("This is the about page")

# Set the query parameter based on the user's selection
if st.button("Go to Home Page"):
    st.experimental_set_query_params(page="home")
elif st.button("Go to About Page"):
    st.experimental_set_query_params(page="about")

# Get the current page from the query parameter
query_params = st.experimental_get_query_params()
page = query_params.get("page", "home")

# Display the appropriate page based on the current page
if page == "home":
    home()
elif page == "about":
    about()


# if "start" not in st.session_state:
    image = []
    for i in range(4):
        img_path = choice(["b-f", "b-m", "w-f", "w-m"])
        img_name = choice(os.listdir(img_path)[1:])
        image.append(os.path.join(img_path, img_name))
    shuffle(image)
    st.session_state["image"] = image
    st.session_state["page"] = "intro"

# def intro():
    st.title("Welcome to the survey!")
    st.write("In this survey, you will be shown a number of images. You would then be asked to answer a series of questions, " +
            "which you are supposed to answer based solely on the image. Some of these may be subjective, but we would like you to answer them as best as you can. " + 
            "All questions are mandatory and you will not be able to complete the survey until you have answered all of them. Thank you for your time and participation.")
    st.write("Please note that you may be shown the same image multiple times, in that case, please try to answer the questions as closely as possible.")
    st.write("Thank you for your time and participation.")
    st.write("Please click on the button below to start the survey.")
    if st.button("Start"):
        st.session_state["page"] = "survey"

# def survey():
#     st.title("Image annotation survey")

# if st.session_state["page"] == "intro":
#     intro()

# elif st.session_state["page"] == "survey":
#     survey()

# if "seed" not in st.session_state:
#     st.session_state["seed"] = randint(0, 1000)

# if "type" not in st.session_state:
#     st.session_state["type"] = 1
#     st.session_state["gender"] = ""
#     st.session_state["age"] = 0
#     st.session_state["education"] = ""
#     st.session_state["race"] = ""

# if "redo" not in st.session_state:
#     st.session_state["redo"] = 0

# if "counter" not in st.session_state:
#     st.session_state["counter"] = 0

# if st.session_state["type"] == 0:
#     st.title("Background information")
#     st.write("Please provide the following information about yourself. This information will be used for research purposes only and will not be shared with anyone else.")
#     question = "What gender do you identify as?"
#     answers = ["Male", "Female", "Other/Prefer not to say"]
#     st.session_state["gender"] = st.selectbox(question, answers)

#     question = "What race do you identify as?"
#     answers = ["African-American", "White", "Hispanic", "Asian", "Other/Prefer not to say"]
#     st.session_state["race"] = st.selectbox(question, answers)

#     st.session_state["age"] = st.number_input("What is your age?", step=1, min_value=18, max_value=80)
#     question = "What is your highest level of education?"
#     answers = ["High School", "Some College", "Bachelor's Degree", "Master's Degree", "Doctoral Degree", "Other/Prefer not to say"]
#     st.session_state["education"] = st.selectbox(question, answers)

#     if st.button("Submit"):
#         st._rerun()

# else:
#     seed_val = st.session_state["seed"]
#     seed(seed_val) # prolific ID
#     img_path = choice(["b-f", "b-m", "w-f", "w-m"])
#     img_name = choice(os.listdir(img_path)[1:])
    image = Image.open(os.path.join(img_path, img_name))

#     st.title('Founder image annotation survey')
#     st.write("In this survey, you will be shown a number of images of founder’s of various start-up companies. You would be asked to answer a series of questions, " + 
#             "which you are supposed to answer based solely on the founder image. Some of these may be subjective, but we would like you to answer them as best as you can. " +
#             " All questions are mandatory and you will not be able to complete the survey until you have answered all of them. Thank you for your time and participation.")

#     col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image(image, caption="Founder Image", use_column_width=False)

    with col3:
        st.write(' ')


#     question = "What is the perceived gender of the founder?"
#     answers = ["Male", "Female", "Other/Prefer not to say"]
#     gender = st.selectbox(question, answers)

    # question = "What is the perceived race of the founder?"
    # answers = ["African-American", "White", "Hispanic", "Asian", "Other/Prefer not to say"]
    # race = st.selectbox(question, answers)

    # age = st.number_input("What is the perceived age of the founder?", step=1, min_value=10, max_value=80)

#     # Creating a list of options for the Likert scale
#     options = ["Very Low", "Low", "Moderate", "High", "Very High"]

#     # Creating the Likert scale using the select_slider() function
#     attractive = st.select_slider("Please rate the founder’s attractiveness:", options)
#     confident = st.select_slider("Please rate how confident the founder appears:", options)
#     credible = st.select_slider("Please rate how credible the founder appears:", options)
#     attention_check1 = st.select_slider("Please select rating equivalent to neutral for the question:", options)
#     attention_check1 = st.select_slider("Please select rating one above what you selected in the previous question:", options)

#     question = "Does the founder image appear to be augmented? (Eg: Are there any obvious photoshop artifacts or filter use?)"
#     answers = ["Yes", "No", "Not sure"]
#     augmented = st.selectbox(question, answers)

#     if "refresh" in st.session_state and st.session_state["refresh"] == 1:
#         st.session_state["refresh"] = 0
#         st.write("Please answer the following questions again for the new image.")

#     if st.button("Submit"):
#         st.session_state["counter"] += 1
#         if st.session_state["counter"] >= 4:
#             if st.session_state["counter"] == 4:
#                 answer = [st.session_state["gender"], st.session_state["age"], st.session_state["education"], 
#                     st.session_state["age"], img_path + "/" + img_name, gender, race, age, 
#                     attractive, confident, credible, augmented]
#                 pd.DataFrame([answer]).to_csv("answers.csv", mode="a", header=False, index=False)
#             st.write("Thank you for your participation. You may now close this window.")
#             st.session_state["type"] = 0
#             st._rerun()
#         else:
#             answer = [st.session_state["gender"], st.session_state["age"], st.session_state["education"], 
#                   st.session_state["age"], img_path + "/" + img_name, gender, race, age, 
#                   attractive, confident, credible, augmented]
#             pd.DataFrame([answer]).to_csv("answers.csv", mode="a", header=False, index=False)
#             st.session_state["seed"] += randint(2, 1000)
#             st.session_state["redo"] = 1
#             st.session_state["refresh"] = 1
#             st._rerun()
        

    