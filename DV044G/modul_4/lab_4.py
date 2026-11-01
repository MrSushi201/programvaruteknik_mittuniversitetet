#!/usr/bin/env python

"""DV044G - LAB ASSIGNMENT 4

The assignment requirements are described in the lab instructions.
Do not modify the provided constants, variable names, or function
signatures unless explicitly instructed by the assignment.

Functions to implement:

Grade G:
    - authenticate_user(..)
    - format_username(..)
    - main()

Grade VG (optional):
    - See spies_r_us.py

Example input:
    joHn BElusHI CaLzOnE

Expected output:
    Authentication successful. User may now access the system!

Example input:
    joHn BElusHI calzone

Expected output:
    Authentication failed. Program exits...
"""

def format_username(username: list[str]) -> str:
    """Format and return a username."""

    ''' PSEUDO CODE
    SPLIT username into first name and last name
    FORMAT both names according to the requirements
    COMBINE the formatted names into a username
    RETURN formatted username
    '''

    formatted_username_list = []

    for i in username:
        formatted_username_list.append(i[0].upper() + i[1:].lower())

    # print(formatted_username_list) # Kontrollera att formatted_username_list är inte längre en tom lista utan faktiskt innehåller formatterade förnamn och efternamn

    return "_".join(formatted_username_list)


def calculate_rotation_seed(password: str) -> int:
    """Calculate and return a rotation seed based on the password."""

    ''' PSEUDO CODE
    PROCESS all characters in the password
    CALCULATE a numeric value according to the requirements
    RETURN calculated rotation seed
    '''

    total = 0
    position = 0

    for _ in password:
        position = position + 1
        total = total + (ord(_) * position)

    rotation_seed = int(total // position)

    return rotation_seed


def decrypt_password(password: str) -> str:
    """Decrypt and return the provided password."""
    rot7, rot9 = 7, 9      # Rotation values. MAY NOT BE MODIFIED!
    vowels = "AEIOUaeiou"  # MAY NOT BE MODIFIED!
    decrypted = ""         # Stores decrypted password
    rotation_seed = 0      # Stores calculated rotation seed (VG)

    ''' PSEUDO CODE
    [VG] PREPROCESS password using the provided function
    PROCESS all characters in the password
    DETERMINE how each character should be transformed
    BUILD decrypted password
    RETURN decrypted password
    '''

    # [VG] - Implementation
    reordered = reorder_password(password, calculate_rotation_seed(password))

    index = 0

    for char in reordered:
        char_value = ord(char)
        if char_value < 33 or char_value > 126:
            raise ValueError("Character outside the ASCII range 33-126 as specified in the requirement.")

        rotation_key = rot7 if index % 2 == 0 else rot9
        decryption_value = char_value + rotation_key

        if decryption_value > 126:
            decryption_value = decryption_value - 94

        decrypted_char = chr(decryption_value)

        if char in vowels:
            decrypted = decrypted + "0" + decrypted_char + "0"

        else:
            decrypted = decrypted + decrypted_char

        index = index + 1

    return decrypted


def reorder_password(password: str, rotation_seed: int) -> str:
    """Based on the rotation seed, return a reordered variant of the password."""
    reordered = ""  # Stores reordered password

    ''' PSEUDO CODE
    DETERMINE how the password should be reordered
    PROCESS the password according to the assignment requirements
    STORE result in reordered
    RETURN reordered password
    '''

    result = rotation_seed % 3

    if result == 0:
        reordered = password[::-1]

    elif result == 1:
        for index in range(0, len(password), 2):
            reordered += password[index:index + 2][::-1]

    else:
        shift = rotation_seed % len(password)
        reordered = password[-shift:] + password[:-shift] if shift else password

    return reordered


def authenticate_user(credentials: str) -> bool:
    """Validate the provided credentials and return the authentication result."""
    agents = {  # Valid credentials used for authentication. MAY NOT BE MODIFIED!
        # Key: formatted username
        # Value: [decrypted_G_password, decrypted_VG_password]

        "Chevy_Chase": ["i0J0u0j0u0J0Zys0r0{", "i0J0u0j0u0J0Zys0r0{"],  # cipher: bAnanASplit
        "Dan_Aykroyd": ["i0N00h00~0[$", "[$i0N00h00~0"],                # cipher: bEauTy
        "John_Belushi": ["J0j0S%0V0w0L0", "u0N0J0j0S%0V0"]              # cipher: CaLzOnE
    }

    ''' PSEUDO CODE
    EXTRACT username and password from credentials
    PROCESS username using the provided function
    PROCESS password using the provided function
    VALIDATE the processed values against the known credentials
    RETURN authentication result
    '''

    input_split = credentials.split(" ")

    user_tmp = input_split[0] + " " + input_split[1]
    pass_tmp = input_split[2]

    # print(user_tmp)
    # print(pass_tmp)

    username = user_tmp.split(" ")
    password = pass_tmp

    # print(username)
    # print(password)

    formatted_username = format_username(username=username)
    decrypted_password = decrypt_password(password=password)

    # print(formatted_username)
    # print(decrypted_password)

    if (formatted_username in agents) and (decrypted_password in agents[formatted_username]):
        return True
    else:
        return False


def main():
    """Main program execution."""
    PROMPT = "Enter your credentials: "  # DO NOT MODIFY CONSTANT VALUE

    credentials = ""          # Stores complete user input
    is_authenticated = False  # Stores outcome of authentication

    ''' PSEUDO CODE
    READ user input
    DETERMINE if user credentials are valid by using the provided function
    DISPLAY success or failed message
    '''

    credentials = input(PROMPT)
    is_authenticated = authenticate_user(credentials)

    if is_authenticated:
        print("Authentication successful! User may now access the system!")
    else:
        print("Authentication failed. Program exits...")


''' PSEUDO CODE
START main program execution
'''

if __name__ == '__main__':
    main()