
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Streamlit app
st.title("Personality Predictor")

# Create a form
with st.form("personality_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    hobbies = st.text_area("Hobbies (comma-separated)")
    movie_types = st.multiselect(
        "Types of movies you like",
        ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Documentary"]
    )
    superpower = st.selectbox(
        "If you could have any superpower, which one would you choose?",
        ["Flying", "Invisibility", "Super Strength", "Telepathy"]
    )
    activity = st.selectbox(
        "What is your preferred weekend activity?",
        ["Reading", "Hiking", "Watching Movies", "Socializing", "Other"]
    )
    food = st.multiselect(
        "Which Indian foods do you enjoy? (Select all that apply)",
        ["Samosa", "Ice Cream", "Chaat", "Pani Puri", "Bhel Puri"]
    )
    color = st.selectbox(
        "Choose your favorite color from the options below:",
        ["❤", "💙", "💚", "💛", "🖤", "🤍", "💜", "🧡"]
    )
    favorite_books = st.multiselect(
        "Which genres of books do you enjoy?",
        ["Fiction", "Non-Fiction", "Mystery", "Fantasy", "Science Fiction", "Biography", "History"]
    )
    travel_interests = st.multiselect(
        "What types of destinations do you prefer to travel to?",
        ["Beaches", "Mountains", "Cities", "Countryside", "Historical Sites", "Adventure Spots"]
    )
    pet_choice = st.selectbox(
        "Do you prefer cats, dogs, or other pets?",
        ["Cats", "Dogs", "no pets"]
    )
    submitted = st.form_submit_button("Submit")

# Process the form submission
if submitted:
    # Generate a prompt for the LLM
    prompt = f"""
    Analyze the following user information and predict their personality, type of person they are, future interests, and growth direction:
    
    Name: {name}
    Age: {age}
    Sex: {sex}
    Hobbies: {hobbies}
    Preferred Movie Types: {movie_types}
    Superpower Choice: {superpower}
    Weekend Activity: {activity}
    Favorite Indian Foods: {food}
    Favorite Color: {color}
    Favorite Book Genres: {favorite_books}
    Travel Interests: {travel_interests}
    Pet Preference: {pet_choice}
    
    Please format the response in markdown and be direct to the point.
    """
    response = model.invoke(prompt)
    st.markdown(response.content)
