import streamlit as st
from app.components.dashboard_cards import show_dashboard_card
from services.gpt_service import analyze_expense_with_gpt
from app.utils.text_utils import translate_to_pidgin
st.markdown("""
    <style>
    .stApp {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #005f3c;
    }
    .css-1d391kg {
        color: #ffaa00;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Kudibuddy Dashboard")

st.title("👋 Welcome to Kudibuddy")
income = st.number_input("Enter your monthly income (₦):", min_value=0)
food = st.number_input("Food expenses:", min_value=0)
transport = st.number_input("Transport expenses:", min_value=0)
others = st.number_input("Other expenses:", min_value=0)

if st.button("Analyze My Spending"):
    total_expense = food + transport + others
    balance = income - total_expense

    show_dashboard_card("Total Expense", f"₦{total_expense}")
    show_dashboard_card("Remaining Balance", f"₦{balance}")

    prompt = f"My income is ₦{income}, and I spent ₦{food} on food, ₦{transport} on transport, and ₦{others} on other things."
    feedback = analyze_expense_with_gpt(prompt)
    pidgin_feedback = translate_to_pidgin(feedback)

    show_dashboard_card("💬 GPT Feedback", pidgin_feedback)
from app.components.animation import show_animation
show_animation()

