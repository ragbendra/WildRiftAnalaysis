import streamlit as st
import pandas as pd
import datetime
import uuid
from PIL import Image
import pytesseract


# Function to generate Match ID
def generate_match_id(player_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"{player_name}_{timestamp}_{unique_id}"

# Function to extract text from image using OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

# Function to save match data to CSV
def save_match_data(data, file_path="wildrift_matches.csv"):
    try:
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
    excePpt FileNotFoundError:
        df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

# Streamlit UI
st.title("Wild Rift Match Tracker")
st.write("Log your matches, extract stats, and generate Match IDs easily.")

# Step 1: Generate Match ID
player_name = st.text_input("Enter Player Name:")
if player_name:
    match_id = generate_match_id(player_name)
    st.write(f"Generated Match ID: `{match_id}`")

# Step 2: Upload Screenshot for OCR
uploaded_file = st.file_uploader("Upload Match Stats Screenshot (optional):", type=["png", "jpg", "jpeg"])
if uploaded_file:
    extracted_text = extract_text_from_image(uploaded_file)
    st.text_area("Extracted Match Stats:", extracted_text, height=200)

# Step 3: Enter Match Details
champion = st.text_input("Champion Played:")
kills = st.number_input("Kills:", min_value=0, step=1)
deaths = st.number_input("Deaths:", min_value=0, step=1)
assists = st.number_input("Assists:", min_value=0, step=1)
win_loss = st.selectbox("Match Outcome:", ["Win", "Loss"])

# Step 4: Save Data
if st.button("Save Match Data"):
    if player_name and champion:
        match_data = [{
            "Match ID": match_id,
            "Player Name": player_name,
            "Champion": champion,
            "Kills": kills,
            "Deaths": deaths,
            "Assists": assists,
            "Win/Loss": win_loss
        }]
        save_match_data(match_data)
        st.success("Match data saved successfully!")
    else:
        st.error("Player Name and Champion are required.")

# Display Saved Matches
st.subheader("Saved Matches")
try:
    saved_data = pd.read_csv("wildrift_matches.csv")
    st.dataframe(saved_data)
except FileNotFoundError:
    st.write("No match data found. Start by logging your first match!")
