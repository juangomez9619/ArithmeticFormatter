def arithmetic_arranger(problems, show_result = None):
    print_1 = list()
    print_2 = list()
    print_3 = list()
    print_4 = list()
    if len(problems) >5:
        return "Error: Too many problems."
    for operation in problems:
        line_1 = str()
        line_2 = str()
        line_3 = str()
        line_4 = str()
        #print(operation)
        try:
            operator_1 = int(operation.split()[0])
            operator_2 = int(operation.split()[2])
            if operation.split()[1] == '+':
                result = operator_1 + operator_2
            elif operation.split()[1] == '-':
                result = operator_1 - operator_2
            else:
                return "Error: Operator must be '+' or '-'."
            if (len(operation.split()[0])>=5) or (len(operation.split()[2])>=5):
                return "Error: Numbers cannot be more than four digits."
        
            if len(operation.split()[0]) >= len(operation.split()[2]):
                line_1 = str(operation.split()[0])
                line_2 = ' '*(len(operation.split()[0])-len(operation.split()[2]))+str(operation.split()[2])
                line_4 = ' '*(len(operation.split()[0])-len(str(result)))+str(result)
            else:
                line_1 = ' '*(len(operation.split()[2])-len(operation.split()[0]))+str(operation.split()[0])
                line_2 = str(operation.split()[2])
                line_4 = ' '*(len(operation.split()[2])-len(str(result)))+str(result)

            line_1 = ' '*2+line_1
            line_2 = str(operation.split()[1])+' '+line_2
            line_3 = '-'*(len(line_1))
            if result >= 0:
                line_4 = ' '*2+line_4
            else:
                line_4 = ' '+line_4
            print_1.append(line_1)
            print_2.append(line_2)
            print_3.append(line_3)
            print_4.append(line_4)

        except:
            return "Error: Numbers must only contain digits."

    out_1 = ''
    out_2 = ''
    out_3 = ''
    out_4 = ''

    for item in range(len(print_1)):
        if item == 0:
            out_1 = out_1 + print_1[item]
            out_2 = out_2 + print_2[item]
            out_3 = out_3 + print_3[item]
            out_4 = out_4 + print_4[item]
        else:
            out_1 = out_1 + ' '*4 + print_1[item]
            out_2 = out_2 + ' '*4 + print_2[item]
            out_3 = out_3 + ' '*4 + print_3[item]
            out_4 = out_4 + ' '*4 + print_4[item]

    if show_result != True:        
        output = out_1.rstrip()+'\n'+out_2.rstrip()+'\n'+out_3.rstrip()
    else:
        output = out_1.rstrip()+'\n'+out_2.rstrip()+'\n'+out_3.rstrip()+'\n'+out_4.rstrip()
    return output