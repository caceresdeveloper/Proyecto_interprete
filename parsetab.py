
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEAND ASSIGN COMMA COMMENT CONTROL_KEYWORD DIVIDE DOT EQUALS FUNCTION_KEYWORD GREATER_THAN GREATER_THAN_OR_EQUAL IDENTIFIER INTEGER KEYWORD LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS_THAN LESS_THAN_OR_EQUAL MINUS MULTIPLY NOT NOT_EQUALS OR PLUS RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN SEMICOLON STRING SYMBOL\n    program : statement_list\n    \n    statement_list : statement\n                   | statement statement_list\n    \n    statement : expression SEMICOLON\n              | function_definition\n              | if_statement\n              | code_block\n              | COMMENT\n    \n    function_definition : FUNCTION_KEYWORD IDENTIFIER LEFT_PAREN argument_list RIGHT_PAREN code_block\n    \n    argument_list : IDENTIFIER\n                 | IDENTIFIER COMMA argument_list\n                 | empty\n    \n    if_statement : CONTROL_KEYWORD expression code_block\n                 | CONTROL_KEYWORD expression code_block else_statement\n    \n    else_statement : CONTROL_KEYWORD code_block\n                   | empty\n    \n    empty :\n    \n    code_block : LEFT_BRACE statement_list RIGHT_BRACE\n    \n    expression : IDENTIFIER\n               | INTEGER\n               | STRING\n               | expression PLUS expression\n               | expression MINUS expression\n               | expression MULTIPLY expression\n               | expression DIVIDE expression\n               | expression EQUALS expression\n               | expression NOT_EQUALS expression\n               | expression LESS_THAN expression\n               | expression GREATER_THAN expression\n               | expression LESS_THAN_OR_EQUAL expression\n               | expression GREATER_THAN_OR_EQUAL expression\n               | expression AND expression\n               | expression OR expression\n               | NOT expression\n               | IDENTIFIER ASSIGN expression\n               | LEFT_PAREN expression RIGHT_PAREN\n    '
    
_lr_action_items = {'COMMENT':([0,3,5,6,7,8,16,18,52,53,58,59,62,64,],[8,8,-5,-6,-7,-8,8,-4,-13,-18,-14,-16,-15,-9,]),'IDENTIFIER':([0,3,5,6,7,8,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,51,52,53,58,59,60,62,64,],[9,9,-5,-6,-7,-8,9,9,34,9,9,-4,9,9,9,9,9,9,9,9,9,9,9,9,9,54,-13,-18,-14,-16,54,-15,-9,]),'INTEGER':([0,3,5,6,7,8,12,13,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,53,58,59,62,64,],[10,10,-5,-6,-7,-8,10,10,10,10,-4,10,10,10,10,10,10,10,10,10,10,10,10,10,-13,-18,-14,-16,-15,-9,]),'STRING':([0,3,5,6,7,8,12,13,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,53,58,59,62,64,],[11,11,-5,-6,-7,-8,11,11,11,11,-4,11,11,11,11,11,11,11,11,11,11,11,11,11,-13,-18,-14,-16,-15,-9,]),'NOT':([0,3,5,6,7,8,12,13,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,53,58,59,62,64,],[12,12,-5,-6,-7,-8,12,12,12,12,-4,12,12,12,12,12,12,12,12,12,12,12,12,12,-13,-18,-14,-16,-15,-9,]),'LEFT_PAREN':([0,3,5,6,7,8,12,13,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,52,53,58,59,62,64,],[13,13,-5,-6,-7,-8,13,13,13,13,-4,13,13,13,13,13,13,13,13,13,13,13,13,13,51,-13,-18,-14,-16,-15,-9,]),'FUNCTION_KEYWORD':([0,3,5,6,7,8,16,18,52,53,58,59,62,64,],[14,14,-5,-6,-7,-8,14,-4,-13,-18,-14,-16,-15,-9,]),'CONTROL_KEYWORD':([0,3,5,6,7,8,16,18,52,53,58,59,62,64,],[15,15,-5,-6,-7,-8,15,-4,57,-18,-14,-16,-15,-9,]),'LEFT_BRACE':([0,3,5,6,7,8,9,10,11,16,18,32,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,57,58,59,61,62,64,],[16,16,-5,-6,-7,-8,-19,-20,-21,16,-4,-34,16,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,-13,-18,16,-14,-16,16,-15,-9,]),'$end':([1,2,3,5,6,7,8,17,18,52,53,58,59,62,64,],[0,-1,-2,-5,-6,-7,-8,-3,-4,-13,-18,-14,-16,-15,-9,]),'RIGHT_BRACE':([3,5,6,7,8,17,18,36,52,53,58,59,62,64,],[-2,-5,-6,-7,-8,-3,-4,53,-13,-18,-14,-16,-15,-9,]),'SEMICOLON':([4,9,10,11,32,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[18,-19,-20,-21,-34,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,]),'PLUS':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[19,-19,-20,-21,19,19,19,-22,-23,-24,-25,19,19,19,19,19,19,19,19,19,-36,]),'MINUS':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[20,-19,-20,-21,20,20,20,-22,-23,-24,-25,20,20,20,20,20,20,20,20,20,-36,]),'MULTIPLY':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[21,-19,-20,-21,21,21,21,21,21,-24,-25,21,21,21,21,21,21,21,21,21,-36,]),'DIVIDE':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[22,-19,-20,-21,22,22,22,22,22,-24,-25,22,22,22,22,22,22,22,22,22,-36,]),'EQUALS':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[23,-19,-20,-21,23,23,23,-22,-23,-24,-25,23,23,23,23,23,23,23,23,23,-36,]),'NOT_EQUALS':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[24,-19,-20,-21,24,24,24,-22,-23,-24,-25,24,24,24,24,24,24,24,24,24,-36,]),'LESS_THAN':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[25,-19,-20,-21,25,25,25,-22,-23,-24,-25,25,25,25,25,25,25,25,25,25,-36,]),'GREATER_THAN':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[26,-19,-20,-21,26,26,26,-22,-23,-24,-25,26,26,26,26,26,26,26,26,26,-36,]),'LESS_THAN_OR_EQUAL':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[27,-19,-20,-21,27,27,27,-22,-23,-24,-25,27,27,27,27,27,27,27,27,27,-36,]),'GREATER_THAN_OR_EQUAL':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[28,-19,-20,-21,28,28,28,-22,-23,-24,-25,28,28,28,28,28,28,28,28,28,-36,]),'AND':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[29,-19,-20,-21,29,29,29,-22,-23,-24,-25,29,29,29,29,29,29,29,29,29,-36,]),'OR':([4,9,10,11,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[30,-19,-20,-21,30,30,30,-22,-23,-24,-25,30,30,30,30,30,30,30,30,30,-36,]),'RIGHT_PAREN':([9,10,11,32,33,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,60,63,],[-19,-20,-21,-34,50,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,-17,-10,61,-12,-17,-11,]),'ASSIGN':([9,],[31,]),'COMMA':([54,],[60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,3,16,],[2,17,36,]),'statement':([0,3,16,],[3,3,3,]),'expression':([0,3,12,13,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,],[4,4,32,33,35,4,37,38,39,40,41,42,43,44,45,46,47,48,49,]),'function_definition':([0,3,16,],[5,5,5,]),'if_statement':([0,3,16,],[6,6,6,]),'code_block':([0,3,16,35,57,61,],[7,7,7,52,62,64,]),'argument_list':([51,60,],[55,63,]),'empty':([51,52,60,],[56,59,56,]),'else_statement':([52,],[58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','julia_interprete.py',123),
  ('statement_list -> statement','statement_list',1,'p_statement_list','julia_interprete.py',129),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','julia_interprete.py',130),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','julia_interprete.py',135),
  ('statement -> function_definition','statement',1,'p_statement','julia_interprete.py',136),
  ('statement -> if_statement','statement',1,'p_statement','julia_interprete.py',137),
  ('statement -> code_block','statement',1,'p_statement','julia_interprete.py',138),
  ('statement -> COMMENT','statement',1,'p_statement','julia_interprete.py',139),
  ('function_definition -> FUNCTION_KEYWORD IDENTIFIER LEFT_PAREN argument_list RIGHT_PAREN code_block','function_definition',6,'p_function_definition','julia_interprete.py',144),
  ('argument_list -> IDENTIFIER','argument_list',1,'p_argument_list','julia_interprete.py',149),
  ('argument_list -> IDENTIFIER COMMA argument_list','argument_list',3,'p_argument_list','julia_interprete.py',150),
  ('argument_list -> empty','argument_list',1,'p_argument_list','julia_interprete.py',151),
  ('if_statement -> CONTROL_KEYWORD expression code_block','if_statement',3,'p_if_statement','julia_interprete.py',156),
  ('if_statement -> CONTROL_KEYWORD expression code_block else_statement','if_statement',4,'p_if_statement','julia_interprete.py',157),
  ('else_statement -> CONTROL_KEYWORD code_block','else_statement',2,'p_else_statement','julia_interprete.py',162),
  ('else_statement -> empty','else_statement',1,'p_else_statement','julia_interprete.py',163),
  ('empty -> <empty>','empty',0,'p_empty','julia_interprete.py',168),
  ('code_block -> LEFT_BRACE statement_list RIGHT_BRACE','code_block',3,'p_code_block','julia_interprete.py',174),
  ('expression -> IDENTIFIER','expression',1,'p_expression','julia_interprete.py',184),
  ('expression -> INTEGER','expression',1,'p_expression','julia_interprete.py',185),
  ('expression -> STRING','expression',1,'p_expression','julia_interprete.py',186),
  ('expression -> expression PLUS expression','expression',3,'p_expression','julia_interprete.py',187),
  ('expression -> expression MINUS expression','expression',3,'p_expression','julia_interprete.py',188),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','julia_interprete.py',189),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','julia_interprete.py',190),
  ('expression -> expression EQUALS expression','expression',3,'p_expression','julia_interprete.py',191),
  ('expression -> expression NOT_EQUALS expression','expression',3,'p_expression','julia_interprete.py',192),
  ('expression -> expression LESS_THAN expression','expression',3,'p_expression','julia_interprete.py',193),
  ('expression -> expression GREATER_THAN expression','expression',3,'p_expression','julia_interprete.py',194),
  ('expression -> expression LESS_THAN_OR_EQUAL expression','expression',3,'p_expression','julia_interprete.py',195),
  ('expression -> expression GREATER_THAN_OR_EQUAL expression','expression',3,'p_expression','julia_interprete.py',196),
  ('expression -> expression AND expression','expression',3,'p_expression','julia_interprete.py',197),
  ('expression -> expression OR expression','expression',3,'p_expression','julia_interprete.py',198),
  ('expression -> NOT expression','expression',2,'p_expression','julia_interprete.py',199),
  ('expression -> IDENTIFIER ASSIGN expression','expression',3,'p_expression','julia_interprete.py',200),
  ('expression -> LEFT_PAREN expression RIGHT_PAREN','expression',3,'p_expression','julia_interprete.py',201),
]
