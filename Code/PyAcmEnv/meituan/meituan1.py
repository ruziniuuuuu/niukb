def mapping_string(in_words):
    # A mapping
    mapping = {
        "Q": "P", "W": "O", "E":"I", "R": "U", "T":"Y", "P": "Q", "O": "W", "I": "E", "U": "R", "Y": "T",
        "A": "L", "S": "K", "D": "J", "F": "H", "G": "G", "H": "F", "J": "D", "K": "S", "L": "A",
        "Z": "M", "X": "N", "C": "B", "V": "V", "B": "C", "N":"X", "M": "Z"
    }

    out_words = ''
    for char in in_words:
        out_words = out_words + mapping[char]
    print(out_words)


if __name__ == '__main__':
    in_words = input()
    out_words = mapping_string(in_words)
    