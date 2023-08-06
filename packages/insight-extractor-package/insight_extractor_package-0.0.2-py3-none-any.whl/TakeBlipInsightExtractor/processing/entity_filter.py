from math import floor


def filter_entity(entities_column: list, entities_to_keep: set,
                  field_name: str) -> list:
    """Filter the entities a specific class

    Parameters
    ----------
    entities_column : list
        list with the entities of each row
    entities_to_keep : set
        set with the the match of a field to filter
    field_name : str
        string indicating which field should be used to filter the entities

    Returns
    -------
    list
        list with the entities filtered
    """

    filtered_entities_list = []
    for entities_list in entities_column:
        if len(entities_list) > 0:
            filtered_list = [entity_dict for entity_dict in entities_list
                             if entity_dict[field_name] in entities_to_keep]
        else:
            filtered_list = []
        filtered_entities_list.append(filtered_list)
    return filtered_entities_list


def filter_entity_type(entities_column: list) -> list:
    """Filter the entities to keep only the desired type
    Parameters
    ----------
    entities_column : list
        List with entities of each row

    Returns
    -------
    list
        List with the entities of each row, filtered to contained only the
        entities of specific class.
    """
    entity_list = filter_entity(
        entities_column=entities_column,
        entities_to_keep={'generic_entity', 'financial'},
        field_name='type')
    return entity_list


def filter_entity_frequency(entities_column: list,
                            entity_frequency_dict: dict) -> list:
    """Filter the entities based on the frequency

    Parameters
    ----------
    entities_column : list
        List with entities of each row
    entity_frequency_dict : dict
         Dictionary with entities as keys and frequency as values,
         filtered by the frequency

    Returns
    -------
    list
        List with the entities of each row, filtered to the most frequently
    """
    entity_list = filter_entity(
        entities_column=entities_column,
        entities_to_keep=set(entity_frequency_dict.keys()),
        field_name='lowercase_value')
    return entity_list


def create_postagging_dict(entities_column: list) -> dict:
    """Create dictionary with the postag of each entity

    Parameters
    ---------
    entities_column : list
        list with entities of each row

    Returns
    -------
    dict
        Dictionary with key as the entities and values with the postag of the
        entities.
    """
    entity_postagging_dict = {
        entity_dict['lowercase_value']: entity_dict['postags']
        for entities_list in entities_column for entity_dict in entities_list}
    return entity_postagging_dict


def create_entity_frequency_dict(entities_column: list,
                                 percentage_threshold: float) -> dict:
    """
    Create the dictionary with the frequency of each entities and filtered
    using a certain frequency percentile

    Parameters
    ----------
    entities_column : list
        list with the entities of each row
    percentage_threshold : float
        percentile of frequency to filter

    Returns
    -------
    dict
        Dictionary with entities as keys and frequency as values
    """

    frequency = dict()
    for entities_list in entities_column:
        entities = map(dict, set(tuple(entity_dict.items()) for
                                 entity_dict in entities_list))
        for entity_dict in entities:
            entity_name = entity_dict['lowercase_value']
            frequency[entity_name] = frequency.get(entity_name, 0) + 1
    sorted_frequencies_lst = sorted(frequency.values(), reverse=True)
    number_items = floor(percentage_threshold * len(frequency))
    threshold_frequency = sorted_frequencies_lst[:number_items][-1]
    delete_low_frequency_entities(threshold_frequency, frequency)
    return frequency


def delete_low_frequency_entities(threshold_frequency, frequency_dict):
    frequency_dict_copy = frequency_dict.copy()

    if threshold_frequency == 1:
        threshold_frequency = 2

    for entity, frequency in frequency_dict_copy.items():
        if frequency < threshold_frequency:
            del frequency_dict[entity]
