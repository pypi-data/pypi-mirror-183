__version__ = "0.0.1a1"


# This is needed to allow Airflow to pick up specific metadata fields it needs
# for certain features. We recognize it's a bit unclean to define these in
# multiple places, but at this point it's the only workaround if you'd like
# your custom conn type to show up in the Airflow UI.
def get_provider_info() -> dict:
    return {
        # Required.
        "package-name": "universal-transfer-operator",
        "name": "Universal Transfer Operator",
        "description": (
            "Universal Transfer Operator for Apache Airflow to transfer between files, tables, dataframes, apis."
        ),
        "versions": [__version__],
        # Optional.
        "hook-class-names": [],
        "extra-links": [],
    }
