file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia10/input.txt')
stack=[]
error=0

for line in file:
    list = line
    for i in list:
        stack.append(i)
        if(i==']' or i=='}' or i==')' or i=='>'):
            if(i==']'):
                if(stack[stack.index(i)-1]=='['):
                    stack.pop(stack.index(i)-1)
                    stack.pop(stack.index(i))
                else:
                    error+=57
                    break
            if(i=='}'):
                if(stack[stack.index(i)-1]=='{'):
                    stack.pop(stack.index(i)-1)
                    stack.pop(stack.index(i))
                else:
                    error+=1197
                    break
            if(i=='>'):
                if(stack[stack.index(i)-1]=='<'):
                    stack.pop(stack.index(i)-1)
                    stack.pop(stack.index(i))
                else:
                    error+=25137
                    break
            if(i==')'):
                if(stack[stack.index(i)-1]=='('):
                    stack.pop(stack.index(i)-1)
                    stack.pop(stack.index(i))
                else:
                    error+=3
                    break
    stack=[]

print(error)