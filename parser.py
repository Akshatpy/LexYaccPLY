# parser.py

import ply.yacc as yacc
from lexer import tokens

start = 'statement'

def p_statement(p):
    '''statement : variable_declaration
                 | if_else_statement
                 | function_definition
                 | expression
                 | list
                 | dictionary
    '''
    p[0] = p[1]

def p_variable_declaration(p):
    'variable_declaration : ID EQUALS value'
    p[0] = ('var_assign', p[1], p[3])

def p_value(p):
    '''value : expression
             | STRING
             | list
             | dictionary
             | NUMBER
             | ID
    '''
    p[0] = p[1]

def p_if_else_statement(p):
    '''if_else_statement : IF condition COLON statement ELSE COLON statement
                         | IF condition COLON statement
    '''
    if len(p) == 8:
        p[0] = ('if-else', p[2], p[4], p[7])
    else:
        p[0] = ('if', p[2], p[4])

def p_condition(p):
    '''condition : expression GT expression
                 | expression LT expression
                 | expression EQEQ expression
                 | expression
    '''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_function_definition(p):
    'function_definition : DEF ID LPAREN arg_list RPAREN COLON statement'
    p[0] = ('func_def', p[2], p[4], p[7])

def p_arg_list(p):
    '''arg_list : ID
                | ID COMMA arg_list
                | empty
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_list(p):
    'list : LBRACKET item_list RBRACKET'
    p[0] = ('list', p[2])

def p_item_list(p):
    '''item_list : value
                 | value COMMA item_list
                 | empty
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_dictionary(p):
    'dictionary : LBRACE pair_list RBRACE'
    p[0] = ('dict', p[2])

def p_pair_list(p):
    '''pair_list : pair
                 | pair COMMA pair_list
                 | empty
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_pair(p):
    '''pair : STRING COLON value
            | NUMBER COLON value
    '''
    p[0] = (p[1], p[3])

def p_expression(p):
    '''expression : term PLUS term
                  | term MINUS term
                  | term
    '''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : factor TIMES factor
            | factor DIVIDE factor
            | factor
    '''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN
    '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]
        
def p_empty(p):
    'empty :'
    pass
def p_error(p):
    if p:
        message = f"Syntax error at token '{p.value}' (type: {p.type})"
    else:
        message = "Syntax error at end of input"
    raise SyntaxError(message)

parser = yacc.yacc()