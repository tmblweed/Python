def braces_combinations(output, open_brace, close_brace, pairs):
"""for each combination, you cannot have more open braces than number of pairs or more closed than open"""
    if open_brace == pairs and close_brace == pairs:
        print output
    else:
        if open_brace<pairs:
            braces_combinations(output+'(', open_brace+1, close_brace, pairs)
        if close_brace<pairs: #you want every closed brace to have an open brace
            braces_combinations(output+')', open_brace, close_brace+1, pairs)

braces_combinations('', 0, 0, 3)
