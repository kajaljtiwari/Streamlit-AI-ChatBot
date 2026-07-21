import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -------------------- Load API Key --------------------
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- Custom CSS --------------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:1rem;
}

div[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:12px;
    margin-bottom:12px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Chat History --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Sidebar --------------------
with st.sidebar:

    st.title("🤖 AI ChatBot")
    st.caption("Powered by Groq AI")

    st.divider()

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("📌 About")
    st.info(
        """
This AI ChatBot answers your
questions using the Groq API
and Llama 3.3 70B model.
"""
    )

    st.subheader("💡 Example Prompts")

    st.markdown("""
- Explain Python OOP
- Write a Resume Summary
- Difference between AI & ML
- Create SQL Query
- Write Python Program
""")

    st.divider()

    st.subheader("🛠 Tech Stack")

    st.success("""
🐍 Python

⚡ Streamlit

🧠 Groq API

🤖 Llama 3.3 70B
""")

    st.divider()

    st.caption("App Version 1.0")

# -------------------- Main Page --------------------
st.title("🤖 AI ChatBot")

st.markdown("""
### Your Intelligent AI Assistant

Ask programming, technology,
career, or general questions.
""")

# Welcome Message
if len(st.session_state.messages) == 0:
    st.info("👋 Welcome! Start chatting with your AI assistant.")

# -------------------- Display Messages --------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- Chat Input --------------------
prompt = st.chat_input("💬 Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        with st.spinner("⚡ Generating response..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        st.error(f"❌ {e}")

# -------------------- Footer --------------------
st.divider()

st.markdown("""
<div style="text-align:center;color:gray;">
Powered by <b>Groq AI</b> • Built with <b>Streamlit</b>
</div>
""", unsafe_allow_html=True)