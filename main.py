from lexer import lexer
from parser import parser
while True:
    try:
        data = input("Enter Python construct > ")
    except EOFError:
        break
    if not data:
        continue
    parsed = parser.parse(data, lexer=lexer)
    if parsed is not None:
        print("Accepted\n")