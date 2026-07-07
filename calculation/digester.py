"""
=========================================================
BioDesignAI
Digester Design Module

Author : Batool Fatima
Version : 1.0

Calculates:

1. Working Digester Volume
2. Freeboard Volume
3. Total Digester Volume
4. Digester Height
5. Digester Diameter
6. Digester Radius
7. Floor Area
8. Wall Area

Gas storage is calculated separately in dome.py.
=========================================================
"""

import math

from calculations.constants import DEFAULT_FREEBOARD


class DigesterCalculator:
    """
    Digester geometry calculator.
    """

    def __init__(
        self,
        working_volume: float,
        freeboard: float = DEFAULT_FREEBOARD,
    ):
        """
        Parameters
        ----------
        working_volume : float
            Required working volume of the digester (m³).

        freeboard : float
            Extra freeboard allowance (fraction of working volume).
        """

        self.working_volume = working_volume
        self.freeboard = freeboard

    # -------------------------------------------------------
    # Freeboard Volume
    # -------------------------------------------------------

    def freeboard_volume(self):
        """
        Extra freeboard volume (m³).
        """

        return self.working_volume * self.freeboard

    # -------------------------------------------------------
    # Total Structural Volume
    # -------------------------------------------------------

    def total_volume(self):
        """
        Total structural volume of the cylindrical digester.

        Gas storage is designed separately
        inside the fixed dome.
        """

        return (
            self.working_volume
            + self.freeboard_volume()
        )

    # -------------------------------------------------------
    # Digester Height
    # -------------------------------------------------------

    def height(self):
        """
        Assuming:

            Diameter = 2 × Height

        Therefore,

            V = πH³

            H = (V / π)^(1/3)
        """

        return (self.total_volume() / math.pi) ** (1 / 3)

    # -------------------------------------------------------
    # Digester Diameter
    # -------------------------------------------------------

    def diameter(self):
        """
        Digester diameter (m).
        """

        return 2 * self.height()

    # -------------------------------------------------------
    # Digester Radius
    # -------------------------------------------------------

    def radius(self):
        """
        Digester radius (m).
        """

        return self.diameter() / 2

    # -------------------------------------------------------
    # Floor Area
    # -------------------------------------------------------

    def floor_area(self):
        """
        Circular floor area (m²).
        """

        return math.pi * self.radius() ** 2

    # -------------------------------------------------------
    # Circumference
    # -------------------------------------------------------

    def circumference(self):
        """
        Circumference of digester (m).
        """

        return math.pi * self.diameter()

    # -------------------------------------------------------
    # Wall Area
    # -------------------------------------------------------

    def wall_area(self):
        """
        Cylindrical wall area (m²).
        """

        return self.circumference() * self.height()

    # -------------------------------------------------------
    # Summary
    # -------------------------------------------------------

    def summary(self):
        """
        Return all calculated values.
        """

        return {

            "Working Volume (m³)": round(
                self.working_volume, 3
            ),

            "Freeboard Volume (m³)": round(
                self.freeboard_volume(), 3
            ),

            "Total Digester Volume (m³)": round(
                self.total_volume(), 3
            ),

            "Digester Height (m)": round(
                self.height(), 3
            ),

            "Digester Diameter (m)": round(
                self.diameter(), 3
            ),

            "Digester Radius (m)": round(
                self.radius(), 3
            ),

            "Floor Area (m²)": round(
                self.floor_area(), 3
            ),

            "Circumference (m)": round(
                self.circumference(), 3
            ),

            "Wall Area (m²)": round(
                self.wall_area(), 3
            )

        }
