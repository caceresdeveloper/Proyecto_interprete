import ply.lex as lex
import ply.yacc as yacc
import re
import subprocess


# Lista de nombres de tokens
tokens = [
    'IDENTIFIER',
    'INTEGER',
    'STRING',
    'SYMBOL',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_OR_EQUAL',
    'GREATER_THAN_OR_EQUAL',
    'AND',
    'OR',
    'NOT',
    'ASSIGN',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'COMMENT',
    'KEYWORD',
    'CONTROL_KEYWORD',
    'METHOD_KEYWORD',
    'CLASS_KEYWORD',
    'ATTR_KEYWORD',
    'CODE_BLOCK',
    'METHOD_CALL',
]

# Definición de patrones para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_OR_EQUAL = r'<='
t_GREATER_THAN_OR_EQUAL = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_ignore = ' \t'

# Patrones con funciones
def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    t.type = 'IDENTIFIER'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    return t

def t_SYMBOL(t):
    r':[a-zA-Z_]\w*'
    return t

def t_KEYWORD(t):
    r'\b(alias|and|BEGIN)\b'
    return t

def t_CONTROL_KEYWORD(t):
    r'\b(if|else|elsif)\b'
    return t

def t_METHOD_KEYWORD(t):
    r'\b(def|end)\b'
    return t

def t_CLASS_KEYWORD(t):
    r'\b(class|module)\b'
    return t

def t_ATTR_KEYWORD(t):
    r'\b(attr_reader|attr_writer)\b'
    return t

def t_CODE_BLOCK(t):
    r'\b(do|end|{|\})\b'
    return t

def t_METHOD_CALL(t):
    r'[a-zA-Z_]\w*\.[a-zA-Z_]\w*'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_whitespace(t):
    r'[ \t]+'
    pass

def t_error(t):
    print(f"Caracter no válido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Reglas de gramática para el analizador sintáctico
def p_program(p):
    '''
    program : statement_list
    '''
    print("Programa válido")

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement statement_list
    '''

def p_statement(p):
    '''
    statement : expression SEMICOLON
              | method_definition
              | if_statement
              | code_block
              | COMMENT
    '''

def p_method_definition(p):
    '''
    method_definition : METHOD_KEYWORD IDENTIFIER LEFT_PAREN IDENTIFIER RIGHT_PAREN code_block
    '''

def p_if_statement(p):
    '''
    if_statement : CONTROL_KEYWORD expression code_block
                 | CONTROL_KEYWORD expression code_block else_statement
    '''

def p_else_statement(p):
    '''
    else_statement : CONTROL_KEYWORD code_block
                   | empty
    '''

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_code_block(p):
    '''
    code_block : CODE_BLOCK
               | LEFT_BRACE statement_list RIGHT_BRACE
    '''

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_expression(p):
    '''
    expression : IDENTIFIER
               | INTEGER
               | STRING
               | expression PLUS expression
               | expression MINUS expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression EQUALS expression
               | expression NOT_EQUALS expression
               | expression LESS_THAN expression
               | expression GREATER_THAN expression
               | expression LESS_THAN_OR_EQUAL expression
               | expression GREATER_THAN_OR_EQUAL expression
               | expression AND expression
               | expression OR expression
               | NOT expression
               | IDENTIFIER ASSIGN expression
               | LEFT_PAREN expression RIGHT_PAREN
               | method_call
               | SYMBOL
    '''

def p_method_call(p):
    '''
    method_call : IDENTIFIER DOT IDENTIFIER LEFT_PAREN RIGHT_PAREN
    '''

def p_error(p):
    if p:
        token_value = p.value
        print(f"Error de sintaxis en el token '{token_value}'")
        with open("Sintaxico.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Error de sintaxis en el token '{token_value}'\n")
    else:
        print("Error de sintaxis en la entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare_variable(self, name, var_type):
        self.symbols[name] = var_type

    def check_variable(self, name):
        if name not in self.symbols:
            print(f"Error semantico: Variable '{name}' no declarada.")

# Crear una tabla de símbolos
symbol_table = SymbolTable()

def ejecutar_codigo_desde_archivo(Codigo):
    try:
        # Abre el archivo de texto en modo lectura
        with open(Codigo, 'r') as file:
            # Lee el contenido del archivo
            codigo = file.read()

        # Ejecuta el código leído desde el archivo
        lexer = lex.lex()
        lexer.input(codigo)
        
        # Guarda el código Ruby en un archivo temporal
        with open("codigo_ruby.rb", "w") as archivo4:
            archivo4.write(codigo)

        proceso = subprocess.Popen(["ruby", "codigo_ruby.rb"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida, errores = proceso.communicate()

        print("Salida:")
        print(salida)

        # Guarda la salida en un archivo de texto
        with open("salida.txt", "w") as archivo_salida:
            archivo_salida.write(salida)

        print("Errores:")
        print(errores)
        
        # Abre un archivo llamado "Analizador_Lexico.txt" en modo escritura con codificación utf-8
        with open("Analizador_Lexico.txt", "w", encoding="utf-8") as archivo:
            for token in lexer:
                print("Token:", token.value, "Tipo:", token.type)
                resultado = f"Token: {token.value}, Tipo: {token.type}"
                # Escribe el resultado en el archivo
                archivo.write(resultado + "\n")
        
        parser.parse(codigo, lexer=lexer)
        
        # Analizador semántico
        symbol_table = SymbolTable()
        lines = codigo.split('\n')
        for line in lines:
            if line.strip().startswith('def '):
                # Declaración de una función
                func_name = line.strip().split(' ')[1].split('(')[0]
                symbol_table.declare_variable(func_name, 'FUNCTION')
            elif line.strip().startswith('tiempo = '):
                # Declaración de una variable
                variable_name = line.strip().split('=')[0].strip()
                symbol_table.declare_variable(variable_name, 'INTEGER')

        # Analizar uso de variables y funciones
        for line in lines:
            if '(' in line and ')' in line:
                # Llamada a una función
                func_name = line.strip().split('(')[0]
                if func_name in symbol_table.symbols:
                    args = line.strip().split('(')[1].split(')')[0].split(',')
                    for arg in args:
                        arg = arg.strip()
                        if arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit()):
                            symbol_table.check_variable(arg)
                        elif arg.isalpha():
                            symbol_table.check_variable(arg)
                        else:
                            print(f"Error semantico: Uso no valido de '{arg}' en '{line.strip()}'.")
        
        # Mostrar resultado de la tabla de símbolos
        with open("Semantico.txt", "w", encoding="utf-8") as archivo3:
            print("\nTabla de simbolos:")
            for symbol, var_type in symbol_table.symbols.items():
                print(f"{symbol}: {var_type}")
                resultado2 = f"{symbol}: {var_type}"
                archivo3.write(resultado + "\n")

            print("\nAnalisis semantico completo.")
            finalizacion = (f"\nAnalisis semantico completo.")
            archivo3.write(finalizacion)
                
        
    except FileNotFoundError:
        print(f"El archivo '{Codigo}' no se encontró.")
    except Exception as e:
        print(f"Error al ejecutar el código desde '{Codigo}': {str(e)}")
    except Exception as e:
        print("Ocurrió un error:", str(e))


if __name__ == "__main__":
    # Nombre del archivo que contiene el código a ejecutar
    nombre_archivo = 'Codigo.txt'  # Cambia aquí el nombre del archivo que deseas ejecutar

    # Ejecutar el código desde el archivo
    ejecutar_codigo_desde_archivo(nombre_archivo)
    
