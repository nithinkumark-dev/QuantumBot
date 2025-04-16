import streamlit as st
import time
from utils import *
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


# === Generate Response ===
def generate_response(query):
    llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', google_api_key=api_key)
    create_vector_store()
    combined_docs = get_similar_docs(query)

    prompt_template = """
    You are a helpful assistant in a time-bending, quantum adventure. Answer questions based on the following documents about "The Quantum Paradox" universe.

    Documents:
    {combined_documents}

    Question:
    {query}
    """
    prompt_template_ = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt_template_.invoke({"combined_documents": combined_docs, "query": query})
    response = llm.invoke(prompt)
    return response.content


# === Page Config ===
st.set_page_config(page_title="Quantum Paradox Chatbot", page_icon="⚛️", layout="wide")

# === Custom CSS for a futuristic UI ===
st.markdown("""
    <style>
    .stChatMessage.user { background-color: #F0F2F6; border-radius: 12px; padding: 10px; margin-bottom: 10px; }
    .stChatMessage.assistant { background-color: #e5e5e5; border-radius: 12px; padding: 10px; margin-bottom: 10px; }
    .main { background: linear-gradient(to right, #1a2a6c, #b21f1f, #fdbb2d); color: white; }
    .block-container { padding: 2rem 3rem; }
    .st-bp { background: rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 1rem; }
    .css-1kyxreq, .css-1v3fvcr { color: white; }
    .chat-container { padding: 20px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# === Sidebar Branding ===
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1998/1998708.png",
        width=100)
    st.title("Quantum Paradox Chatbot 💡")
    st.markdown("Explore the world of time loops, quantum physics, and reality bending.")
    st.markdown("---")
    st.caption("Powered by Gemini + LangChain")

# === Header ===
st.markdown("<h2 style='color: white;'>The Quantum Paradox: A Journey Beyond Time 🤖</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='color: white; font-size: 16px;'>Ask questions about the quantum world and Dr. Elara Nova’s daring adventures!</p>",
    unsafe_allow_html=True)

# === Chat History ===
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant",
                                  "content": "👋 Welcome to The Quantum Paradox Chatbot! Ask me anything about the quantum universe."}]

# === Display chat messages ===
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# === Input Field ===
if user_query := st.chat_input("Type your quantum question here..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.spinner("Processing quantum information..."):
        response = generate_response(user_query)

        # Typing animation
        with st.chat_message("assistant"):
            msg_placeholder = st.empty()
            full_response = ""
            for word in response.split():
                full_response += word + " "
                msg_placeholder.markdown(full_response + "▌")
                time.sleep(0.03)
            msg_placeholder.markdown(full_response.strip())

        st.session_state.messages.append({"role": "assistant", "content": full_response.strip()})
        st.balloons()
