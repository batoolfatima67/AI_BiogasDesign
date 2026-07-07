"""
===========================================================
BioDesignAI
AI-Powered Biogas Plant Design & Decision Support System

Developer : Batool Fatima
Version   : 1.0
===========================================================
"""

import streamlit as st

# -------------------------------------------------
# UI
# -------------------------------------------------

from ui.theme import initialize_theme
from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.footer import render_footer

# -------------------------------------------------
# Existing Pages ONLY
# -------------------------------------------------

import pages.home as home
import pages.plant_design as plant_design
import pages.calculations as calculations
import pages.about as about

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="BioDesignAI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Session State
# -------------------------------------------------

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# -------------------------------------------------
# Initialize Theme
# -------------------------------------------------

initialize_theme()
load_css()

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

render_sidebar()

# -------------------------------------------------
# Header
# -------------------------------------------------

render_header()

# -------------------------------------------------
# Navigation
# -------------------------------------------------

PAGES = {
    "Home": home.show,
    "Plant Design": plant_design.show,
    "Engineering Calculations": calculations.show,
    "About": about.show,
}

selected_page = st.session_state.current_page

if selected_page in PAGES:
    PAGES[selected_page]()
else:
    st.error(f"Page '{selected_page}' does not exist.")

# -------------------------------------------------
# Footer
# -------------------------------------------------

render_footer()
