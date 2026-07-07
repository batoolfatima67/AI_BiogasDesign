"""
=========================================================
BioDesignAI
Outlet Chamber Design

Author : Batool Fatima
Version : 1.0

Calculates:

1. Outlet Chamber Volume
2. Outlet Chamber Length
3. Outlet Chamber Width
4. Outlet Chamber Height

=========================================================
"""

import math


class OutletCalculator:
    """
    Rectangular outlet chamber design.
    """

    def __init__(
        self,
        daily_slurry_volume: float,
        height: float = 1.20,
        storage_factor: float = 1.20,
    ):
        """
        Parameters
        ----------
        daily_slurry_volume : float
            Daily slurry volume entering the digester (m³/day).

        height : float
            Outlet chamber height (m).

        storage_factor : float
            Safety/storage factor.
            Default = 1.2 (20% extra capacity)
        """

        self.daily_slurry_volume = daily_slurry_volume
        self.height = height
        self.storage_factor = storage_factor

    # -----------------------------------------------------
    # Outlet Volume
    # -----------------------------------------------------

    def chamber_volume(self):
        """
        Required outlet chamber volume.
        """

        return (
            self.daily_slurry_volume
            * self.storage_factor
        )

    # -----------------------------------------------------
    # Width
    # -----------------------------------------------------

    def width(self):
        """
        Assuming:

        Length = 2 × Width

        Volume = L × W × H
        """

        return math.sqrt(
            self.chamber_volume()
            / (2 * self.height)
        )

    # -----------------------------------------------------
    # Length
    # -----------------------------------------------------

    def length(self):

        return 2 * self.width()

    # -----------------------------------------------------
    # Summary
    # -----------------------------------------------------

    def summary(self):

        return {

            "Outlet Volume (m³)": round(
                self.chamber_volume(),
                3
            ),

            "Outlet Length (m)": round(
                self.length(),
                3
            ),

            "Outlet Width (m)": round(
                self.width(),
                3
            ),

            "Outlet Height (m)": round(
                self.height,
                3
            )

        }
