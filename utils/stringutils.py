
def capitalize_first_letter(text_string):
    """
    Capitalizes the first letter of a string. The same can be done using the str.capitalize function

    :param text_string: String which has to be converted to capital case
    :return: String in capital case
    """
    return text_string[0].upper() + text_string[1:].lower()


def get_item_count_dictionary_from_list(generic_list):
    """
    Given a list of items returns a dictionary containing its counts

    :param generic_list: List containing the items
    :return: Dictionary containing the item counts
    """
    generic_dict = dict({})
    for element in generic_list:
        if element in generic_dict.keys():
            generic_dict[element] += 1
        else:
            generic_dict[element] = 1
    return generic_dict


def add_anchor_tag_to_string(url):
    """
    Attaches an anchor tag with each url string

    :param url: URL string in which the anchor tag has to be attached
    :return: URL string with the anchor tag attached
    """
    anchor_text = '<a href=' + '"' + url + '"' + ' target="_blank" ' + '>' + 'Story Link' + ' </a>'
    return anchor_text
