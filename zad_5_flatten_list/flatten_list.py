def flatten_list(nested_list: list) -> list:
    to_flat_list = []
    for el in nested_list:
        if isinstance(el, list):
            to_flat_list.extend(flatten_list(el))
        else:
            to_flat_list.append(el)
    return to_flat_list
