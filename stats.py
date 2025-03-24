def get_num_words(text):
    words = text.split()
    
    return len(words)

def get_character_count(text):
    dict = {}

    for word in text.split():
        for char in word:
            char = char.lower()
            if not char in dict:
                dict[char] = 0
            dict[char] += 1

    return dict

def sort_on(dict):
    return dict["num"]

def get_sorted_character_count(text):
    character_count = get_character_count(text)
    sorted_character_counts = []

    for char in character_count:
        if char.isalpha():
            sorted_character_counts.append({ "char": char, "num": character_count[char] })

    sorted_character_counts.sort(reverse=True, key=sort_on)

    return sorted_character_counts
