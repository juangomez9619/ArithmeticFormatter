def arithmetic_arranger(problems, show_result = None):
    line_1 = str()
    line_2 = str()
    line_3 = str()
    line_4 = str()

    for operation in problems:
        print(operation)
        try:
            operator_1 = int(operation.split()[0])
            operator_2 = int(operation.split()[2])
            if operation.split()[1] == '+':
                result = operator_1 + operator_2
            elif operation.split()[1] == '-':
                result = operator_1 - operator_2

            if len(operation.split()[0]) >= len(operation.split()[2]):
                line_1 = line_1+str(operation.split()[0])+' '
                line_2 = line_2+' '*(len(operation.split()[0])-len(operation.split()[2]))+str(operation.split()[2])+' '

                line_1 = ' '*2+line_1
                line_2 = str(operation.split()[1])+' '+line_2
                line_3 = '-'*(len(line_1)-1)
            else:
                pass
                # line_1 = line_1+' '*(len(operation.split()[2])-len(operation.split()[0]))+' '
                #line_2 = line_2+str(operation.split()[2])+' '
            
            
        except:
            print('error')

    output = line_1+'\n'+line_2+'\n'+line_3+'\n'+line_4
    return output