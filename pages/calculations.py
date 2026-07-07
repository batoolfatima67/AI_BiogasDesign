"""
=========================================================
BioDesignAI
Engineering Calculations Page

Author : Batool Fatima
Version : 1.0
=========================================================
"""

import streamlit as st


def show():

    st.title("🧮 Engineering Calculations")

    st.info(
        "This page is currently under development.\n\n"
        "In Version 1 it will display all engineering calculations "
        "for gas production, slurry volume, digester sizing, dome design, "
        "inlet and outlet chamber dimensions."
    )

    st.markdown("---")

    st.subheader("Upcoming Features")

    st.checkbox("Gas Production", disabled=True)

    st.checkbox("Slurry Calculations", disabled=True)

    st.checkbox("Digester Design", disabled=True)

    st.checkbox("Dome Design", disabled=True)

    st.checkbox("Inlet Design", disabled=True)

    st.checkbox("Outlet Design", disabled=True)

    st.checkbox("Material Estimation", disabled=True)

    st.checkbox("Cost Estimation", disabled=True)
