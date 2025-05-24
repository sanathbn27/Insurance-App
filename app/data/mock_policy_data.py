# mock_policy_data.py
"""
Contains mock insurance companies, policy types, and policy documents for the Insurance Policy Q&A Chatbot demo.
All data is fictional and for demonstration purposes only.
"""

MOCK_INSURANCE_DATA = {
    "Allianz": {
        "Private Liability Insurance": "This policy covers personal liability for damages caused to third parties. It includes coverage for accidental property damage and bodily injury. Exclusions apply to intentional acts and damages caused by motor vehicles.",
        "Home Contents Insurance": "This policy protects household belongings against risks such as fire, theft, and water damage. The maximum coverage is 50,000 EUR. Valuables like jewelry are covered up to 5,000 EUR. Flood damage is not included.",
    },
    "AXA": {
        "Car Liability Insurance": "This policy provides mandatory liability coverage for damages caused to others while operating your vehicle. It does not cover damage to your own car. Coverage limit is 100 million EUR for property damage.",
        "Legal Protection Insurance": "This policy covers legal costs for disputes in private and professional life. It includes lawyer fees, court costs, and mediation. Excludes pre-existing disputes and criminal cases.",
    },
    "ERGO Group": {
        "Building Insurance": "This policy insures residential buildings against fire, storm, hail, and certain types of water damage. Outbuildings and garages are included. Earthquake and flood coverage require additional riders.",
        "Travel Insurance": "This policy covers emergency medical expenses and trip cancellation for international travel. Lost luggage is covered up to 1,000 EUR. Pre-existing medical conditions are excluded.",
    },
    "HUK-COBURG": {
        "Private Health Insurance": "This policy reimburses medical expenses for outpatient and inpatient treatments. It includes dental coverage and alternative medicine. There is a deductible of 500 EUR per year.",
        "Pet Liability Insurance": "This policy covers damages caused by your pet to third parties. It includes coverage for dogs and cats. Excludes damages caused by exotic animals.",
    },
    "Generali Deutschland": {
        "Accident Insurance": "This policy provides financial compensation in case of accidental injury resulting in disability or death. It covers accidents worldwide, 24/7. Sports injuries are included, but professional sports are excluded.",
        "Bicycle Insurance": "This policy covers theft and damage to bicycles. It includes roadside assistance within Germany. E-bikes are covered up to 3,000 EUR. Wear and tear is not covered.",
    },
}
