import streamlit as st

def show_dashboard_card(title, content):
    st.markdown(f"""
    <div style='border:1px solid #CCC; padding:15px; border-radius:10px; margin-bottom:10px;'>
        <h4>{title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)
