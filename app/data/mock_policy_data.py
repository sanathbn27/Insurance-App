# mock_policy_data.py
"""
Contains mock insurance companies, policy types, and policy documents for the Insurance Policy Q&A Chatbot demo.
All data is fictional and for demonstration purposes only.
"""

import os

def load_policy_document(company, policy):
    base_path = os.path.join(os.path.dirname(__file__), "policy_docs")
    filename = f"{company}__{policy}.txt".replace(" ", "_")
    file_path = os.path.join(base_path, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "[Policy document not found.]"

MOCK_INSURANCE_DATA = {
    "Allianz": {
        "Private Liability Insurance": {
            "preview": "Covers personal liability for damages to third parties, including property and injury.",
            "document": lambda: load_policy_document("Allianz", "Private Liability Insurance")
        },
        "Home Contents Insurance": {
            "preview": "Protects household belongings against fire, theft, and water damage. Max coverage 50,000 EUR.",
            "document": lambda: load_policy_document("Allianz", "Home Contents Insurance")
        },
    },
    "AXA": {
        "Car Liability Insurance": {
            "preview": "Mandatory liability coverage for damages to others while operating your vehicle.",
            "document": lambda: load_policy_document("AXA", "Car Liability Insurance")
        },
        "Legal Protection Insurance": {
            "preview": "Covers legal costs for disputes in private and professional life, including lawyer fees.",
            "document": lambda: load_policy_document("AXA", "Legal Protection Insurance")
        },
    },
    "ERGO Group": {
        "Building Insurance": {
            "preview": "Insures residential buildings against fire, storm, hail, and water damage.",
            "document": lambda: load_policy_document("ERGO Group", "Building Insurance")
        },
        "Travel Insurance": {
            "preview": "Covers emergency medical expenses and trip cancellation for international travel.",
            "document": lambda: load_policy_document("ERGO Group", "Travel Insurance")
        },
    },
    "HUK-COBURG": {
        "Private Health Insurance": {
            "preview": "Reimburses medical expenses for outpatient and inpatient treatments, includes dental.",
            "document": lambda: load_policy_document("HUK-COBURG", "Private Health Insurance")
        },
        "Pet Liability Insurance": {
            "preview": "Covers damages caused by your pet to third parties, includes dogs and cats.",
            "document": lambda: load_policy_document("HUK-COBURG", "Pet Liability Insurance")
        },
    },
    "Generali Deutschland": {
        "Accident Insurance": {
            "preview": "Provides compensation for accidental injury resulting in disability or death.",
            "document": lambda: load_policy_document("Generali Deutschland", "Accident Insurance")
        },
        "Bicycle Insurance": {
            "preview": "Covers theft and damage to bicycles, includes roadside assistance in Germany.",
            "document": lambda: load_policy_document("Generali Deutschland", "Bicycle Insurance")
        },
    },
}
