# OpenUtau Dict Tools
Handy tools for creating dictionaries and G2Ps for OpenUtau.
## Acknowledgement
The files in this repository were for 99% vibecoded with the help of Gemini. I did edit some things where I deemed them necessary. I'm not very good at Python, but I tested the code and it works (granted, I didn't really write a large chunk of it myself).
## Getting started
1.  Make sure you have Python installed on your computer. Any 3.x version is fine. No external packages are needed.
2. Second, make sure your dictionary is in **table/spreadsheet format** (can vary from CSV/TSV to XLS(X) etc.).

    * Make sure to mass find-replace the **double spaces between graphemes and phonemes** with something else (e.g. a tab, comma, etc.) beforehand. This is because a single character works better as a column separator when importing into a spreadsheet program.
3.  Open/import the dictionary in a spreadsheet program (e.g. Google Sheets, LibreOffice Calc, Microsoft Excel, etc.).

    * If it's in CSV/TSV format, make sure to pick the correct **column separator** (aka whatever you replaced the double spaces with above).
4. Select the entire column of either the words or the phonetic transcriptions in the dictionary and paste them into a new file. Save this file under any filename you want.

    * I do **NOT** recommend using NotePad for this, since it can't handle large files well. I recommend either VSCode, NotePad++ or another powerful text editor.
5. Follow the next steps, depending on what you want to do next.

## Number duplicates
Some open source dictionaries, such as WikiPron, contain duplicate entries that are not numbered. This repo contains a tool that does this automatically.
### Usage
1. Open a terminal in the folder where you saved these Python files.
2. Type `python number_dupes.py <input_file> <output_file>`. Replace input and output with your own filenames.
3. Open the output file, select everything, and copy-paste it into the words column of your spreadsheet file (you can usually select the relevant column by clicking on the column name at the top).
4. Save your suffixed spreadsheet/table file as a TXT. This is what OpenUtau needs.
5. Open the TXT file in an advanced text editor (such as aforementioned VSCode or NotePad++), mass find-replace your column separator back to the double spaces, and save the file.

## Extract graphemes
This tool is for easy grapheme extraction for G2P training and development. Now you no longer have to check for every grapheme manually.
### Usage
1. Open a terminal in the folder where you saved these Python files.
2. Type `python extract_graphemes.py <input_file_path>`. Replace the input with the file where you saved the dictionary words in.
3. The extracted graphemes will be saved in a file called `graphemes-out.txt`. Make sure to back up this file if you want to run the script again! Otherwise it will be overwritten the next time the script is ran.

## Extract phonemes
This tool is for easy phoneme extraction for G2P training and development. Now you no longer have to check for every phoneme manually.
### Usage
1. Open a terminal in the folder where you saved these Python files.
2. Type `python extract_phonemes.py <input_file_path>`. Replace the input with the file where you saved the phonetic transcriptions in.
3. The extracted phonemes will be saved in a file called `phonemes-out.txt`. Make sure to back up this file if you want to run the script again! Otherwise it will be overwritten the next time the script is ran.