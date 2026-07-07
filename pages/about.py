"""
=========================================================
BioDesignAI
About Page

Author : Batool Fatima
Version : 1.0
=========================================================
"""

import streamlit as st


def show():
    """
    Display the About page.
    """

    st.title("ℹ️ About BioDesignAI")

    st.markdown(
        """
## BioDesignAI

BioDesignAI is an AI-powered Engineering Design and Decision Support System
for biogas plants.

### Version
1.0

### Developer
Batool Fatima

### Features

- Engineering Calculations
- Digester Design
- Dome Design
- Material Estimation
- Cost Estimation
- Engineering Drawings
- PDF Reports
- AI Recommendations

---
Future versions will include interactive 3D visualization,
optimization, and AI-assisted design.
"""
    )
