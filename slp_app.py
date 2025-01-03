# ipa_app.py
import streamlit as st

# -----------------------------------------------------------------
# 1) Sample data (Fake Data)
# -----------------------------------------------------------------
# A dictionary mapping "challenge word" -> list of possible IPA transcriptions
SAMPLE_WORDS_DATA = {
    "cat": ["/kæt/", "/kʌt/", "/kɑt/"],
    "dog": ["/dɔg/", "/dɒg/", "/dɑg/"],
    "bird": ["/bɜrd/", "/bɚd/", "/bɪrd/"],
    "paper": ["/peɪpɚ/", "/pæpə/", "/peɪpər/"],
    "phone": ["/foʊn/", "/fəʊn/", "/foːn/"]
}

# -----------------------------------------------------------------
# 2) Define helper functions
# -----------------------------------------------------------------
def transcription_page():
    """
    Page where the user can upload an audio file (as a prototype)
    and select IPA transcriptions for a list of challenge words.
    """
    st.title("IPA Transcription Page")

    # File uploader (prototype)
    st.subheader("Upload Client Audio (Prototype)")
    uploaded_audio = st.file_uploader(
        "Upload the client's audio recording (e.g., .wav, .mp3, .ogg)",
        type=["wav", "mp3", "ogg"]
    )
    
    if uploaded_audio:
        st.write("**File uploaded:**", uploaded_audio.name)
        # In a real app, you would process the audio here or store it.

    st.write("---")
    st.subheader("Select IPA Transcriptions")
    st.write("Below is a list of challenge words and possible IPA versions.")

    # For each challenge word in the sample data, we allow user to pick one IPA
    # from the possible options.
    user_choices = {}
    for word, ipa_list in SAMPLE_WORDS_DATA.items():
        st.markdown(f"**Challenge Word:** {word}")
        choice = st.radio(
            f"Select IPA for '{word}'",
            ipa_list,
            key=f"radio_{word}"  # ensure unique key
        )
        user_choices[word] = choice
        st.write("---")

    # Option to save or show the user's selections
    if st.button("Submit IPA Selections"):
        st.success("IPA selections submitted.")
        st.write("Your chosen IPA for each challenge word:")
        st.json(user_choices)


def home_page():
    """
    Simple homepage for the application.
    """
    st.title("Welcome to the IPA Transcription Prototype")
    st.write("""
        This prototype helps speech-language pathologists transcribe 
        the words produced by a client. You can navigate to the 
        Transcription page to upload an audio file and select 
        possible IPA transcriptions for each challenge word.
    """)
    st.write("Use the sidebar to navigate between pages.")


def analysis_page():
    """
    Placeholder page for any potential data analysis or 
    summary steps you might implement.
    """
    st.title("Data Analysis (Prototype)")
    st.write("""
        In a more robust application, this page could show:
        - Summary of selected IPA transcriptions
        - Charts or tables comparing correct vs. client pronunciation
        - Progress tracking over multiple sessions
    """)


# -----------------------------------------------------------------
# 3) Main Streamlit App Structure (Multi-Page Navigation)
# -----------------------------------------------------------------

# Set some basic configuration
st.set_page_config(
    page_title="IPA Transcription App",
    layout="wide",
)

# Create a sidebar for page navigation
pages = {
    "Home": home_page,
    "Transcription": transcription_page,
    "Analysis": analysis_page
}

with st.sidebar:
    selected_page = st.radio("Navigate", list(pages.keys()))

# Render the selected page
pages[selected_page]()

