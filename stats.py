def get_number_of_words(text: str):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def count_symbols(text: str):
    symbols = {}
    for symbol in text:
        if symbol.lower() in symbols:
            symbols[symbol.lower()] += 1
        else:
            symbols[symbol.lower()] = 1
    return symbols

def sort_symbols_dictionary(dictionary: dict):
    final_list = []
    for key in dictionary:
        if key.isalpha():
            final_list.append({"char": key, "num": dictionary[key]})

    def sort_on(items):
        return items["num"]

    final_list.sort(reverse=True, key=sort_on)
    return final_list

