# mock_policy_data.py
"""
Contains mock insurance companies, policy types, and policy documents for the Insurance Policy Q&A Chatbot demo.
All data is fictional and for demonstration purposes only.
"""

MOCK_INSURANCE_DATA = {
    "Allianz": {
        "Private Liability Insurance": {
            "preview": "Covers personal liability for damages to third parties, including property and injury.",
            "document": "Section 1: Coverage\nThis policy covers personal liability for damages caused to third parties, including accidental property damage and bodily injury.\nSection 2: Exclusions\nExclusions apply to intentional acts, damages caused by motor vehicles, and professional activities.\nSection 3: Claims Process\nClaims must be reported within 30 days of the incident. Supporting documentation is required.\nSection 4: Limits\nMaximum coverage is 10 million EUR per incident. Legal costs are included up to 100,000 EUR.\nSection 5: Additional Benefits\nIncludes coverage for loss of keys and volunteer activities.\nSection 6: Termination\nPolicy may be terminated with 3 months' notice before renewal."
        },
        "Home Contents Insurance": {
            "preview": "Protects household belongings against fire, theft, and water damage. Max coverage 50,000 EUR.",
            "document": "Section 1: Insured Items\nCovers furniture, electronics, clothing, and valuables against fire, theft, and water damage.\nSection 2: Coverage Limits\nMaximum coverage is 50,000 EUR. Jewelry and valuables are covered up to 5,000 EUR.\nSection 3: Exclusions\nFlood damage and wear-and-tear are not covered.\nSection 4: Claims\nClaims must be filed within 14 days of discovery. Police report required for theft.\nSection 5: Premiums\nAnnual premium is based on property value and location.\nSection 6: Policy Changes\nPolicyholder must notify insurer of major purchases or renovations."
        },
    },
    "AXA": {
        "Car Liability Insurance": {
            "preview": "Mandatory liability coverage for damages to others while operating your vehicle.",
            "document": "Section 1: Coverage\nProvides mandatory liability coverage for damages caused to others while operating your vehicle.\nSection 2: Exclusions\nDoes not cover damage to your own car, intentional acts, or racing.\nSection 3: Coverage Limit\n100 million EUR for property damage, 15 million EUR for bodily injury per person.\nSection 4: Claims\nAccidents must be reported within 48 hours. Police report required for major incidents.\nSection 5: Additional Services\nIncludes roadside assistance and legal support.\nSection 6: Premiums\nPremiums depend on driver history and vehicle type."
        },
        "Legal Protection Insurance": {
            "preview": "Covers legal costs for disputes in private and professional life, including lawyer fees.",
            "document": "Section 1: Coverage\nCovers legal costs for disputes in private and professional life, including lawyer fees, court costs, and mediation.\nSection 2: Exclusions\nExcludes pre-existing disputes, criminal cases, and intentional violations.\nSection 3: Claims\nLegal assistance must be requested before engaging a lawyer.\nSection 4: Coverage Limit\nUp to 300,000 EUR per case.\nSection 5: Waiting Period\nThree-month waiting period applies for most disputes.\nSection 6: Termination\nPolicy can be terminated annually with one month's notice."
        },
    },
    "ERGO Group": {
        "Building Insurance": {
            "preview": "Insures residential buildings against fire, storm, hail, and water damage.",
            "document": "Section 1: Insured Property\nCovers residential buildings, outbuildings, and garages.\nSection 2: Covered Risks\nFire, storm, hail, and certain types of water damage.\nSection 3: Exclusions\nEarthquake and flood coverage require additional riders.\nSection 4: Claims\nClaims must be reported within 7 days. Emergency repairs are reimbursed.\nSection 5: Coverage Limit\nBased on reconstruction value of the property.\nSection 6: Premiums\nPremiums depend on location, building age, and construction type."
        },
        "Travel Insurance": {
            "preview": "Covers emergency medical expenses and trip cancellation for international travel.",
            "document": "Section 1: Medical Coverage\nEmergency medical expenses abroad, including hospitalization and repatriation.\nSection 2: Trip Cancellation\nReimburses non-refundable costs if trip is cancelled for covered reasons.\nSection 3: Lost Luggage\nLost luggage is covered up to 1,000 EUR.\nSection 4: Exclusions\nPre-existing medical conditions and high-risk activities are excluded.\nSection 5: Claims\nClaims must be submitted within 30 days of return.\nSection 6: Assistance\n24/7 emergency hotline available worldwide."
        },
    },
    "HUK-COBURG": {
        "Private Health Insurance": {
            "preview": "Reimburses medical expenses for outpatient and inpatient treatments, includes dental.",
            "document": "Section 1: Coverage\nReimburses medical expenses for outpatient, inpatient, and specialist treatments.\nSection 2: Dental and Alternative Medicine\nIncludes dental coverage and alternative medicine up to policy limits.\nSection 3: Deductible\n500 EUR annual deductible applies.\nSection 4: Exclusions\nCosmetic procedures and experimental treatments are excluded.\nSection 5: Claims\nClaims must be submitted with original invoices.\nSection 6: Premiums\nPremiums based on age, health status, and coverage level."
        },
        "Pet Liability Insurance": {
            "preview": "Covers damages caused by your pet to third parties, includes dogs and cats.",
            "document": "Section 1: Coverage\nCovers damages caused by your pet to third parties, including property and injury.\nSection 2: Covered Animals\nIncludes dogs and cats. Excludes exotic animals.\nSection 3: Exclusions\nIntentional acts and damages to family members are excluded.\nSection 4: Claims\nClaims must be reported within 14 days.\nSection 5: Coverage Limit\nUp to 2 million EUR per incident.\nSection 6: Premiums\nPremiums depend on animal type and breed."
        },
    },
    "Generali Deutschland": {
        "Accident Insurance": {
            "preview": "Provides compensation for accidental injury resulting in disability or death.",
            "document": "Section 1: Coverage\nFinancial compensation in case of accidental injury resulting in disability or death.\nSection 2: Worldwide Coverage\nCovers accidents worldwide, 24/7.\nSection 3: Exclusions\nProfessional sports and intentional acts are excluded.\nSection 4: Claims\nClaims must be filed within 30 days. Medical documentation required.\nSection 5: Coverage Limit\nUp to 500,000 EUR for disability, 100,000 EUR for death.\nSection 6: Premiums\nPremiums based on occupation and risk level."
        },
        "Bicycle Insurance": {
            "preview": "Covers theft and damage to bicycles, includes roadside assistance in Germany.",
            "document": "Section 1: Coverage\nCovers theft and damage to bicycles, including vandalism and accidents.\nSection 2: Roadside Assistance\nRoadside assistance within Germany.\nSection 3: E-bikes\nE-bikes are covered up to 3,000 EUR.\nSection 4: Exclusions\nWear and tear, and racing are not covered.\nSection 5: Claims\nClaims must be reported within 7 days. Police report required for theft.\nSection 6: Premiums\nPremiums depend on bike value and location."
        },
    },
}
