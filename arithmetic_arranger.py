def operand(equation):
    return ''.join([num for num in equation if num.isnumeric()]), ''.join([num for num in equation[::-1] if num.isnumeric()])

def error_catch_1(equation, len_problems, i):
    if len_problems > 5:
        return "Error: Too many problems."
    else:
        for char in equation:
            if char.isalpha():
                return "Error: Numbers must only contain digits."
                break

def error_catch_2(operand_top_list, operand_bottom_list, i):
    if len(operand_bottom_list[i]) > 4 or len(operand_top_list[i]) > 4:
        return "Error: Numbers cannot be more than four digits."
        
def operation(equation):
    for char in equation:
        if char == ' ' or char.isnumeric():
            pass
        elif char == '+' or char == '-':
            return char

def arithmetic_arranger(problems, showResults=False):
    len_problems = len(problems)
    operand_top_list = []
    operand_bottom_list = []
    operation_list = []
    results = []
    widths = []
    
    #catches initial errors
    for i in range(len_problems):
        operation_list.append(operation(problems[i]))
        if operation_list[i] == None:
            return "Error: Operator must be '+' or '-'."
        elif error_catch_1(problems[i], len_problems, i) != None:
            return error_catch_1(problems[i], len_problems, i)

    #populates lists
    for equation in problems:
        operand_top_list.append(operand(equation)[0])
        operand_bottom_list.append(operand(equation)[1][::-1])
        
    
    #catches remaining errors
    for i in range(len_problems):
        if error_catch_2(problems[i], len_problems, i) != None:
            return error_catch_2(operand_top_list, operand_bottom_list, i)

    #computes results
    for i in range(len_problems):
        if operation_list[i] == '+':
            results.append(int(operand_top_list[i]) + int(operand_bottom_list[i]))
        else:
             results.append(int(operand_top_list[i]) - int(operand_bottom_list[i]))