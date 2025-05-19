# -*- coding: utf-8 -*-
import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def show_animation():
    animation = load_lottie("app/assets/piggy.json")
    st_lottie(animation, speed=1, width=500, height=400)
