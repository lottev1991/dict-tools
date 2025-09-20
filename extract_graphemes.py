import sys
import string

def get_unique_graphemes(file_path):
    """
    Reads a text file and returns a sorted list of all unique graphemes found.
    """
    unique_graphemes = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for char in line:
                    unique_graphemes.add(char)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    
    return sorted(list(unique_graphemes))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_graphemes.py <input_file_path>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    graphemes = get_unique_graphemes(input_file)
    
    if graphemes:
        with open('graphemes-out.txt', 'w') as f:
            for grapheme in graphemes:
                print(grapheme, file=f)
                # print(grapheme)
            print('Graphemes have been extracted! You can find them in a file called \'graphemes-out.txt\'.')
    else:
        print("No graphemes were found in the file.")