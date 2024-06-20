import logging



def exctract_properties_names(djson):
    logging.info(f'Началась очистка данных, тип объекта {type(djson)}')
    keys = djson.keys()
    logging.debug(keys)
    logging.info('Завершена очистка данных')
    return keys


def extract_smth_else():
    pass