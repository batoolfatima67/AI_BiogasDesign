"""
=========================================================
BioDesignAI
Gas Production & Demand Calculations

Author : Batool Fatima
Version: 1.0

This module calculates:
1. Daily dung production
2. Daily household gas demand
3. Gas production from available dung
4. Required dung for household demand
5. Gas balance
=========================================================
"""

from calculations.constants import (
    GAS_YIELD,
    DUNG_PRODUCTION,
    DEFAULT_GAS_REQUIREMENT,
)


class GasCalculator:
    """
    Gas production and demand calculator.
    """

    def __init__(
        self,
        waste_type: str,
        number_of_animals: int,
        family_members: int,
        dung_per_animal: float = None,
        gas_requirement: float = None,
    ):

        self.waste_type = waste_type
        self.number_of_animals = number_of_animals
        self.family_members = family_members

        # Use user-defined value if available
        if dung_per_animal is None:
            self.dung_per_animal = DUNG_PRODUCTION[waste_type]
        else:
            self.dung_per_animal = dung_per_animal

        if gas_requirement is None:
            self.gas_requirement = DEFAULT_GAS_REQUIREMENT
        else:
            self.gas_requirement = gas_requirement

        self.gas_yield = GAS_YIELD[waste_type]

    # ----------------------------------------------------
    # Daily dung production
    # ----------------------------------------------------

    def daily_dung_production(self):

    return self.number_of_animals * self.dung_per_animal

    # ----------------------------------------------------
    # Daily gas demand
    # ----------------------------------------------------

    def daily_gas_demand(self):

    return self.family_members * self.gas_requirement

    # ----------------------------------------------------
    # Daily gas production
    # ----------------------------------------------------

    def daily_gas_production(self):

    return self.daily_dung_production() * self.gas_yield

    # ----------------------------------------------------
    # Required Gas Storage
    # ----------------------------------------------------

    def required_gas_storage(
    self,
    storage_factor=0.40,
    ):
    """
    Recommended gas storage volume.

    Usually 35–50% of
    daily gas production.
    """

    return (
        self.daily_gas_production()
        * storage_factor
    )

    # ----------------------------------------------------
    # Required dung
    # ----------------------------------------------------

    def required_dung(self):

    return self.daily_gas_demand() / self.gas_yield

    # ----------------------------------------------------
    # Gas surplus / deficit
    # ----------------------------------------------------

    def gas_balance(self):

    return self.daily_gas_production() - self.daily_gas_demand()

    # ----------------------------------------------------
    # Plant feasibility
    # ----------------------------------------------------

    def plant_status(self):

        if self.gas_balance() >= 0:
            return "Sufficient"

        return "Insufficient"

    # ----------------------------------------------------
    # Engineering recommendation
    # ----------------------------------------------------

    def recommendation(self):

        if self.plant_status() == "Sufficient":

            return (
                "Available feedstock is sufficient to meet the "
                "daily household gas demand."
            )

        shortage = abs(self.gas_balance())

        return (
            f"Feedstock is insufficient. "
            f"Additional gas requirement = {shortage:.2f} m³/day."
        )

    # ----------------------------------------------------
    # Summary dictionary
    # ----------------------------------------------------

    def summary(self):

        return {

            "Waste Type": self.waste_type,

            "Gas Yield (m³/kg)": round(self.gas_yield, 3),

            "Daily Dung (kg/day)": round(
                self.daily_dung_production(), 2
            ),

            "Daily Gas Production (m³/day)": round(
                self.daily_gas_production(), 2
            ),

            "Daily Gas Demand (m³/day)": round(
                self.daily_gas_demand(), 2
            ),

            "Required Dung (kg/day)": round(
                self.required_dung(), 2
            ),

            "Gas Balance (m³/day)": round(
                self.gas_balance(), 2
            ),

            "Plant Status": self.plant_status(),

            "Recommendation": self.recommendation(),

        }
