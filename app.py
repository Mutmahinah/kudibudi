# -*- coding: utf-8 -*-
import streamlit as st
from app.pages import dashboard  # Ensures the dashboard is loaded

def main():
    st.switch_page("app/pages/dashboard.py")

if __name__ == "__main__":
    main()
