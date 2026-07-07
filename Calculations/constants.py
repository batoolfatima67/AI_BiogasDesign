"""
=========================================================
BioDesignAI
Engineering Design Constants

Author : Batool Fatima
Version: 1.0

All engineering constants used throughout the software
are defined here.

References:
• KVIC Biogas Design Manual
• IS 9478
• FAO Biogas Manuals
=========================================================
"""

# =========================================================
# GAS YIELD
# =========================================================

# Average gas yield from fresh cattle dung
# Unit : m³/kg fresh dung

GAS_YIELD = {
    "Cattle Dung": 0.040,
    "Buffalo Dung": 0.038,
    "Horse Manure": 0.032,
    "Goat Manure": 0.030,
    "Sheep Manure": 0.030,
    "Pig Manure": 0.060,
    "Poultry Litter": 0.070,
}

# =========================================================
# DAILY DUNG PRODUCTION
# =========================================================

# Fresh dung production per animal
# Unit : kg/day

DUNG_PRODUCTION = {

    "Cattle Dung":25,

    "Buffalo Dung":30,

    "Horse Manure":20,

    "Goat Manure":2,

    "Sheep Manure":2,

    "Pig Manure":5,

    "Poultry Litter":0.12

}

# =========================================================
# GAS REQUIREMENT
# =========================================================

# Daily household cooking gas requirement

DEFAULT_GAS_REQUIREMENT = 0.25

# m³/person/day

# =========================================================
# DILUTION RATIO
# =========================================================

DEFAULT_DILUTION_RATIO = 1.0

# 1:1 Dung : Water

# =========================================================
# HYDRAULIC RETENTION TIME
# =========================================================

DEFAULT_HRT = 20

# Days

# =========================================================
# DIGESTER DESIGN
# =========================================================

DEFAULT_FREEBOARD = 0.30

DEFAULT_DOME_FACTOR = 0.25

# Gas storage is usually designed as
# 35–50% of the daily gas production.

DEFAULT_GAS_STORAGE_FACTOR = 0.40

DEFAULT_SLURRY_DENSITY = 1000

# kg/m³

# =========================================================
# METHANE CONTENT
# =========================================================

DEFAULT_METHANE = 60

# %

# =========================================================
# CONSTRUCTION PARAMETERS
# =========================================================

BRICK_THICKNESS = 0.23

PLASTER_THICKNESS = 0.015

CONCRETE_THICKNESS = 0.10

# =========================================================
# SAFETY FACTOR
# =========================================================

DESIGN_SAFETY_FACTOR = 1.10
