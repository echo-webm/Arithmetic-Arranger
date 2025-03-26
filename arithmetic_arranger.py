def operand(equation):
    numbers = ''.join([num for num in equation if num.isnumeric()])
    top_operand = []
    for char in equation:
        if char.isnumeric():
            top_operand.append(char)
        else:
            top_operand_string = ''.join(top_operand)
            break
    bottom_operand = []
    for i in range(len(numbers) - len(top_operand_string)):
        bottom_operand.append(equation[-i - 1])
    return ''.join(top_operand), ''.join(bottom_operand[::-1])
    

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

def padding(widths, operand_list, i):
    pad = []
    for i in range(widths[i] - len(operand_list[i].strip('-'))):
        pad.append(' ')
    return ''.join(pad)

def final_operand_top(operand_top_list, widths, i):
    return '  ' + padding(widths, operand_top_list, i) + operand_top_list[i] + '    '

def final_operand_bottom(operand_bottom_list, widths, operation_list, i):
    return f'{operation_list[i]} ' + padding(widths, operand_bottom_list, i) + operand_bottom_list[i] + '    '

def dashed_line(widths, i):
    line = []
    for i in range(widths[i] + 2):
        line.append('-')
    return ''.join(line) + '    '

def final_results(results, widths, i):
    if results[i] < 0:
        return ' ' + padding(widths, results, i) + str(results[i]) + '    '
    else: 
        return '  ' + padding(widths, results, i) + str(results[i]) + '    '

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

    #populates operand lists
    for equation in problems:
        operand_top_list.append(operand(equation)[0])
        operand_bottom_list.append(operand(equation)[1])
        
    
    #catches remaining errors
    for i in range(len_problems):
        if error_catch_2(operand_top_list, operand_bottom_list, i) != None:
            return error_catch_2(operand_top_list, operand_bottom_list, i)

    #computes results
    for i in range(len_problems):
        if operation_list[i] == '+':
            results.append(int(operand_top_list[i]) + int(operand_bottom_list[i]))
        else:
             results.append(int(operand_top_list[i]) - int(operand_bottom_list[i]))    

    #returns maximum widths
    for i in range(len_problems):
        widths.append(max(len(operand_top_list[i]), len(operand_bottom_list[i])))

    #creates final string
    top_list = ['_']
    bottom_list = ['_']
    dash_list = ['']

    for i in range(len_problems):
        top_list.append(final_operand_top(operand_top_list, widths, i))
    top_string = ''.join(top_list)

    for i in range(len_problems):
        bottom_list.append(final_operand_bottom(operand_bottom_list, widths, operation_list, i))
    bottom_string = ''.join(bottom_list)

    for i in range(len_problems):
        dash_list.append(dashed_line(widths, i))
    dash_string = ''.join(dash_list)

    if showResults:
        results_list = ['_']
        for i in range(len_problems):
            results_list.append(final_results(results, widths, i))
        results_string = ''.join(results_list)
        results_string.strip(' ')

        return top_string.strip(' ').strip('_') + '\n' + bottom_string.strip(' ').strip('_') + '\n' + dash_string.strip(' ') + '\n' + results_string.strip('_').strip(' ')

    return top_string.strip(' ').strip('_') + '\n' + bottom_string.strip(' ').strip('_') + '\n' + dash_string.strip(' ')