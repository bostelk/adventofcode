"""
DAY 10
PART 1
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
class SyntaxError(Exception):
    def __init__(self, token, expected_token=None):
        message = None
        if token and expected_token:
            message = "expected '%s', but found '%s' instead." % (expected_token, token)
        elif token:
            message = "invalid token '%'" % token
        super(SyntaxError, self).__init__(message)
        self.token = token
        self.expected_token = expected_token
def parse_line(line):
    i = 0
    open_chunks = []
    while i < len(line):
        c = line[i]
        if c not in TOKENS:
            raise SyntaxError(c)
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
                    raise SyntaxError(c, expected_close_token)
            else:
                raise Exception("no chunk to close")
        else:
            raise Exception("unknown token: " + c)
        i += 1
syntax_error_score = 0
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        try:
            parse_line(line.strip())
        except Exception as e:
            print e
            syntax_error_score += ERROR_SCORE_TOKEN[e.token]
        line = file.readline()
    print("End of input")
print("Syntax error score = %s" % syntax_error_score)
