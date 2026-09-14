from pathlib import Path

import pystac


def validate_catalog(catalog_path: Path):
    """Takes the path to a local catalog and performs a JSON schema validation on it

    Args:
        catalog_path (Path): _description_
    """
    catalog = pystac.Catalog.from_file(catalog_path)
    catalog.validate_all()
