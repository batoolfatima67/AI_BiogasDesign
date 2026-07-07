"""
=========================================================
BioDesignAI
Inlet Chamber Design

Author : Batool Fatima
Version : 1.0
=========================================================
"""

import math


class InletCalculator:
    """
    Rectangular inlet chamber design.
    """

    def __init__(
        self,
        daily_slurry_volume: float,
        height: float = 1.20,
        storage_factor: float = 1.0,
    ):

        self.daily_slurry_volume = daily_slurry_volume

        self.height = height

        self.storage_factor = storage_factor

    # ----------------------------------------------------

    def chamber_volume(self):
        """
        One-day slurry storage.
        """

        return (
            self.daily_slurry_volume
            * self.storage_factor
        )

    # ----------------------------------------------------

    def width(self):

        return math.sqrt(

            self.chamber_volume()

            / (2 * self.height)

        )

    # ----------------------------------------------------

    def length(self):

        return 2 * self.width()

    # ----------------------------------------------------

    def summary(self):

        return {

            "Inlet Volume (m³)": round(
                self.chamber_volume(), 3
            ),

            "Inlet Length (m)": round(
                self.length(), 3
            ),

            "Inlet Width (m)": round(
                self.width(), 3
            ),

            "Inlet Height (m)": round(
                self.height, 3
            )

        }
