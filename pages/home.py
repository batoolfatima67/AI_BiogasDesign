"""
=========================================================
BioDesignAI Home Page

Author : Batool Fatima
Version : 1.0
=========================================================
"""

from pathlib import Path

import streamlit as st

from ui.hero import render_hero
from ui.cards import metric_card


def show():

    # ==================================================
    # Hero Section
    # ==================================================

    render_hero()

    st.write("")

    # ==================================================
    # Quick Actions
    # ==================================================

    st.subheader("🚀 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "📐 Start New Design",
            use_container_width=True,
        ):
            st.session_state.current_page = "Plant Design"
            st.rerun()

    with col2:
        if st.button(
            "📊 Open Dashboard",
            use_container_width=True,
        ):
            st.session_state.current_page = "Dashboard"
            st.rerun()

    with col3:
        if st.button(
            "📄 Generate Report",
            use_container_width=True,
        ):
            st.session_state.current_page = "Reports"
            st.rerun()

    st.write("")

    # ==================================================
    # Dashboard Cards
    # ==================================================

    st.subheader("📈 System Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Engineering Modules",
            "10",
            icon="📐",
        )

    with c2:
        metric_card(
            "Supported Waste Types",
            "15",
            icon="♻️",
        )

    with c3:
        metric_card(
            "Design Accuracy",
            "95%",
            icon="🎯",
        )

    with c4:
        metric_card(
            "Version",
            "1.0",
            icon="🚀",
        )

    st.write("")

    # ==================================================
    # Why BioDesignAI
    # ==================================================

    left, right = st.columns([2, 1])

    with left:

        st.subheader("🌍 Why BioDesignAI?")

        st.markdown(
            """
BioDesignAI is an AI-powered engineering software platform for designing
fixed-dome biogas plants.

### Key Objectives

- Automated engineering calculations
- Accurate plant sizing
- Engineering drawings
- Material estimation
- Cost estimation
- Interactive visualization
- Professional PDF reports
- Future AI-powered recommendations
"""
        )

    with right:

        BASE_DIR = Path(__file__).resolve().parent.parent
        banner_path = BASE_DIR / "assets" / "hero_banner.png"

        if banner_path.exists():

            try:

                st.image(
                    str(banner_path),
                    use_container_width=True,
                )

            except Exception:

                st.warning("⚠️ Hero banner exists but cannot be opened.")

        else:

            st.info(
                "🖼️ Hero Banner\n\n"
                "Add 'hero_banner.png' inside the assets folder."
            )

    st.divider()

    # ==================================================
    # Workflow
    # ==================================================

    st.subheader("⚙️ Engineering Workflow")

    st.info(
        """
① Enter Design Parameters

⬇

② Perform Engineering Calculations

⬇

③ Generate Plant Dimensions

⬇

④ Create Engineering Drawings

⬇

⑤ Estimate Materials & Cost

⬇

⑥ Generate Final Engineering Report
"""
    )

    st.divider()

    # ==================================================
    # Version 1 Features
    # ==================================================

    st.subheader("✨ Version 1 Features")

    f1, f2 = st.columns(2)

    with f1:

        st.success("✔ Fixed Dome Plant Design")

        st.success("✔ Numerical Engineering Calculations")

        st.success("✔ Dashboard Analytics")

        st.success("✔ Material Estimation")

    with f2:

        st.success("✔ Cost Estimation")

        st.success("✔ Engineering Drawings")

        st.success("✔ 3D Visualization")

        st.success("✔ PDF Reports")

    st.divider()

    # ==================================================
    # Project Progress
    # ==================================================

    st.subheader("📊 Development Progress")

    st.progress(20)

    st.caption("Version 1 is currently under active development.")
