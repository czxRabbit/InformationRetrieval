# Input: list of pairs < token , document id >
# Output: sorted list of pairs < token , document id >
# This component will perform sorting of the token list: first by tokens (alphabetical order), and then by
# document ids (since they are file paths, i.e. – strings, we use alphabetical order as well). Input to this
# component will be a concatenated list of tokens from all documents.


def Sort(tokens):
    tokens.sort(key=lambda element: (element[0], element[1]))
    return tokens
