"""
=========================================================
BioDesignAI
Plant Design Page
=========================================================
"""

import streamlit as st


def show():

    st.title("📐 Biogas Plant Design")

    st.caption(
        "Provide the engineering design parameters for the biogas plant."
    )

    st.divider()

    # =========================================================
    # PROJECT INFORMATION
    # =========================================================

    st.subheader("📁 Project Information")

    col1, col2 = st.columns(2)

    with col1:

        project_name = st.text_input(
            "Project Name",
            value=st.session_state.project["inputs"].get(
                "project_name",
                "My Biogas Plant",
            ),
        )

    with col2:

        location = st.text_input(
            "Project Location",
            value=st.session_state.project["inputs"].get(
                "location",
                "Pakistan",
            ),
        )

    # =========================================================
    # FEEDSTOCK INFORMATION
    # =========================================================

    st.divider()

    st.subheader("🐄 Feedstock Information")

    c1, c2, c3 = st.columns(3)

    with c1:

        waste_type = st.selectbox(
            "Waste Type",
            [
                "Cattle Dung",
                "Buffalo Dung",
                "Horse Manure",
                "Goat Manure",
                "Sheep Manure",
                "Pig Manure",
                "Poultry Litter",
            ],
        )

    with c2:

        animals = st.number_input(
            "Number of Animals",
            min_value=1,
            value=10,
            step=1,
        )

    with c3:

        dung = st.number_input(
            "Dung per Animal (kg/day)",
            min_value=1.0,
            value=25.0,
            step=1.0,
        )

    # =========================================================
    # HOUSEHOLD
    # =========================================================

    st.divider()

    st.subheader("👨‍👩‍👧 Household Information")

    c1, c2 = st.columns(2)

    with c1:

        family = st.number_input(
            "Family Members",
            min_value=1,
            value=5,
        )

    with c2:

        gas = st.number_input(
            "Gas Requirement per Person (m³/day)",
            min_value=0.1,
            value=0.25,
            step=0.05,
        )

    # =========================================================
    # DIGESTER PARAMETERS
    # =========================================================

    st.divider()

    st.subheader("🧪 Digester Parameters")

    c1, c2 = st.columns(2)

    with c1:

        hrt = st.slider(
            "Hydraulic Retention Time (Days)",
            10,
            60,
            20,
        )

    with c2:

        digester_type = st.selectbox(
            "Digester Type",
            [
                "Fixed Dome",
            ],
        )

    # =========================================================
    # ENVIRONMENT
    # =========================================================

    st.divider()

    st.subheader("🌍 Environmental Conditions")

    c1, c2 = st.columns(2)

    with c1:

        temperature = st.slider(
            "Average Temperature (°C)",
            0,
            45,
            25,
        )

    with c2:

        climate = st.selectbox(
            "Climate Zone",
            [
                "Tropical",
                "Sub-Tropical",
                "Temperate",
                "Cold",
            ],
        )

    # =========================================================
    # ENGINEERING ASSUMPTIONS
    # =========================================================

    st.divider()

    st.subheader("⚙ Engineering Assumptions")

    dilution = st.selectbox(
        "Dung : Water Mixing Ratio",
        [
            "1 : 1",
        ],
    )

    methane = st.slider(
        "Expected Methane Content (%)",
        45,
        75,
        60,
    )

    # =========================================================
    # SUMMARY
    # =========================================================

    st.divider()

    st.subheader("📋 Design Summary")

    left, right = st.columns(2)

    with left:

        st.write(f"**Project:** {project_name}")
        st.write(f"**Location:** {location}")
        st.write(f"**Waste:** {waste_type}")
        st.write(f"**Animals:** {animals}")

    with right:

        st.write(f"**Family Members:** {family}")
        st.write(f"**Temperature:** {temperature} °C")
        st.write(f"**HRT:** {hrt} Days")
        st.write(f"**Climate:** {climate}")

    # =========================================================
    # SAVE INPUTS
    # =========================================================

    st.session_state.project["inputs"] = {

        "project_name": project_name,
        "location": location,
        "waste_type": waste_type,
        "animals": animals,
        "dung": dung,
        "family": family,
        "gas": gas,
        "hrt": hrt,
        "temperature": temperature,
        "climate": climate,
        "digester_type": digester_type,
        "dilution": dilution,
        "methane": methane,

    }

    st.divider()

    if st.button(
        "🚀 Start Engineering Design",
        use_container_width=True,
        type="primary",
    ):

        st.session_state.current_page = "Engineering Calculations"
        st.rerun()
