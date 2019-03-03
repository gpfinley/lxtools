import csv
import re
import fire
from typing import List, Tuple, Iterable
from configurations import Config, parameters


def read_and_write(in_file, out_file, language=None, **kwargs):
    """
    De facto main method: create a CSV from a specially formatted file.
    :param in_file:
    :param out_file:
    :param language:
    :param kwargs:
    :return:
    """
    if language is not None:
        params = parameters[language]
    else:
        params = Config()
    for k, v in kwargs.items():
        setattr(params, k, v)
    tuples = read_file(in_file, params.headword_pattern, params.headword_group, params.encoding)
    processed_tuples = postprocess(tuples, params.entry_postproc_patterns, params.entry_postproc_replacements)
    write_csv(out_file, processed_tuples)


def postprocess(headword_entry_list: Iterable[Tuple[str, str]],
                patterns: Iterable[str],
                replacements: Iterable[str]) -> List[Tuple[str, str]]:
    """
    Perform regex replacements on an extracted dictionary.
    :param headword_entry_list:
    :param patterns:
    :param replacements:
    :return:
    """
    compiled_patterns = [re.compile(pattern) for pattern in patterns]
    def do_replacements(string):
        for pattern, repl in zip(compiled_patterns, replacements):
            string = pattern.sub(repl, string)
        return string
    return [(h, do_replacements(e)) for h, e in headword_entry_list]


def read_file(in_path: str,
              headword_pattern: str,
              groupnum: int,
              encoding: str='utf-8') -> List[Tuple[str, str]]:
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
