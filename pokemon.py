import requests

def get_pokemon_data(pokemon_name):
    """
    Retrieves the data of a specific Pokemon from the PokeAPI.

    This function makes a GET request to the PokeAPI to retrieve the data
    of a specific Pokemon based on its name.

    Parameters:
    - pokemon_name (str): The name of the Pokemon to retrieve data for.

    Returns:
    dict: A dictionary containing the Pokemon's name, abilities, types, and weight.

    Raises:
    - requests.exceptions.RequestException: If there is an error in making the API request.
    """

    # Constructing the URL for the PokeAPI based on the given Pokemon name
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        # Making a GET request to the PokeAPI
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        # Parsing the JSON response into a dictionary
        pokemon_data = response.json()

        # Extracting the required information from the Pokemon data
        name = pokemon_data["name"]
        abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
        types = [type["type"]["name"] for type in pokemon_data["types"]]
        weight = pokemon_data["weight"]

        # Creating a dictionary with the extracted information
        pokemon_info = {
            "name": name,
            "abilities": abilities,
            "types": types,
            "weight": weight
        }

        return pokemon_info

    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error in making API request: {e}")

def create_pokemon_dictionary():
    """
    Creates a dictionary of Pokemon categorized by type.

    This function retrieves data for 20 Pokemon from the PokeAPI and categorizes them
    based on their types. Each Pokemon's name, abilities, types, and weight are included
    in the dictionary.

    Returns:
    dict: A dictionary containing Pokemon categorized by type, with each Pokemon's
          name, abilities, types, and weight.

    Raises:
    - requests.exceptions.RequestException: If there is an error in making the API request.
    """

    # List of Pokemon names to retrieve data for
    pokemon_names = ["charizard", "blastoise", "pikachu", "jigglypuff", "gengar",
                     "machamp", "gyarados", "lapras", "snorlax", "dragonite",
                     "mewtwo", "mew", "typhlosion", "feraligatr", "ampharos",
                     "scizor", "heracross", "kingdra", "tyranitar", "lugia"]

    # Creating an empty dictionary to store the categorized Pokemon data
    pokemon_dictionary = {}

    try:
        # Retrieving data for each Pokemon and categorizing them by type
        for pokemon_name in pokemon_names:
            pokemon_data = get_pokemon_data(pokemon_name)
            types = pokemon_data["types"]

            for pokemon_type in types:
                if pokemon_type not in pokemon_dictionary:
                    pokemon_dictionary[pokemon_type] = {}

                pokemon_dictionary[pokemon_type][pokemon_name] = {
                    "abilities": pokemon_data["abilities"],
                    "weight": pokemon_data["weight"]
                }

        return pokemon_dictionary

    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error in making API request: {e}")

# Example usage:

try:
    pokemon_dict = create_pokemon_dictionary()
    print(pokemon_dict)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")