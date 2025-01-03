import streamlit as st

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
    
    # Loop through words and display IPA options
    for word_data in words:
        st.markdown(f"### {word_data['word'].capitalize()}")
        
        # Create a horizontal layout for IPA transcriptions
        selected_ipa = st.radio(
            "Select the correct IPA transcription:",
            word_data["ipa"],
            horizontal=True,
            key=word_data["word"]
        )
        
        st.write(f"You selected: {selected_ipa}")
