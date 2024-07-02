NUMTYPES = {
    "koreanLegal": ['제{}조'.format(i) for i in range(1, 21)],
    "arabic": [str(i) for i in range(1, 21)],
    "decimal": [str(i) for i in range(1, 21)],
    "decimalEnclosedCircle": ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳'],
    "decimalEnclosedFullstop": ['{}.'.format(i) for i in range(1, 21)],
    "decimalEnclosedParen": ['({})'.format(i) for i in range(1, 21)],
    "decimalZero": ['{:02d}'.format(i) for i in range(1, 21)],
    "upperRoman": ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX'],
    "upperLetter": [chr(64+i) for i in range(1, 21)],
    "lowerRoman": ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx'],
    "lowerRomanFullStop": ['i.', 'ii.', 'iii.', 'iv.', 'v.', 'vi.', 'vii.', 'viii.', 'ix.', 'x.', 'xi.', 'xii.', 'xiii.', 'xiv.', 'xv.', 'xvi.', 'xvii.', 'xviii.', 'xix.', 'xx.'],
    "koreanChapter": ['제{}장'.format(i) for i in range(1, 21)],
    "koreanSection": ['제{}절'.format(i) for i in range(1, 21)]
}
