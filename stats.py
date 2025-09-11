def count_words(text):
    return len(text.split())
# Counts the number of words in the path_to_book

def count_characters(text):
    convert_to_lower = text.lower()
    characters = {}
    for char in convert_to_lower:
        if char.isalpha(): # Consider only alphabet letters
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters
# Counts the occurrences of each character in the path_to_book

def sorting_characters(characters):
    result = []
    for char, count in characters.items():
        mini_dict = {"char": char, "num": count}
        result.append(mini_dict)
    def sort_key(item):
        return item["num"]
    result.sort (key = sort_key, reverse=True)
    return result
# Converts the characters dictionary to a list of dictionaries with 'char' and 'count' keys
# and returns the list sorted by characters
# in descending order of their counts