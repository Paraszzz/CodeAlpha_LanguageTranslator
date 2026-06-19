import streamlit as st
from deep_translator import GoogleTranslator

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
}

# Page setup
st.set_page_config(page_title="TalkTranslate", page_icon="🌐")

st.title("🌐 TalkTranslate")
st.caption("Translate text instantly, in any language")

# Text input
text_to_translate = st.text_area("Enter text to translate:", height=120)

# Language selectors, side by side
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("From", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("To", list(LANGUAGES.keys()), index=1)

# Translate button
if st.button("Translate →"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text first.")
    else:
        source_code = LANGUAGES[source_lang]
        target_code = LANGUAGES[target_lang]
        translated = GoogleTranslator(source=source_code, target=target_code).translate(text_to_translate)

        st.subheader("Translation")
        st.success(translated)