from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

client = st.secrets['OPENAI_API_KEY']

def analyze_expense_with_gpt(prompt):
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a money-saving buddy that talks like a Nigerian friend."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content
