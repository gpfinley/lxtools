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

# Saved configurations. Add to this dict to enable simple command-line usage.
parameters = {
    'wanano': Config(
        headword_pattern='(^|\\n)(.+?)\\s*\\[',
        headword_group=2,
        entry_postproc_patterns=(
            '\\n',
            '\\s*[eE]j\\. .+?(\\d|$)'     # remove example from entry
        ),
        entry_postproc_replacements=(
            ' ',
            ' \\1'
        ),
        encoding='latin1'
    ),

    'barasana': Config(
        headword_pattern='(^|\\n)(.+?)\\s*\\[',
        headword_group=2,
        entry_postproc_patterns=(
            '\\n',
            '\\s*[eE]j\\. .+?(\\d|$)'     # remove example from entry
        ),
        entry_postproc_replacements=(
            ' ',
            ' \\1'
        ),
        encoding='utf-8'
    )
}
