"""
Simple configuration object and example configurations for Wanano and Barasana.
Aggressive processing to remove all non-gloss information (examples, PoS, etc.) from entry.
"""


class Config:

    def __init__(self,
                 headword_pattern,
                 headword_group=0,
                 entry_postproc_patterns=tuple(),
                 entry_postproc_replacements=tuple(),
                 encoding='utf-8'):
        self.headword_pattern = headword_pattern
        self.headword_group = headword_group
        self.entry_postproc_patterns = entry_postproc_patterns
        self.entry_postproc_replacements = entry_postproc_replacements
        self.encoding = encoding

_capture_example_pattern = '\\s*[eE]j\\. .+?(\\d|$)'
_capture_example_replace = ' \\1'

_clean_beginning_pattern = '^\\W*'
_clean_beginning_replace = ''

_clean_end_pattern = '\\s*$'
_clean_end_replace = ''

_capture_phonetic_and_pos_pattern = '\\[.*?\\](,? *\\S*?\\. )?'
_capture_phonetic_and_pos_replace = ''

# Saved configurations. Add to this dict to enable simple command-line usage.
parameters = {
    'wanano': Config(
        headword_pattern='(^|\\n)(.+?)\\s*\\[',
        headword_group=2,
        entry_postproc_patterns=(
            '\\n',
            _capture_example_pattern,
            _capture_phonetic_and_pos_pattern,
            _clean_beginning_pattern,
            _clean_end_pattern,
        ),
        entry_postproc_replacements=(
            ' ',
            _capture_example_replace,
            _capture_phonetic_and_pos_replace,
            _clean_beginning_replace,
            _clean_end_replace,
        ),
        encoding='latin1'
    ),

    'barasana': Config(
        headword_pattern='(^|\\n)(.+?)\\s*\\[',
        headword_group=2,
        entry_postproc_patterns=(
            '\\n',
            _capture_example_pattern,
            _capture_phonetic_and_pos_pattern,
            _clean_beginning_pattern,
            _clean_end_pattern,
        ),
        entry_postproc_replacements=(
            ' ',
            _capture_example_replace,
            _capture_phonetic_and_pos_replace,
            _clean_beginning_replace,
            _clean_end_replace,
        ),
        encoding='utf-8'
    )
}
