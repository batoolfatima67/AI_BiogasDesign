"""
=========================================================
BioDesignAI
Fixed Dome Geometry Module

Author : Batool Fatima
Version : 1.0

Calculates:

1. Dome Height
2. Dome Radius
3. Dome Volume
4. Gas Storage Volume
5. Surface Area

=========================================================
"""

import math


class DomeCalculator:
    """
    Fixed Dome Geometry Calculator
    """

    def __init__(
        self,
        digester_diameter: float,
        required_gas_storage: float,
    ):

        self.diameter = digester_diameter
        self.radius = digester_diameter / 2

        self.required_gas_storage = required_gas_storage

        # Initial assumption:
        # Dome height = 25% of diameter
        self.height = 0.25 * self.diameter

    # -----------------------------------------------------
    # Dome Radius
    # -----------------------------------------------------

    def dome_radius(self):
        """
        Radius of the sphere forming the spherical cap.

                 a²+h²
        R = ---------------
              2h
        """

        a = self.radius
        h = self.height

        return (a**2 + h**2) / (2 * h)

    # -----------------------------------------------------
    # Dome Volume
    # -----------------------------------------------------

    def dome_volume(self):
        """
        Volume of spherical cap

        V = πh²(3R-h)/3
        """

        h = self.height
        R = self.dome_radius()

        return (math.pi * h**2 * (3 * R - h)) / 3

    # -----------------------------------------------------
    # Surface Area
    # -----------------------------------------------------

    def surface_area(self):
        """
        Surface area of spherical cap

        A = 2πRh
        """

        R = self.dome_radius()
        h = self.height

        return 2 * math.pi * R * h

    # -----------------------------------------------------
    # Gas Storage Check
    # -----------------------------------------------------

    def storage_ok(self):

        return self.dome_volume() >= self.required_gas_storage

    # -----------------------------------------------------
    # Safety Margin
    # -----------------------------------------------------

    def storage_margin(self):

        return self.dome_volume() - self.required_gas_storage

    # -----------------------------------------------------
    # Summary
    # -----------------------------------------------------

    def summary(self):

        return {

            "Dome Height (m)": round(
                self.height,
                3
            ),

            "Sphere Radius (m)": round(
                self.dome_radius(),
                3
            ),

            "Dome Volume (m³)": round(
                self.dome_volume(),
                3
            ),

            "Required Gas Storage (m³)": round(
                self.required_gas_storage,
                3
            ),

            "Surface Area (m²)": round(
                self.surface_area(),
                3
            ),

            "Storage OK": self.storage_ok(),

            "Storage Margin (m³)": round(
                self.storage_margin(),
                3
            )

        }
