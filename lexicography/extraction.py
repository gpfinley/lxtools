import csv
import re
import fire
from typing import List, Tuple, Iterable


def read_and_write(in_file, out_file, headword_pattern, groupnum, encoding):
    """
    De facto main method: create a CSV from a specially formatted file.
    :param in_file:
    :param out_file:
    :param headword_pattern:
    :param encoding:
    :return:
    """
    write_csv(out_file, read_file(in_file, headword_pattern, groupnum, encoding))


def read_file(in_path: str,
              headword_pattern: str,
              groupnum: int,
              encoding: str='utf-8',
              newline_to_space=True) -> List[Tuple[str, str]]:
    """
    Read a text file and
    Any lines not containing the headword end tag are considered part of the entry.
    :param in_path:
    :param headword_pattern:
    :param groupnum: regular expression group containing the headword
    :param encoding:
    :param newline_to_space:
    :return: a list of two-item tuples: headword and content (not re-sorted)
    """
    entries = []
    last_headword = None

    last_headword_end = 0
    text_file = open(in_path, encoding=encoding).read()
    for match in re.finditer(headword_pattern, text_file):
        print(match.group(groupnum))
        headword_start_index, headword_end_index = match.start(groupnum), match.end(groupnum)
        if last_headword is not None:
            entries.append((last_headword, text_file[last_headword_end:headword_start_index]))
        last_headword = text_file[headword_start_index:headword_end_index]
        last_headword_end = headword_end_index
    entries.append((last_headword, text_file[last_headword_end:]))
    if newline_to_space:
        entries = [(headword, entry.replace('\n', ' ')) for headword, entry in entries]
    return entries


def write_csv(outpath: str, entries: List[Iterable]) -> None:
    """
    Save a list of tuples (e.g., headword, content) to a CSV file.
    :param outpath: the path to write to
    :param entries: a list of entry tuples or lists
    :return:
    """
    with open(outpath, 'w') as w:
        csvwriter = csv.writer(w)
        for entry in entries:
            csvwriter.writerow(entry)


if __name__ == '__main__':
    fire.Fire(read_and_write)
