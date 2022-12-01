"""
DAY 10
PART 2
"""
import sys
OPEN_TOKENS = [ '<', '{', '[', '(' ]
CLOSE_TOKENS = [ '>', '}', ']', ')' ]
TOKENS = OPEN_TOKENS + CLOSE_TOKENS
OPEN_TO_CLOSE_TOKEN = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
ERROR_SCORE_TOKEN = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
COMPLETE_SCORE_TOKEN = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
class SyntaxError(Exception):
    def __init__(self, token, expected_token=None, line_index=None):
        message = None
        if token and expected_token:
            message = "expected '%s', but found '%s' instead." % (expected_token, token)
        elif token:
            message = "invalid token '%'" % token
        super(SyntaxError, self).__init__(message)
        self.token = token
        self.expected_token = expected_token
        self.line_index = line_index
def parse_line(line):
    i = 0
    open_chunks = []
    while i < len(line):
        c = line[i]
        if c not in TOKENS:
            raise SyntaxError(c, line_index=i)
        # open chunk
        if c in OPEN_TOKENS:
            open_chunks.append(c)
        # close chunk
        elif c in CLOSE_TOKENS:
            if len(open_chunks) > 0:
                open_token = open_chunks.pop()
                expected_close_token = OPEN_TO_CLOSE_TOKEN[open_token]
                if c is expected_close_token:
                    pass
                else:
                    raise SyntaxError(c, expected_close_token, i)
            else:
                raise Exception("no chunk to close")
        else:
            raise Exception("unknown token: " + c)
        i += 1
    return open_chunks
complete_token_scores = []
syntax_error_score = 0
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        open_chunks = None
        try:
            open_chunks = parse_line(line.strip())
        except Exception as e:
            syntax_error_score += ERROR_SCORE_TOKEN[e.token]
        complete_chunks = []
        if not open_chunks:
            # failed to parse. syntax error.
            line = file.readline()
            continue
        while len(open_chunks) > 0:
            open_token = open_chunks.pop()
            expected_close_token = OPEN_TO_CLOSE_TOKEN[open_token]
            complete_chunks.append(expected_close_token)
        complete_token_score = 0
        for i in range(0, len(complete_chunks)):
            complete_token = complete_chunks[i]
            complete_token_score = 5 * complete_token_score + COMPLETE_SCORE_TOKEN[complete_token]
        complete_token_scores.append(complete_token_score)
        line = file.readline()
    print("End of input")
complete_token_scores = sorted(complete_token_scores)
middle_complete_score = complete_token_scores[len(complete_token_scores)/2]
print("Middle autocomplete score = %s" % middle_complete_score)
