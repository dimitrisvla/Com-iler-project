from sys import argv
# We need two parameters because we'll get file name from command line.
script, filename = argv 

# Every token we'll extract will have an int as a specific id
########################################################################################################
# Operators:
Op_add, Op_sub, Op_multi, Op_div, Op_equal, Op_not_equal, \
Op_less, Op_less_equal, Op_greater, Op_greater_equal, Op_assign = range(11)

# Symbols:
Left_bracket, Right_bracket, Left_paren, Right_paren, Left_brace, Right_brace, \
Semicolon, Comma, Colon, Dot = range(11,21)

# Keywords:
Keyword_program, Keyword_declare, \
Keyword_if, Keyword_else, Keyword_while, \
Keyword_switchcase, Keyword_forcase, Keyword_incase, Keyword_case, Keyword_default, \
Keyword_not, Keyword_and, Keyword_or, \
Keyword_function, Keyword_procedure, Keyword_call, Keyword_return, Keyword_in, Keyword_inout, \
Keyword_input, Keyword_print = range(21,42)

# Others:
Comment, Integer, Identifier = range(42,45)
Keyword_eof = 45

# Set max integer
Max_Integer = 4294967295

[place, true, false] = range(3)
########################################################################################################

########################################################################################################
key_words = { 'program': Keyword_program, 'declare': Keyword_declare,
             'if': Keyword_if, 'else': Keyword_else, 'while': Keyword_while,
              'switchcase': Keyword_switchcase, 'forcase': Keyword_forcase, 'incase': Keyword_incase, 
               'case': Keyword_case, 'default': Keyword_default, 
                'not': Keyword_not, 'and': Keyword_and, 'or': Keyword_or,
                'function': Keyword_function, 'procedure': Keyword_procedure, 'call': Keyword_call,
                 'return': Keyword_return, 'in': Keyword_in, 'inout': Keyword_inout,
                 'input': Keyword_input, 'print': Keyword_print }


arithmetic_operators = { '*': Op_multi, '/': Op_div, '+': Op_add, '-': Op_sub }


symbols = { '[': Left_bracket, ']': Right_bracket, '(': Left_paren, ')': Right_paren, 
           '{': Left_brace, '}': Right_brace, ',': Comma, ';': Semicolon, '.': Dot }

relational_operators = [ Op_equal, Op_not_equal, Op_less, Op_less_equal, Op_greater,
                        Op_greater_equal ]

statement_cases = [ Keyword_if, Keyword_while, Keyword_switchcase, Keyword_forcase,
                   Keyword_incase, Keyword_call, Keyword_return, Keyword_input,
                   Keyword_print, Identifier ]

########################################################################################################

#################################################################################
token = ''
list_of_tokens  = []   # initialize an empty list in which we'll store our tokens
list_index = 0         # index of every token
my_character = ' '     # initialize to an empty 1st character
line = 1               # we must count our lines
#################################################################################


label_of_quad = 0
list_of_quads = []
number_of_temporary = 0

list_of_variables = []
program_name = ''

list_of_scopes = []

return_flag = False

list_of_quads_asm = []
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
# lexycal analysis starts here.
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

#---------------------------------------------------------------------#
# Produces the next character in each iteration & checks for new lines
#---------------------------------------------------------------------#
def read_next_char():
    global line, my_character
 
    my_character = input_file.read(1)

    if my_character == '\n':
        line += 1
    return my_character


#-------------------#
# Check if '>', '>='
#-------------------#
def start_with_greater():
  global list_index, token

  next_char = read_next_char()
  if(next_char == '='):
    id = Op_greater_equal
    str = '>='
    #print(f"Line {line} Token id is {id} and token is {str}.")
    token = str
    return id
  else:
    id = Op_greater
    str = '>'
    #print(f"Line {line}: Token id is {id} and token is {str}.")
    token = str
    input_file.seek(input_file.tell()-1, 0)
    return id


#------------------------#
# Check if '<', '<=', '<>'
#------------------------#
def start_with_less():
  global list_index, id_token, token

  next_char = read_next_char()
  if(next_char == '='):
    id = Op_less_equal
    str = '<='
    #print(f"Line {line} Token id is {id} and token is {str}.")
    token = str
    return id
  elif(next_char == '>'):
    id = Op_not_equal
    str = '<>'
    #print(f"Line {line} Token id is {id} and token is {str}.")
    token = str
    return id
  else:
    id = Op_less
    str = '<'
    #print(f"Line {line} Token id is {id} and token is {str}.")
    token = str
    input_file.seek(input_file.tell()-1, 0)
    return id


#-----------------------------#
# Check if a comment is closed
#-----------------------------#
def comment():  
  temp_char = read_next_char()
  temp_line = line
  # now we are inside a comment
  while True:
    if temp_char == '#':  # comment closed
      #print(f"Comment opened in line {temp_line} closed.")
      return produce_token()
    elif temp_char == '':
      #print(f"Error: Comment opened in line {temp_line} did not close.")
      exit(1) 
    else:
      temp_char = read_next_char()


#----------------------------------------#
# Check if keyword integer or identifier
#----------------------- ----------------#
def key_int_id():
  global line, token

  tok = ""   
  if my_character.isalpha(): 
    while my_character.isalpha() or my_character.isdigit():
      tok += my_character
      read_next_char()
  elif my_character.isdigit():
    while my_character.isdigit():
      tok += my_character
      read_next_char()
    if my_character.isalpha():
      print(f"Error :Line {line}.\nToken '{tok}' is not a number.")
      exit(1)
  else:
    print(f"Line {line}: Unknown character {my_character}.")
    exit(1)
  if len(tok) > 30:
      print(f"Error: Line {line}.\nToken '{tok}' is too big.")
      exit(0)
  
  input_file.seek(input_file.tell()-1, 0)      
  
  if my_character == '\n':
      line -= 1
  # Case 1 : Keyword.
  if tok in key_words:
    #print(f"Line {line}. Token id is {key_words[tok]} and token is {tok}.")
    token = tok
    return key_words[tok] 
  # Case 2 : Number or Error
  elif tok[0].isdigit():
    if int(tok) > Max_Integer :
      #print(f"Error: Line {line}.\nNumber '{tok}' is too large.")
      #print(f"Hint: numbers must be between -4294967295 and 4294967295.")
      exit(1)
    else:
      #print(f"Line {line}: Token id is {Integer} and token is {int(tok)}.")
      token = tok
      return Integer #, int(tok) 
  else:# Case 3 : Identifier. Warning: We will need the id type !!!
    #print(f"Line {line}: Token id is {Identifier} and token is {tok}.")
    token = tok
    return Identifier #, tok


#------------------------------------------#
# Produces the next token in each iteration
#------------------------------------------#
def produce_token():
  global list_index, token
  
  read_next_char()
  while my_character.isspace():  # ignore whitespace characters
    read_next_char()

  if my_character == '':
      return Keyword_eof
  elif my_character in arithmetic_operators:
    id = arithmetic_operators[my_character]
    #print(f"Line {line}: Token id is {arithmetic_operators[my_character]} and token is {my_character}.")
    token = my_character
    
    return id
  elif my_character in symbols:
    id = symbols[my_character]
    #print(f"Line {line}: Token id is {symbols[my_character]} and token is {my_character}.")
    token = my_character
    return id
  elif my_character == ':':
    if read_next_char() == '=':
      id = Op_assign
      my_char = ":="
      #print(f"Line {line}: Token id is {Op_assign} and token is {my_char}.")
      token = my_char
      return id
    else:
      #print(f" Error: Line {line}.\n \t After symbol ':' symbol '='' expected (Assignment symbol ':=').")
      exit(1)
  elif my_character == '=':
      id = Op_equal
      #print(f"Line {line}: Token id is {Op_equal} and token is {my_character}.")
      token = my_character
      return id
  elif my_character == '#':
    comment()
  elif my_character == '>':
    return start_with_greater()
  elif my_character == '<':
    return start_with_less()
  else:
    return key_int_id()



#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
# Syntax analysis starts here.
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

# 1
def program():
  global id_token, list_index, token, program_name

  id_token = produce_token()
  if id_token == Keyword_program:
    id_token = produce_token()
    if id_token == Identifier:
      program_name = token
      insertScope(program_name)
      id_token = produce_token()
      block(program_name)  # 2
      if id_token == Dot:
        print(f"End of program")
      else:
        print(f"Error :Line {line}.\nA program in C-imple must end with '.'.")
        exit(1)
    else:
      print(f"Error :Line {line}.\nName of the program is invalid.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nA program in C-imple must start with the keyword 'program'.")
    exit(1)



# 2
def block(block_name):
  global id_token, list_index, program_name, list_of_scopes, return_flag
  
  if id_token == Left_brace:
    id_token = produce_token()
    declarations()        # 3
    subprograms()
    
    if block_name != program_name:
      list_of_scopes[1][3][-1][2] = nextquad()

    genquad("begin block", block_name, "_", "_")  
    return_flag = False
    blockstatements()     # 9         
    if block_name == program_name:
      genquad("halt", "_", "_", "_")
    genquad("end block", block_name, "_", "_")
    
   
    if block_name != program_name:
      if return_flag == False:
        type = list_of_scopes[1][3][-1][1]
        if type == "func":
          print(f"Error :Line {line}.\nA function must have a return.")
          exit(1)
          
      list_of_scopes[1][3][-1][3] = list_of_scopes[0][2]
    deleteScope()
    if id_token == Right_brace:
      id_token = produce_token()  
    else:
      print(f"Error :Line {line}.\nA program block in C-imple must end with right brace.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nA program block in C-imple must start with left brace.")
    exit(1)
      
'''  
  functions()           # 5
  procedures()          # 6
  blockstatements()     # 9
''' 


# 3
def declarations():
  global id_token, list_index

  while(id_token == Keyword_declare):
    id_token = produce_token()
    varlist()  # 4
    if id_token == Semicolon:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nDeclaration of variables must end with ';' If a variable is not the last one ',' is expected.")
      exit(1)



# 4
def varlist():
  global id_token, list_index, list_of_variables, token

  if id_token == Identifier: # the variable list declaration is not necessary
    
    list_of_variables.append(token)
    insertEntity(createVariable(token))
    id_token = produce_token()
    while(id_token == Comma):
      id_token = produce_token()
      if id_token == Identifier:
    
        list_of_variables.append(token)
        insertEntity(createVariable(token))
        id_token = produce_token()
      else:
        print(f"Error :Line {line}.\nVariable name is invalid.")
        exit(1)

  


def subprograms():
  global id_token
  
  while id_token == Keyword_function or id_token == Keyword_procedure:
      if id_token == Keyword_function:
        functions()
      else:
        procedures()
# 5
def functions():
  global id_token, list_index, token

  id_token = produce_token()
  if id_token == Identifier:
    block_name = token
    insertEntity(createFuncProc(block_name, "func"))
    insertScope(block_name)
    id_token = produce_token()
    if id_token == Left_paren:
      id_token = produce_token()
      formalparlist()
      if id_token == Right_paren:
        id_token = produce_token()
        block(block_name)  # return to block
      else:
        print(f"Error :Line {line}.\nSymbol ')' expected.")
        exit(1)
    else:
      print(f"Error :Line {line}.\nSymbol '(' expected.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nInvalid function name.")
    exit(1)



# 6
def procedures():
  global id_token, token

  id_token = produce_token()
  if id_token == Identifier:
    block_name = token
    insertEntity(createFuncProc(block_name, "proc"))
    insertScope(block_name)
    id_token = produce_token()
    if id_token == Left_paren:
      id_token = produce_token()
      formalparlist()
      if id_token == Right_paren:
        id_token = produce_token()
        block(block_name)  # return to block
      else:
        print(f"Error :Line {line}.\nSymbol ')' expected.")
        exit(1)
    else:
      print(f"Error :Line {line}.\nSymbol '(' expected.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nInvalid procedure name.")
    exit(1)


# 7
def formalparlist():
  global id_token

  if id_token == Keyword_in  or id_token == Keyword_inout:
    formalparitem()
    while id_token == Comma:  # if there is not a comma function formalparitem is not used
      id_token = produce_token()
      formalparitem()



# 8
def formalparitem():
  global id_token

  if id_token == Keyword_in:
    id_token = produce_token()
    if id_token == Identifier:
      insertEntity(createParameter(token, "CV"))
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nA by value id(name) was expected.")
      exit(1)
  elif id_token == Keyword_inout:
    id_token = produce_token()
    if id_token == Identifier:
      insertEntity(createParameter(token, "REF"))
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nA by reference id(name) was expected.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nKeywords 'in' or 'inout' was expected.")
    exit(1)



# 9
def statements():
  global id_token

  if id_token == Left_brace:
    id_token = produce_token()
    statement()  # we'll have at least 1 more statement inside the braces
    while id_token == Semicolon:
      id_token = produce_token()
      statement()
    if id_token == Right_brace:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nRight brace is expected after the end of statements.")
      exit(1)
  # we'll have 10 cases for statements
  else:
    statement()  # After the 1st statement we need ';'
    if id_token == Semicolon:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nSymbol ';' was expected.")
      exit(1)

 



# 10
def blockstatements():  # may be e
  global id_token

  print(f"    [We're inside blockstatements].")
  # we'll have 10 cases for statements
  if id_token in statement_cases:
    print(f"    [We go to statement.]")
    statement()

  while id_token == Semicolon:
      print(f"    [We go to statement.]")
      id_token = produce_token()
      statement()



# 11
def statement():
  global id_token, token
  print(f"    We're inside statement.")
  if id_token == Identifier:
    print(f"    We're inside Identifier.")
    id = token
    id_token = produce_token()
    assignstat(id)  # 1st rule
  elif id_token == Keyword_if:
    print(f"    We're inside if.")
    id_token = produce_token()
    ifstat()  # 2nd rule  
  elif id_token == Keyword_while:
    print(f"    We're inside while.") 
    id_token = produce_token()
    whilestat()  # 3rd rule
  elif id_token == Keyword_switchcase:
    print(f"    We're inside swhitchcase.")
    id_token = produce_token()
    switchcasestat()  # 4th rule
  elif id_token == Keyword_forcase:
    print(f"    We're inside forcase.")
    id_token = produce_token()
    forcasestat()  # 5th rule
  elif id_token == Keyword_incase:
    print(f"    We're inside incase.")
    id_token = produce_token()
    incasestat()  # 6th rule
  elif id_token == Keyword_return:
    print(f"    We're inside return.")
    id_token = produce_token()
    returnstat()  # 7th rule
  elif id_token == Keyword_call:
    print(f"    We're inside call.")
    id_token = produce_token()
    callstat()  # 8th rule
  elif id_token == Keyword_print:
    print(f"    We're inside print.")
    id_token = produce_token()
    printstat()  # 9th rule
  elif id_token == Keyword_input:
    id_token = produce_token()
    inputstat()  # 10th rule
  else:
    pass



# 12
def assignstat(id):
  global id_token

  print(f"    [We're inside ASSIGNSTAT].")
  
  entity = find(id)
  if len(entity) == 4:
    print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as {entity[1]}.")
    exit(1)
  if id_token == Op_assign:
    id_token = produce_token()
    expression1 = expression()
    genquad(":=", expression1[place], "_", id)
  else:
    print(f"Error :Line {line}.\nAn assignment uses symbol ':='.")
    exit(1)



# 13
def ifstat():
  global id_token

  if id_token == Left_paren:
    id_token = produce_token()      
    cond = condition()
    if id_token == Right_paren:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nThe 'if' statement ends with ')' (right parenthesis).")
      exit(1)
  else:
    print(f"Error :Line {line}.\nAfter the 'if' keyword we need '(' (left parenthesis).")
    exit(1)
  backpatch(cond[true], nextquad())
  
  statements()
  
  jump = makelist(nextquad())
  genquad("jump", "_", "_", "_")
  
  backpatch(cond[false], nextquad())
  
  elsepart()
  
  backpatch(jump, nextquad())


# 14
def elsepart():
  global id_token
  # optional
  if id_token == Keyword_else:
    id_token = produce_token()
    statements()



# 15
def whilestat():
  global id_token
  label = nextquad()
  if id_token == Left_paren:
    id_token = produce_token()
    cond = condition()
    if id_token == Right_paren:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\n'condition must close with ')'.")
      exit(1)
  else:
      print(f"Error :Line {line}.\n'while' keyword must be followed by '('.")
      exit(1)
  backpatch(cond[true], nextquad())
  
  statements()
  
  genquad("jump", "_", "_", label)
  backpatch(cond[false], nextquad())


def switchcasestat():
  global id_token
  
  exitList = emptylist()
  while id_token == Keyword_case:
    id_token = produce_token()
    if id_token == Left_paren:
        id_token = produce_token()
        cond = condition()
        if id_token == Right_paren:
            id_token = produce_token()
            
            backpatch(cond[true], nextquad())
            
            statements()
            
            exit1 = makelist(nextquad())
            genquad("jump", "_", "_", "_")
            exitList = merge(exitList, exit1)
            
            backpatch(cond[false], nextquad())
        else:
            print(f"Error :Line {line}.\n'condition must close with ')'.")
            exit(1)
    else:
        print(f"Error :Line {line}.\n'case' keyword must be followed by '('.")
        exit(1)

  if id_token == Keyword_default:
    id_token = produce_token()
    statements()
    
    backpatch(exitList, nextquad())
  else:
    print(f"Error :Line {line}.\nDefault expected in switchcase.")
    exit(1)


def forcasestat():
  global id_token
  
  label = nextquad()
  
  while id_token == Keyword_case:
    id_token = produce_token()
    if id_token == Left_paren:
        id_token = produce_token()
        cond = condition()
        if id_token == Right_paren:
            id_token = produce_token()
            
            backpatch(cond[true], nextquad())
            
            statements()
            
            genquad("jump", "_", "_", label)
            
            backpatch(cond[false], nextquad())
        else:
            print(f"Error :Line {line}.\n'condition must close with ')'.")
            exit(1)
    else:
        print(f"Error :Line {line}.\n'case' keyword must be followed by '('.")
        exit(1)

  if id_token == Keyword_default:
    id_token = produce_token()
    statements()
  else:
    print(f"Error :Line {line}.\nDefault expected in forcase.")
    exit(1)


def incasestat():
  global id_token
  
  label = nextquad()
  flag = newtemp()
  genquad(":=", "0", "_", flag)
  
  while id_token == Keyword_case:
    id_token = produce_token()
    if id_token == Left_paren:
        id_token = produce_token()
        cond = condition()
        if id_token == Right_paren:
            id_token = produce_token()
            
            backpatch(cond[true], nextquad())
            genquad(":=", "1", "_", flag)
            statements()
            backpatch(cond[false], nextquad())
            
        else:
            print(f"Error :Line {line}.\n'condition must close with ')'.")
            exit(1)
    else:
        print(f"Error :Line {line}.\n'case' keyword must be followed by '('.")
        exit(1)
  genquad("=", "1", flag, label)
    
# 19  
def returnstat():
  global id_token, list_of_scopes, return_flag

  if len(list_of_scopes) == 1:
      print(f"Error :Line {line}.\nReturn in main program.")
      exit(1)
  else:
    type = list_of_scopes[1][3][-1][1]
    if type == "proc":
      print(f"Error :Line {line}.\nReturn in procedure.")
      exit(1)
    return_flag = True
      
  if id_token == Left_paren:
    id_token = produce_token()
    expression1 = expression()
    genquad("retv", expression1[place], "_", "_")
    if id_token == Right_paren:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nA return statement ends with ')'.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nA return statement starts with '('.")
    exit(1)



# 20
def callstat():
  global id_token, token

  if id_token == Identifier:
    procedure_name = token
    
    entity = find(procedure_name)
    if len(entity) == 2:
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as variable.")
      exit(1)
    if len(entity) == 3:
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as parameter.")
      exit(1) 
    if len(entity) == 4 and entity[1] == "func":
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as {entity[1]}.")
      exit(1)
    id_token = produce_token()
    if id_token == Left_paren:
      id_token = produce_token()
      actualparlist()
      genquad("call", procedure_name, "_", "_")
      if id_token == Right_paren:
        id_token = produce_token()
      else:
        print(f"Error :Line {line}.\nA call statement ends with ')'.")
        exit(1)
    else:
      print(f"Error :Line {line}.\nA call statement starts with '('.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nUnacceptable name for call statement.")
    exit(1)




# 21
def printstat():
  global id_token

  if id_token == Left_paren:
    id_token = produce_token()
    expression1 = expression()
    
    genquad("out", expression1[place], "_", "_")
    
    if id_token == Right_paren:
      id_token =produce_token()
    else:
      print(f"Error :Line {line}.\nA print statement ends with ')'.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nAn iput statement starts with '('.")
    exit(1)



# 22
def inputstat():
  global id_token, token
  
  print(f"  [We're inside INPUT].")

  if id_token == Left_paren:
    id_token = produce_token()
    if id_token == Identifier:
      
      entity = find(token)
      if len(entity) == 4:
        print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as {entity[1]}.")
        exit(1)
      genquad("inp", token, "_", "_")
      
      id_token = produce_token()
      if id_token == Right_paren:
        id_token = produce_token()
      else:
        print(f"Error :Line {line}.\nAn iput statement ends with ')'.")
        exit(1)
    else:
      print(f"Error :Line {line}.\nid name inside input statement is invalid.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nAn iput statement needs '(' after input keyword.")
    exit(1)



# 23
def actualparlist():
  global id_token
  # what follows is optional
  if id_token == Keyword_in or id_token == Keyword_inout:
    actualparitem()
    while id_token == Comma:
      id_token = produce_token()
      actualparitem()



# 24
def actualparitem():
  global id_token, token

  if id_token == Keyword_in:
    id_token = produce_token()
    expression1 = expression()
    genquad("par", expression1[place], "CV", "_")
  elif id_token == Keyword_inout:
    id_token = produce_token()
    if id_token == Identifier:
      entity = find(token)
      if len(entity) == 4:
        print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as {entity[1]}.")
        exit(1)
      genquad("par", token, "REF", "_")
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nA by reference id(name) was expected.")
      exit(1)
  else:
    print(f"Error :Line {line}.\nKeywords 'in' or 'inout' was expected.")
    exit(1)



# 25
def condition():
  global id_token

  boolterm1 = boolterm()
  while id_token == Keyword_or:
    id_token = produce_token()
    backpatch(boolterm1[false], nextquad())
    boolterm2 = boolterm()
    
    boolterm1[true] = merge(boolterm1[true], boolterm2[true])
    boolterm1[false] = boolterm2[false]
    
  return boolterm1



# 26
def boolterm():
  global id_token

  boolfactor1 = boolfactor()
  while id_token == Keyword_and:
    id_token = produce_token()
    backpatch(boolfactor1[true], nextquad())
    boolfactor2 = boolfactor()
    
    boolfactor1[true] = boolfactor2[true]
    boolfactor1[false] = merge(boolfactor1[false], boolfactor2[false])
  return boolfactor1

# 27
def boolfactor():
  global id_token
  
  boolfactorList = ["", "", ""]
  if id_token == Keyword_not:
    id_token = produce_token()
    if id_token == Left_bracket:
      id_token = produce_token()
      cond = condition()
      boolfactorList[true] = cond[false]
      boolfactorList[false] = cond[true]
      if id_token == Right_bracket:
        id_token = produce_token()
      else:
        print(f"Error :Line {line}.\nThe factor in boolean expression must close with ']'.")
        exit(1)
    else:
        print(f"Error :Line {line}.\nThe factor in boolean expression must start with '['.")
        exit(1)
  elif id_token == Left_bracket:
    id_token = produce_token()
    cond = condition()
    boolfactorList = cond
    if id_token == Right_bracket:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nThe factor in boolean expression must close with ']'.")
      exit(1)
  else:
    expression1 = expression()
    rel = relOp()
    expression2 = expression()
    
    boolfactorList[true] = makelist(nextquad())
    genquad(rel, expression1[place], expression2[place], "_")
    boolfactorList[false] = makelist(nextquad())
    genquad("jump", "_", "_", "_")
    
  return boolfactorList



# 28
def expression():
  global id_token

  print(f"    [We're inside EXPRESSION].")
  optionalSign()
  term1 = term()
  while id_token == Op_add or id_token == Op_sub:  # optional part
    id_token_while = id_token
    id_token = produce_token()
    term2 = term()
    
    w = newtemp()
    if id_token_while == Op_add:
      genquad("+", term1[place], term2[place], w)
    else:
      genquad("-", term1[place], term2[place], w)
    term1[place] = w
    
  return term1

# 29
def term():
  global id_token

  factor1 = factor()
  while id_token == Op_multi or id_token == Op_div:  # optional part
    id_token_while = id_token
    id_token = produce_token()
    factor2 = factor()
    
    w = newtemp()
    if id_token_while == Op_multi:
      genquad("*", factor1[place], factor2[place], w)
    else:
      genquad("/", factor1[place], factor2[place], w)
      
    factor1[place] = w
  
  return factor1


# 30
def factor():
  global id_token, my_character, token

  returnList = ["", "", ""]
  if id_token == Integer:
    returnList[place] = token
    id_token = produce_token()
  elif id_token == Left_paren:
    id_token = produce_token()
    returnList = expression()
    if id_token == Right_paren:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nA factor of your expression must close with ')'.")
      exit(1)
  elif id_token == Identifier:
    returnList[place] = token
    id_token = produce_token()
    idtail(returnList)
  else:
    print(f"Error :Line {line}.\nA factor of your expression must open with '(' or must be an integer or a variable.")
    exit(1)
  
  return returnList

# 31
def idtail(returnList):
  global id_token
  
  entity = find(returnList[place])
  
  if id_token == Left_paren:
    if len(entity) == 2:
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as variable.")
      exit(1)
    if len(entity) == 3:
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as parameter.")
      exit(1) 
    if len(entity) == 4 and entity[1] == "proc":
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as {entity[1]}.")
      exit(1)
    id_token = produce_token()
    actualparlist()
    w = newtemp()
    genquad("par", w, "RET", "_")
    genquad("call", returnList[place], "_", "_")
    returnList[place] = w
    if id_token == Right_paren:
      id_token = produce_token()
    else:
      print(f"Error :Line {line}.\nFunction call must end with ')'.")
      exit(1)
  else:
    if len(entity) == 4:
      print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared as {entity[1]}.")
      exit(1)





# 32
def optionalSign():
  global id_token

  if id_token == Op_add:
    id_token = produce_token()
  elif id_token == Op_sub:
    id_token = produce_token()



# 33
def relOp():
  global id_token
  
  if id_token in relational_operators:
    id_token_if = id_token
    id_token = produce_token()
    if id_token_if == Op_equal:
      return '='
    elif id_token_if == Op_greater:
      return '>'
    elif id_token_if == Op_greater_equal:
      return '>='
    elif id_token_if == Op_less:
      return '<'
    elif id_token_if == Op_less_equal:
      return '<='
    elif id_token_if == Op_not_equal:
      return '<>'
  else:
    print(f"Error :Line {line}.\n '=','<', '<=', '>' ,'>=' or '<>' expected.")
    exit(1)



# 34
def addOp():
  global id_token

  if id_token == Op_add:
    id_token = produce_token()
  elif id_token == Op_sub:
    id_token = produce_token()
  else:
    print(f"Error :Line {line}.\n '+' or '-' expected.")
    exit(1)



# 35
def mulOp():
  global id_token

  if id_token == Op_multi:
    id_token = produce_token()
  elif id_token == Op_div:
    id_token = produce_token()
  else:
    print(f"Error :Line {line}.\n '*' or '/' expected.")
    exit(1)


def nextquad():
  global label_of_quad
  return label_of_quad

def newtemp():
  global number_of_temporary
  
  number_of_temporary += 1
  temporary = "T_" + str(number_of_temporary)
  insertEntity(createVariable(temporary))
  return temporary

def genquad(op, x, y, z):
  global label_of_quad, list_of_quads, list_of_quads_asm
  
  quad = [nextquad(), op, x, y, z]
  list_of_quads.append(quad)
  label_of_quad += 1
  
  list_of_quads_asm.append(quad)
  
def emptylist():
  return []

def makelist(x):
  return [x]

def merge(list1, list2):
  list1 = list1 + list2
  return list1

def backpatch(list1, labelZ):
  global list_of_quads
  
  for x in list1:
    list_of_quads[x][4] = labelZ

def output_int():
  global list_of_quads, output_file_int
  
  for quad in list_of_quads:
    line = str(quad[0]) + ": " + str(quad[1]) + ", " + str(quad[2]) + ", " + str(quad[3]) + ", " + str(quad[4]) + "\n"
    output_file_int.write(line)

def output_c():
  global list_of_quads, output_file_c, list_of_variables
  
  line = "#include <stdio.h>\n\nint main(){\n"
  output_file_c.write(line)
  if len(list_of_variables) > 1:
    line = "int "
    for v in list_of_variables:
      line = line + v + ", "
    line = line[0:len(line) - 2] + ";\n"
    output_file_c.write(line)
    
    line = "int "
    for i in range(1, number_of_temporary + 1):
      line = line + "T_" + str(i) + ", "
    line = line[0:len(line) - 2] + ";\n"
    output_file_c.write(line)
  
  for quad in list_of_quads:
    
    line = "L"+str(quad[0]) + ": ";
    if quad[1] == ":=":
      line = line + str(quad[4]) + " = " + str(quad[2])
    elif quad[1] == "+" or quad[1] == "-" or quad[1] == "*" or quad[1] == "/":
      line = line + str(quad[4]) + " = " + str(quad[2]) + " "+ str(quad[1]) + " " + str(quad[3])
    elif quad[1] == "<" or quad[1] == "<=" or quad[1] == ">" or quad[1] == ">=":
      line = line + "if(" +str(quad[2]) + " "+ str(quad[1]) + " " + str(quad[3]) + ") goto L" + str(quad[4])
    elif quad[1] == "=" :
      line = line + "if(" +str(quad[2]) + " == " + str(quad[3]) + ") goto L" + str(quad[4])
    elif quad[1] == "<>" :
      line = line + "if(" +str(quad[2]) + " != " + str(quad[3]) + ") goto L" + str(quad[4])
    elif quad[1] == "jump" :
      line = line + "goto L" + str(quad[4])
    elif quad[1] == "inp" :
      line = line + "scanf(\"%d\", &" + str(quad[2]) + ")"
    elif quad[1] == "out" :
      line = line + "printf(\"%d\\n\", " + str(quad[2]) + ")"
    
    
    #+ str(quad[1]) + ", " + str(quad[2]) + ", " + str(quad[3]) + ", " + str(quad[4]) + "\n"
    line = line + ";\n"
    output_file_c.write(line)  
  line = "}\n"
  output_file_c.write(line)
  
def insertScope(scope_name):
  global list_of_scopes
  
  nesting_level = len(list_of_scopes)
  
  scope = [scope_name, nesting_level, 12, []]
  
  list_of_scopes.insert(0, scope)
  
def deleteScope():
  global list_of_scopes
  
  output_asm()
  
  line = "Current Symbol Matrix\nStart\n\n"
  output_file_s.write(line)
  for scope in list_of_scopes:
    line = str(scope) + "\n"
    output_file_s.write(line)
  line = "End\n\n"
  output_file_s.write(line)
  del list_of_scopes[0]

def createVariable(name):
  global list_of_scopes
  
  offset = list_of_scopes[0][2]
  list_of_scopes[0][2] += 4
  
  entity = [name, offset]
  return entity

def createParameter(name, type):
  global list_of_scopes
  
  offset = list_of_scopes[0][2]
  list_of_scopes[0][2] += 4
  
  entity = [name, offset, type]
  return entity

def createFuncProc(name, type):
  return [name, type, -100, -100]

def insertEntity(entity):
  global list_of_scopes
  
  for e in list_of_scopes[0][3]:
    if e[0] == entity[0]:
        print(f"Error :Line {line}.\nEntity name -{entity[0]}- is declared.")
        exit(1)
  list_of_scopes[0][3].append(entity)
  
def find(name):
  global list_of_scopes
  
  for scope in list_of_scopes:
    for entity in scope[3]:
      if name == entity[0]:
        return entity
  print(f"Error :Line {line}.\nEntity name -{name}- is not declared.")
  exit(1)

def find_nesting_level(name):
  global list_of_scopes
  
  for scope in list_of_scopes:
    for entity in scope[3]:
      if name == entity[0]:
        return scope[1]
  return -1

def gnlvcode(x):
  global output_file_f, list_of_scopes
  
  nesting_level = len(list_of_scopes) - 1
  nesting_level_x = find_nesting_level(x)
  
  line = "lw $0, -4(sp)\n"
  output_file_f.write(line)
  for i in range(nesting_level - nesting_level_x - 1):
    line = "lw t0, -4(t0)\n"
    output_file_f.write(line)
  
  entity = find(x)
  offset = entity[1]
  line = "addi t0, t0, -" + str(offset)
  output_file_f.write(line)

def loadvr(v, r):
  global output_file_f, list_of_scopes
  
  nesting_level = len(list_of_scopes) - 1
  nesting_level_v = find_nesting_level(v)

  if v[0].isdigit():
    line = "li t" +str(r) + ", " + str(v) + "\n"
    output_file_f.write(line)
  else:
    entity = find(v)
    offset = entity[1]
    
    if nesting_level_v == 0:
      line = "lw t" +str(r) + ", -" + str(offset) +"(gp)\n"
      output_file_f.write(line)
    elif nesting_level_v == nesting_level and len(entity) == 3 and entity[2] == "REF":
      line = "lw t0, -" + str(offset) +"(sp)\n"
      line = line + "lw t" +str(r) + ", (t0)\n"
      output_file_f.write(line)
    elif nesting_level_v == nesting_level:
      line = "lw t" +str(r) + ", -" + str(offset) + "(sp)\n"
      output_file_f.write(line)
    elif nesting_level_v < nesting_level and len(entity) == 3 and entity[2] == "REF":
      gnlvcode(v)
      line = "lw t0, (t0)\n"
      line = line + "lw t" +str(r) + ", (t0)\n"
      output_file_f.write(line)
    elif nesting_level_v < nesting_level:
      gnlvcode(v)
      line = "lw t" +str(r) + ", (t0)\n"
      output_file_f.write(line)



def storerv(r,v):
  global output_file_f, list_of_scopes
  
  nesting_level = len(list_of_scopes) - 1
  nesting_level_v = find_nesting_level(v)

  entity = find(v)
  offset = entity[1]
  
  if nesting_level_v == 0:
    line = "sw t" +str(r) + ", -" + str(offset) + "(gp)\n"
    output_file_f.write(line)
  elif nesting_level_v == nesting_level and len(entity) == 3 and entity[2] == "REF":
    line = "lw t0, -" + str(offset) +  "(sp)\n"
    line = line + "sw t" +str(r) + ", (t0)\n"
    output_file_f.write(line)
  elif nesting_level_v == nesting_level:
    line = "sw t" +str(r) + ", -" + str(offset) + "(sp)\n"
    output_file_f.write(line)
  elif nesting_level_v < nesting_level and len(entity) == 3 and entity[2] == "REF":
    gnlvcode(v)
    line = "lw t0, (t0)\n"
    line = line + "sw t" +str(r) + ", (t0)\n"
    output_file_f.write(line)
  elif nesting_level_v < nesting_level:
    gnlvcode(v)
    line = "sw t" +str(r) + ", (t0)\n"
    output_file_f.write(line)
     
def output_asm():
  global list_of_quads_asm, output_file_f, list_of_scopes
  
  parI = 0
  i = 0
  if output_file_f.tell() == 0:
    line = ".data\n"
    line = line + "str_nl: .asciz \"\\n\"\n"
    line = line + ".text\n"
    line = line + "j Lmain\n"
    output_file_f.write(line)

  nesting_level = len(list_of_scopes) - 1
  for quad in list_of_quads_asm:
    i = i + 1
    line = "L"+str(quad[0]) + ": "
    output_file_f.write(line + "\n")
    line = ""
    if quad[1] == "begin block":
      if nesting_level == 0:
        line = "Lmain:\n"
        line = line + "addi sp, sp, " + str(list_of_scopes[0][2]) + "\n"
        line = line + "mv gp, sp\n"
      else:
        line = "sw ra, (sp)\n"
    elif quad[1] == "end block":
      if nesting_level != 0:
        line = "lw ra, (sp)\n"
        line = line + "jr ra\n"
    elif quad[1] == ":=":
      loadvr(quad[2], 1)
      storerv(1, quad[4])
    elif quad[1] == "+" or quad[1] == "-" or quad[1] == "*" or quad[1] == "/":
      output_file_f.write(line)
      line = ""
      loadvr(quad[2], 1)
      loadvr(quad[3], 2)
      if quad[1] == "+":
        line = line + "add t1, t1, t2\n"
      elif quad[1] == "-":
        line = line + "sub t1, t1, t2\n"
      elif quad[1] == "*":
        line = line + "mul t1, t1, t2\n"
      elif quad[1] == "/":
        line = line + "div t1, t1, t2\n"
      output_file_f.write(line)
      storerv(1, quad[4])
      line = ""
    elif quad[1] == "<" or quad[1] == "<=" or quad[1] == ">" or quad[1] == ">=" or quad[1] == "=" or quad[1] == "<>":
      output_file_f.write(line)
      line = ""
      loadvr(quad[2], 1)
      loadvr(quad[3], 2)
      if quad[1] == "<":
        line = line + "blt t1, t2, L" + str(quad[4]) + "\n"
      elif quad[1] == "<=":
        line = line + "ble t1, t2, L" + str(quad[4]) + "\n"
      elif quad[1] == ">":
        line = line + "bgt t1, t2, L" + str(quad[4]) + "\n"
      elif quad[1] == ">=":
        line = line + "bge t1, t2, L" + str(quad[4]) + "\n"
      elif quad[1] == "=":
        line = line + "beq t1, t2, L" + str(quad[4]) + "\n"
      elif quad[1] == "<>":
        line = line + "bne t1, t2, L" + str(quad[4]) + "\n"
    elif quad[1] == "jump" :
      line = line + "j L" + str(quad[4]) + "\n"
    elif quad[1] == "inp" :
      line = line + "li a7, 5\n"
      line = line + "ecall\n"
      line = line + "mv t1, a0\n"
      output_file_f.write(line)
      storerv(1, quad[2])
      line = ""
    elif quad[1] == "out" :
      output_file_f.write(line)
      line = ""
      loadvr(quad[2], 0)
      line = line + "mv a0, t0\n"
      line = line + "li a7, 1\n"
      line = line + "ecall\n"
      line = line + "la a0, str_nl \n"
      line = line + "li a7, 4\n"
      line = line + "ecall\n"
      
    elif quad[1] == "retv" :
      loadvr(quad[2], 1)
      line = line + "lw t0, -8(sp)\n"
      line = line + "sw t1, (t0)\n"
      
    elif quad[1] == "par" :
      if parI == 0:
        for j in range(i, len(list_of_quads_asm)):
          if list_of_quads_asm[j][1] == "call":
            entity = find(list_of_quads_asm[j][2])
            line = line + "addi fp, sp, " + str(entity[3])
            output_file_f.write(line + "\n")
            line = ""
      
      if quad[3] == "CV":
        loadvr(quad[2], 0)
        line = line + "sw t0, -" + str((12+4*parI)) + "(fp)\n"
        parI = parI + 1
      elif quad[3] == "REF":
        nesting_level = len(list_of_scopes) - 1
        nesting_level_v = find_nesting_level(quad[2])

        entity = find(quad[2])
        
        if nesting_level == nesting_level_v:
          if len(entity) == 3 and entity[2] == "REF":
            line = line + "lw t0, -" + str(entity[1]) + "(sp)\n"
            line = line + "sw t0, -" + str((12+4*parI)) + "(fp)\n"
            parI = parI + 1
          else:
            line = line + "addi t0, sp, -" + str(entity[1]) + "\n"
            line = line + "sw t0, -" + str((12+4*parI)) + "(fp)\n"
            parI = parI + 1
        else:
          if len(entity) == 3 and entity[2] == "REF":
            gnlvcode()
            line = line + "lw t0, (t0)\n"
            line = line + "sw t0, -" + str((12 + 4*parI)) + "(fp)\n"
            parI = parI + 1
          else:
            gnlvcode()
            line = line + "sw t0, -" + str((12+4*parI)) + "(fp)\n"
            parI = parI + 1
            
        loadvr(quad[2], 0)
        line = line + "sw t0, -" + str((12+4*parI)) + "(fp)\n"
        parI = parI + 1
      
      elif quad[3] == "RET":
        entity = find(quad[2])
        line = line + "addi t0, sp, -" + str(entity[1]) + "\n"
        line = line + "sw t0, -8(fp)\n"
        
    elif quad[1] == "call":
      parI = 0
      entity = find(quad[2])
      line = line + "sw sp, -4(fp)\n"
      line = line + "addi sp, sp, " + str(entity[3]) + "\n"
      line = line + "jal L" + str(entity[2]) + "\n"
      line = line + "addi sp, sp, -" + str(entity[3]) + "\n"
    elif quad[1] == "halt":
      line = line + "li a0, 0\n"
      line = line + "li a7, 93\n"
      line = line + "ecall\n"
      
    output_file_f.write(line)  
  line = "\n"
  output_file_f.write(line)
  list_of_quads_asm = []
#----------------#
# main() function
#----------------#
try:
  input_file = open(filename, 'r')
  filename = filename[0:len(filename)-2] + 'int'
  output_file_int = open(filename, 'w')
  filename = filename[0:len(filename)-3] + 'c'
  output_file_c = open(filename, 'w')
  filename = filename[0:len(filename)-1] + 'symb'
  output_file_s = open(filename, 'w')
  filename = filename[0:len(filename)-4] + 'asm'
  output_file_f = open(filename, 'w')
  
except FileNotFoundError:
  print("Error: File not found.")
  exit(1)

program() # 1st function of our syntax analyzer

output_int()
output_c()

output_file_int.close()
output_file_c.close()
output_file_f.close()
