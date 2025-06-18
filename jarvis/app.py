
import streamlit as st
from utils.jarvis_core import process_command
from utils.tts import speak_text
from utils.memory import add_to_memory, get_memory

st.set_page_config(page_title="Jarvis Assistant", page_icon="🤖")
# try:
#     st.image("assets/header.png", use_container_width=True)
# except Exception as e:
#     st.warning(f"Could not load header image: {e}")

st.sidebar.title("🔑 API Keys")
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
news_key = st.sidebar.text_input("News API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("Built by **Sonu Kumar Sharma** 🤖")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/sonu-kumar-sharma)")
st.sidebar.markdown("[GitHub](https://github.com/Golu1464)")

st.title("Jarvis - AI Virtual Assistant")

with st.expander("🔊 Show previous memory"):
    for msg in get_memory():
        st.markdown(f"- {msg}")

command = st.text_input("🔍 Enter a command or message:")
voice = st.checkbox("🎧 Enable voice reply")

if st.button("Send"):
    if not openai_key:
        st.warning("Please enter your OpenAI API Key in sidebar.")
    elif not command:
        st.warning("Type a command!")
    else:
        reply, extra = process_command(command, openai_key, news_key)
        add_to_memory(f"You: {command}")
        add_to_memory(f"Jarvis: {reply}")
        st.markdown(f"**Jarvis:** {reply}")

        if voice:
            speak_text(reply)

        if isinstance(extra, str) and extra.startswith("http"):
            st.markdown(f"[🔗 Click to open]({extra})")
        elif isinstance(extra, list):
            st.write("📰 Headlines:")
            for idx, t in enumerate(extra, 1):
                st.write(f"{idx}. {t}")
