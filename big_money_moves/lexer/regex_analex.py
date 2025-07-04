import ply.lex as lex

tokens = (
    'EXCEPTOPTS', 
    'EXCEPTCAPTURE', 'EXCEPTLOOKAHEADPOS', 'EXCEPTLOOKAHEADNEG', 'EXCEPTLOOKBEHINDPOS', 'EXCEPTLOOKBEHINDNEG', 'START', 'END', 
    'WILDCARD', 'OR', 'LPARENTHESIS', 'RPARENTHESIS', 'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY', 'NULORMANY', 'ONEORMANY', 
    'NULORONE', 'COMMA', 'COLON', 
    'MINUS', 
    #'EQUALS', 
    'BARSS', 'BARLS', 'BARSW', 'BARLW', 'BARSD', 'BARLD', 
    'BART', 'BARN', 'SPACE', 'LITERALBAR', 'CHAR',
    'LITERAL_ESCAPE', 'NUMBER',
    #'OPTIONAL',
    #'EXCEPTION',
)


def t_EXCEPTOPTS(t):
    r'\[\^'
    return t

def t_LBRACKET(t):
    r'\['
    t.lexer.INCLASS = True
    return t

#def t_OPTIONAL(t):
#    r'(?<=\[).*?(?=\])'
#    return t

#def t_EXCEPTION(t):
#    r'(?<=\[\^).*(?=\])'
#    return t


def t_RBRACKET(t):
    r'\]'
    t.lexer.INCLASS = False
    return t

def t_EXCEPTCAPTURE(t):
    r'\?\:'
    return t

def t_EXCEPTLOOKAHEADPOS(t):
    r'\?='
    return t

def t_EXCEPTLOOKAHEADNEG(t):
    r'\?!'
    return t

def t_EXCEPTLOOKBEHINDPOS(t):
    r'\?<='
    return t

def t_EXCEPTLOOKBEHINDNEG(t):
    r'\?<!'
    return t

def t_START(t):
    r'\^'
    return t

def t_END(t):
    r'\$'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_LITERAL_ESCAPE(t):
    r'\\\.'
    t.type = 'CHAR'
    t.value = '.'
    return t

def t_WILDCARD(t):
    r'\.'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_OR(t):
    r'\|'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_LPARENTHESIS(t):
    r'\('
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_RPARENTHESIS(t):
    r'\)'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_LCURLY(t):
    r'\{'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_NUMBER(t):
    r'\d+'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    else:
        t.value = int(t.value)
    return t

def t_RCURLY(t):
    r'\}'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_NULORMANY(t):
    r'\*'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_ONEORMANY(t):
    r'\+'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_NULORONE(t):
    r'(?<!\|)\?(?![\+\*\{])'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_COMMA(t):
    r','
    return t

def t_COLON(t):
    r'\:'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_MINUS(t):
    r'-'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

#def t_EQUALS(t):
#    r'='
#    return t

def t_BARSS(t):
    r'\\s'
    return t

def t_BARLS(t):
    r'\\S'
    return t

def t_BARSW(t):
    r'\\w'
    if t.lexer.INCLASS:
        t.type = 'CHAR'
    return t

def t_BARLW(t):
    r'\\W'
    return t

def t_BARSD(t):
    r'\\d'
    return t

def t_BARLD(t):
    r'\\D'
    return t

def t_BART(t):
    r'\\t'
    return t

def t_BARN(t):
    r'\\n'
    return t

def t_SPACE(t):
    r'\ '
    return t

def t_LITERALBAR(t):
    r'\\'
    return t

def t_CHAR(t):
    r'.'
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.INCLASS = False

#input_code = "S[^l(mk)+]a"
#lexer.input(input_code)

#for tok in lexer:
#    print(f"Value: {tok.value}, Token: {tok.type}, Position: {tok.lexpos}")