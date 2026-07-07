"""
=========================================================
Application Header
=========================================================
"""

import streamlit as st


def render_header():

    left, right = st.columns([1, 6])

    with left:

        st.image(
            "assets/logo.png",
            width=80
        )

    with right:

        st.markdown(
            """
<div class="main-title">
BioDesignAI
</div>

<div class="sub-title">
AI-Powered Biogas Plant Design & Decision Support System
</div>
""",
            unsafe_allow_html=True,
        )

    st.divider()
