def format_username(username: str) -> str:
    """Format and return a username."""

    ''' PSEUDO CODE
    SPLIT username into first name and last name
    FORMAT both names according to the requirements
    COMBINE the formatted names into a username
    RETURN formatted username
    '''

    space_index = username.find(" ")
    first_name = username[:space_index]
    last_name = username[space_index + 1:]

    formatted_first_name = first_name[0].upper() + first_name[1:].lower()
    formatted_last_name = last_name[0].upper() + last_name[1:].lower()

    formatted_username = formatted_first_name + "_" + formatted_last_name

    return formatted_username