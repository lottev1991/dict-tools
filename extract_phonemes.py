import sys

def extract_phonemes(filepath):
    """
    Reads a file and returns a set of unique phonemes.
    Each string in the file is expected to be separated by a space.
    """
    unique_phonemes = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line into a list of phonemes based on spaces
                words = line.strip().split(' ')
                # Add the words to the set. A set automatically handles uniqueness.
                for word in words:
                    if word:  # Ensure no empty phonemes from multiple spaces
                        unique_phonemes.add(word)
        return sorted(list(unique_phonemes))
    except FileNotFoundError:
        return "Error: The file '{filepath}' was not found."

# Example usage:
file_path = sys.argv[1]
unique_items = extract_phonemes(file_path)

if isinstance(unique_items, list):
    with open('phonemes-out.txt', 'w') as f:
        for item in unique_items:
            print(item, file=f)
        print('Phonemes have been extracted! You can find them in a file called \'phonemes-out.txt\'.')
else:
    print(unique_items)