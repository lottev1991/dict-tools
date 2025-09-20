import sys
from collections import defaultdict

def number_dupes(input_path, output_path):
    line_counts = defaultdict(int)

    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            stripped_line = line.strip()  # Removes leading/trailing whitespace and newlines
            line_counts[stripped_line] += 1
            count = line_counts[stripped_line]

            if count > 1:
                outfile.write(f"{stripped_line}({count})\n")
            else:
                outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python number_dupes.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        number_dupes(input_file, output_file)
        print(f"Duplicate lines marked and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)