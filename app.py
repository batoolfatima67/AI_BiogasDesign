"""
===========================================================
BioDesignAI
AI-Powered Biogas Plant Design & Decision Support System

Developer : Batool Fatima
Version   : 1.0
===========================================================
"""

import streamlit as st

# ----------------------------
# UI Components
# ----------------------------
from ui.theme import initialize_theme
from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.footer import render_footer

# ----------------------------
# Pages
# ----------------------------
import pages.home as home
import pages.plant_design as plant_design
import pages.calculations as calculations
import pages.dashboard as dashboard
import pages.drawing as drawing
import pages.visualization as visualization
import pages.materials as materials
import pages.cost as cost
import pages.report as report
import pages.about as about


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="BioDesignAI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# SESSION STATE
# =========================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "project" not in st.session_state:

    st.session_state.project = {

        "inputs": {},

        "results": {},

        "materials": {},

        "cost": {},

        "drawing": {},

        "report": {}

    }


# =========================================================
# INITIALIZATION
# =========================================================

initialize_theme()

load_css()

# =========================================================
# SIDEBAR
# =========================================================

render_sidebar()

selected_page = st.session_state.current_page

# =========================================================
# HEADER
# =========================================================

render_header()

# =========================================================
# PAGE ROUTER
# =========================================================

PAGES = {

    "Home": home.show,

    "Plant Design": plant_design.show,

    "Engineering Calculations": calculations.show,

    "Dashboard": dashboard.show,

    "Engineering Drawing": drawing.show,

    "3D Visualization": visualization.show,

    "Materials": materials.show,

    "Cost Estimation": cost.show,

    "Reports": report.show,

    "About": about.show,

}

try:

    page_function = PAGES.get(selected_page)

    if page_function:

        page_function()

    else:

        st.error("Requested page not found.")

except Exception as e:

    st.error("An unexpected error occurred.")

    with st.expander("Technical Details"):

        st.exception(e)

# =========================================================
# FOOTER
# =========================================================

render_footer()
