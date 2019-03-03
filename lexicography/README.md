# Lexicography tools

Basic tool is a dictionary processor which converts text (probably copied from a PDF dictionary) into a CSV file.

To use (Python 3.6 or later):

python extraction.py <input_txt_path> <output_csv_path> <language_name>

where language\_name is 'wanano' or 'barasana'. You can also specify keyword arguments on the command line (but see the code in configurations.py for the config object's keyword names). Add more configurations manually in the 'parameters' dictionary of configurations.py.
