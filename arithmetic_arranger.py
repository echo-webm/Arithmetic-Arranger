def operand(equation):
    return ''.join([num for num in equation if num.isnumeric()]), ''.join([num for num in equation[::-1] if num.isnumeric()])

def error_catch(equation, operand_top_list, operand_bottom_list, problems, len_problems, i):
    if len_problems > 5:
        return "Error: Too many problems."
    elif len(operand_bottom_list[i]) > 4:
        return "Error: Numbers cannot be more than four digits."
    elif len(operand_top_list[i]) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
        for char in equation:
            if char.isalpha():
                return "Error: Numbers must only contain digits."
                break
        
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

    #populates lists
    for equation in problems:
        operand_top_list.append(operand(equation)[0])
        operand_bottom_list.append(operand(equation)[1][::-1])
        operation_list.append(operation(equation))
    
    #catches errors
    for i in range(len_problems):
        if operation_list[i] == None:
            return "Error: Operator must be '+' or '-'."
        if error_catch(equation, operand_top_list, operand_bottom_list, problems, len_problems, i) != None:
            return error_catch(equation, operand_top_list, operand_bottom_list, problems, len_problems, i)

    #computes results
    for i in range(len_problems):
        if operation_list[i] == '+':
            results.append(int(operand_top_list[i]) + int(operand_bottom_list[i]))
        else:
             results.append(int(operand_top_list[i]) - int(operand_bottom_list[i]))