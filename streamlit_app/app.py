import streamlit as st
from indexing import process_user_query

st.title("Restaurant & Menu Chatbot")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

def display_conversation():
    for message in st.session_state.conversation_history:
        if message['sender'] == 'user':
            st.markdown(f"**User:** {message['text']}")
        elif message['sender'] == 'bot':
            st.markdown(f"**Bot:** {message['text']}")

query = st.text_input("Ask about restaurants and menus:")

display_conversation()

if query:
    st.session_state.conversation_history.append({'sender': 'user', 'text': query})
    response = process_user_query(query)
    st.session_state.conversation_history.append({'sender': 'bot', 'text': response})
    display_conversation()
    st.markdown("<hr>", unsafe_allow_html=True)
