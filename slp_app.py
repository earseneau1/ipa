
import streamlit as st
import random

# Define data
words = [
    {"word": "house", "ipa": ["/haʊs/", "/haʊʃ/", "/haʊz/", "/hɑs/", "/hæs/", "/haʊθ/"]},
    {"word": "dog", "ipa": ["/dɔɡ/", "/dɑɡ/", "/dɔk/", "/dɒɡ/", "/dʌɡ/", "/tɔɡ/"]},
    {"word": "cat", "ipa": ["/kæt/", "/kɛt/", "/kɑt/", "/kʌt/", "/kæt̚/", "/gæt/"]},
]

# Streamlit UI
st.title("SLP Transcription Prototype")

# Simulate uploading a recording
st.subheader("Simulate Uploading a Recording")
uploaded_file = st.file_uploader("Choose a recording", type=["mp3", "wav", "m4a"])

if uploaded_file:
    st.success("Recording uploaded successfully!")
    
    # Show transcription results
    st.subheader("Transcription Results")
    for word_data in words:
        st.markdown(f"### {word_data['word'].capitalize()}")
        
        # Generate random AI suggestion
        ai_suggestion = random.choice(word_data["ipa"])
        
        # Create table for IPA options
        for ipa in word_data["ipa"]:
            highlight = " (AI Suggestion)" if ipa == ai_suggestion else ""
            st.radio(f"{ipa}{highlight}", options=["Correct", "Incorrect"])
