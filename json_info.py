from loguru import logger


def get_info_xlsx(ws, restaurant_cell, config):
    restaurant = ws[restaurant_cell].value
    if restaurant in config["legal_entities"]:
        iiko_name = config["legal_entities"][restaurant]["iiko_name"]
        non_excise_dishes = config["legal_entities"][restaurant]["non_excise_dishes"]
        non_excise_groups = config["legal_entities"][restaurant]["non_excise_groups"]
        db_name = config["legal_entities"][restaurant]["db_name"]
        logger.info(
            f"В ресторані {iiko_name}: \nбезакцизні страви - {non_excise_dishes} \nбезакцизні групи страв - {non_excise_groups}")
        return (iiko_name, non_excise_dishes, non_excise_groups, db_name)
    else:
        logger.error(
            f"{ws[restaurant_cell].value} не існує в файлі JSON. Будь ласка, перевір!")


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
            f"{ws[restaurant_cell].value} не існує в файлі JSON. Будь ласка, перевір!")