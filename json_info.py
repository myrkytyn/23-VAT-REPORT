from loguru import logger


def get_info_xlsx(ws, restaurant_cell, config):
    restaurant = ws[restaurant_cell].value
    if restaurant in config["legal_entities"]:
        iiko_name = config["legal_entities"][restaurant]["iiko_name"]
        non_excise_dishes = config["legal_entities"][restaurant]["non_excise_dishes"]
        non_excise_groups = config["legal_entities"][restaurant]["non_excise_groups"]
        logger.info(
            f"In restaurant {iiko_name} are: \nnon excise dishes - {non_excise_dishes} \nnon excise groups - {non_excise_groups}")
        return (iiko_name, non_excise_dishes, non_excise_groups)
    else:
        logger.error(
            f"{ws[restaurant_cell].value} does not exist in JSON. Please check!")


def get_info_xml(ws, restaurant_cell, config):
    restaurant = ws[restaurant_cell].value
    if restaurant in config["legal_entities"]:
        iiko_name = config["legal_entities"][restaurant]["iiko_name"]
        hnamesel = config["legal_entities"][restaurant]["legal_name"]
        tin = config["legal_entities"][restaurant]["tin"]
        hksel = config["legal_entities"][restaurant]["hksel"]
        htinsel = config["legal_entities"][restaurant]["htinsel"]
        hbos = config["legal_entities"][restaurant]["hbos"]
        hkbos = config["legal_entities"][restaurant]["hkbos"]
        return (iiko_name, hnamesel, tin, hksel, htinsel, hbos, hkbos)
    else:
        logger.error(
            f"{ws[restaurant_cell].value} does not exist in JSON. Please check!")
