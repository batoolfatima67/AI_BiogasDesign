"""
=========================================================
BioDesignAI
Slurry Calculations

Author : Batool Fatima
Version : 1.0

This module calculates:

1. Daily water requirement
2. Daily slurry production
3. Daily slurry volume
4. Digester working volume
=========================================================
"""

from calculations.constants import (
    DEFAULT_DILUTION_RATIO,
    DEFAULT_HRT,
    DEFAULT_SLURRY_DENSITY,
)


class SlurryCalculator:
    """
    Slurry preparation and digester sizing.
    """

    def __init__(
        self,
        daily_dung: float,
        dilution_ratio: float = DEFAULT_DILUTION_RATIO,
        hrt: int = DEFAULT_HRT,
        slurry_density: float = DEFAULT_SLURRY_DENSITY,
    ):

        self.daily_dung = daily_dung
        self.dilution_ratio = dilution_ratio
        self.hrt = hrt
        self.slurry_density = slurry_density

    # ----------------------------------------------------
    # Water Required
    # ----------------------------------------------------

    def daily_water_required(self):

        return self.daily_dung * self.dilution_ratio

    # ----------------------------------------------------
    # Total Slurry Mass
    # ----------------------------------------------------

    def daily_slurry_mass(self):

        return self.daily_dung + self.daily_water_required()

    # ----------------------------------------------------
    # Slurry Volume
    # ----------------------------------------------------

    def daily_slurry_volume(self):

        """
        m³/day
        """

        return self.daily_slurry_mass() / self.slurry_density

    # ----------------------------------------------------
    # Digester Working Volume
    # ----------------------------------------------------

    def digester_volume(self):

        """
        Working Volume (m³)

        V = Daily Slurry Volume × HRT
        """

        return self.daily_slurry_volume() * self.hrt

    # ----------------------------------------------------
    # Hydraulic Loading Rate
    # ----------------------------------------------------

    def hydraulic_loading_rate(self):

        """
        m³/day
        """

        return self.daily_slurry_volume()

    # ----------------------------------------------------
    # Summary
    # ----------------------------------------------------

    def summary(self):

        return {

            "Daily Dung (kg/day)": round(
                self.daily_dung,
                2
            ),

            "Daily Water (kg/day)": round(
                self.daily_water_required(),
                2
            ),

            "Daily Slurry (kg/day)": round(
                self.daily_slurry_mass(),
                2
            ),

            "Daily Slurry Volume (m³/day)": round(
                self.daily_slurry_volume(),
                3
            ),

            "Hydraulic Retention Time (days)": self.hrt,

            "Working Digester Volume (m³)": round(
                self.digester_volume(),
                3
            ),

            "Hydraulic Loading Rate (m³/day)": round(
                self.hydraulic_loading_rate(),
                3
            )

        }
