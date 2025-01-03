import streamlit as st

# Simulated transcription data
transcriptions = {
    "Transcription 1": {"word": "house", "ipa": ["/haʊs/", "/haʊʃ/", "/haʊz/"]},
    "Transcription 2": {"word": "dog", "ipa": ["/dɔɡ/", "/dɑɡ/", "/dɔk/"]},
    "Transcription 3": {"word": "cat", "ipa": ["/kæt/", "/kɛt/", "/kɑt/"]},
}

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Details"])

if page == "Dashboard":
    st.title("Dashboard")
    st.write("Here are your transcriptions:")

    for transcription in transcriptions:
        if st.button(f"View {transcription}"):
            st.session_state["selected_transcription"] = transcription
            st.experimental_rerun()

elif page == "Details":
    if "selected_transcription" not in st.session_state:
        st.warning("Please select a transcription from the Dashboard.")
        st.stop()

    transcription_name = st.session_state["selected_transcription"]
    details = transcriptions[transcription_name]

    st.title(f"Details for {transcription_name}")
    st.write(f"Word: {details['word']}")
    st.write("IPA Options:")
    for ipa in details["ipa"]:
        st.write(f"- {ipa}")
