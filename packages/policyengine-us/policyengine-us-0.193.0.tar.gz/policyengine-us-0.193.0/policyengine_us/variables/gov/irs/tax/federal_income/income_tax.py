from policyengine_us.model_api import *


class iitax(Variable):
    value_type = float
    entity = TaxUnit
    definition_period = YEAR
    unit = USD
    label = "federal income tax"
    documentation = "Total federal individual income tax liability."
    adds = [
        "income_tax_before_credits",
    ]
    subtracts = [
        "income_tax_refundable_credits",
        "income_tax_capped_non_refundable_credits",
    ]

    def formula(tax_unit, period, parameters):
        before_refundable_credits = tax_unit(
            "income_tax_before_refundable_credits", period
        )
        refundable_credits = tax_unit("income_tax_refundable_credits", period)
        return before_refundable_credits - refundable_credits


income_tax = variable_alias("income_tax", iitax)
