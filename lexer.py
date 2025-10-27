import ply.lex as lex
tokens = (
    'ID',        
    'NUMBER',
    'STRING',
    'IF',
    'ELSE',
    'DEF',
    'EQUALS',     # =
    'LPAREN',     # (
    'RPAREN',     # )
    'LBRACKET',   # [
    'RBRACKET',   # ]
    'LBRACE',     # {
    'RBRACE',     # }
    'COLON',      # :
    'COMMA',      # ,
    'PLUS',       # +
    'MINUS',      # -
    'TIMES',      # *
    'DIVIDE',     # /
    'GT',         # >
    'LT',         # <
    'EQEQ',       # ==
)
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
}
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GT = r'>'
t_LT = r'<'
t_EQEQ = r'=='
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_STRING(t):
    r'(\"[^\"]*\")|(\'[^\']*\')'
    t.value = t.value[1:-1]  
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
lexer = lex.lex()