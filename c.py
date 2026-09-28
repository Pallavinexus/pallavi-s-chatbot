import streamlit as st
import ollama
st.set_page_config(
    page_title="My AI Chat",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

    .stApp {
        background-color: #f5f7fb;
    }


    .title {
        text-align: center;
        color: #22223b;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6c757d;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .stTextInput > div > div > input {
        border: 2px solid #6c63ff;
        border-radius: 12px;
        padding: 12px;
        font-size: 16px;
    }

    .stButton > button {
        width: 100%;
        background-color: #6c63ff;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 17px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #5548d9;
        color: white;
    }

    .user-message {
        background-color: #6c63ff;
        color: white;
        padding: 12px 18px;
        border-radius: 15px;
        margin: 10px 0;
        margin-left: 20%;
    }

    .ai-message {
        background-color: white;
        color: #222;
        padding: 12px 18px;
        border-radius: 15px;
        margin: 10px 0;
        margin-right: 20%;
        border: 1px solid #ddd;
    }

    .chat-heading {
        color: #22223b;
        font-size: 24px;
        font-weight: bold;
        margin-top: 25px;
    }

</style>
""", unsafe_allow_html=True)

model = "llama3.2"

if "conversation" not in st.session_state:
    st.session_state.conversation = []

st.markdown(
    '<div class="title">🤖 My AI Chat</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask anything and chat with your local AI</div>',
    unsafe_allow_html=True
)


question = st.text_input(
    "Enter your question:",
    placeholder="Type your question here..."
)

if st.button("🤖 Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    elif question.lower().strip() == "exit":
        st.success("Chat ended.")

    else:

        st.session_state.conversation.append({
            "role": "user",
            "content": question
        })

        response = ollama.chat(
            model=model,
            messages=st.session_state.conversation
        )

        answer = response["message"]["content"]

    
        st.session_state.conversation.append({
            "role": "assistant",
            "content": answer
        })

if st.session_state.conversation:

    st.markdown(
        '<div class="chat-heading">💬 Conversation</div>',
        unsafe_allow_html=True
    )

    for message in st.session_state.conversation:

        if message["role"] == "user":

            st.markdown(
                f"""
                <div class="user-message">
                    <b>You:</b><br>
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="ai-message">
                    <b>🤖 AI:</b><br>
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )