import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from helper import PositionalEncoding, MultiHeadAttentionLayer, create_padding_mask, create_look_ahead_mask, predict

# Load your trained model
model = load_model('./models/v2/model.h5', custom_objects={
        "PositionalEncoding": PositionalEncoding,
        "MultiHeadAttentionLayer": MultiHeadAttentionLayer,
    })

if "ti" not in st.session_state:
    st.session_state["ti"] = ""

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = ""

def generate_response(text, model):
    prediction = predict(text, model)
    return prediction

# Streamlit UI
st.title("Chatbot with Streamlit and Keras Model")
st.write("Ask anything!")

st.markdown(
    """
    <style>
    .scrollable-box {
        height: 300px;
        overflow-y: auto;
        background-color: #f4f4f4;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-family: monospace;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the conversation history in a scrollable box
st.markdown(
    f"<div class='scrollable-box'>{st.session_state['conversation_history']}</div>",
    unsafe_allow_html=True,
)

def submit():
    user_input = st.session_state["ti"]
    print(user_input)
    if user_input:
        response = generate_response(user_input, model)
        st.session_state["conversation_history"] += f"User: {user_input}<br><br>Bot: {response}<br><br>"
        st.session_state["ti"] = ""
    else:
        st.write("Please type a message.")

st.text_input("You: ", key="ti", on_change=submit)
