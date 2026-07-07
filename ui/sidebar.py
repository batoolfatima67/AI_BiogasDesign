"""
=========================================================
BioDesignAI Sidebar
Version 1.0
=========================================================
"""

import streamlit as st
from ui.theme import toggle_theme


def render_sidebar():
    """
    Render the application sidebar.

    Returns
    -------
    str
        Selected page name.
    """

    with st.sidebar:

        # ---------------------------------------------------
        # Logo
        # ---------------------------------------------------

        st.image("assets/logo.png", width=120)

        st.markdown(
            """
            # 🌱 BioDesignAI
            """
        )

        st.caption("AI-Powered Biogas Plant Design")

        st.divider()

        # ---------------------------------------------------
        # HOME
        # ---------------------------------------------------

        st.markdown("### 🏠 Home")

        if st.button("Dashboard", use_container_width=True):
            st.session_state.current_page = "Home"

        st.divider()

        # ---------------------------------------------------
        # DESIGN
        # ---------------------------------------------------

        st.markdown("### 📐 Design")

        if st.button("Plant Design", use_container_width=True):
            st.session_state.current_page = "Plant Design"

        if st.button("Engineering Calculations", use_container_width=True):
            st.session_state.current_page = "Engineering Calculations"

        st.divider()

        # ---------------------------------------------------
        # VISUALIZATION
        # ---------------------------------------------------

        st.markdown("### 🖼 Visualization")

        if st.button("Engineering Drawing", use_container_width=True):
            st.session_state.current_page = "Engineering Drawing"

        if st.button("3D Visualization", use_container_width=True):
            st.session_state.current_page = "3D Visualization"

        st.divider()

        # ---------------------------------------------------
        # ANALYSIS
        # ---------------------------------------------------

        st.markdown("### 📊 Analysis")

        if st.button("Dashboard Results", use_container_width=True):
            st.session_state.current_page = "Dashboard"

        if st.button("Materials", use_container_width=True):
            st.session_state.current_page = "Materials"

        if st.button("Cost Estimation", use_container_width=True):
            st.session_state.current_page = "Cost Estimation"

        st.divider()

        # ---------------------------------------------------
        # REPORTS
        # ---------------------------------------------------

        st.markdown("### 📄 Reports")

        if st.button("Generate Report", use_container_width=True):
            st.session_state.current_page = "Reports"

        st.divider()

        # ---------------------------------------------------
        # SETTINGS
        # ---------------------------------------------------

        st.markdown("### ⚙ Settings")

        if st.button(
            f"Switch to {'Dark' if st.session_state.theme == 'Light' else 'Light'} Mode",
            use_container_width=True,
        ):
            toggle_theme()
            st.rerun()

        st.divider()

        # ---------------------------------------------------
        # ABOUT
        # ---------------------------------------------------

        if st.button("ℹ About", use_container_width=True):
            st.session_state.current_page = "About"

        st.divider()

        st.caption("BioDesignAI Version 1.0")
        st.caption("Developed by Batool Fatima")

    return st.session_state.current_page
