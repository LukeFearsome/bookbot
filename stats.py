def get_no_of_words(text):
    return len(text.split())

def count_chars(text):
    occurences = {}
    
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in occurences: 
                occurences[char] += 1
            else:
                occurences[char] = 1
    return occurences

def get_char_key(pair):
    return pair["num"]

def sort_dict(unsorted):
    cleaned = []
    for k,v in unsorted.items():
        pair = {
            "char": k,
            "num": v
        }
        cleaned.append(pair)
    
    cleaned.sort(reverse=True,key=get_char_key)
    return cleaned
