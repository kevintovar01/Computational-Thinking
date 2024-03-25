from logic.stack import Stack


def postfix_notation(mylist):
    data = Stack()
    posfija = []
    count = 0

    for i in mylist:
        try:
            if float(i):
                posfija.append(i)
        except:
            if i == '(' and count == 0 and data.size >= 1:
                if data.look() != None:
                    posfija.append(data.previous())
                    count += 1
            elif i != ')' and i != '(':
                data.push(i)
            elif i == ')':
                posfija.append(data.pop())

    while data.top != None:
        posfija.append(data.pop())
    
    return posfija


def postfix_solution(postfix):
    data = Stack()
    op = {
        '+': lambda x, y: x + y, 
        '-': lambda x, y: x - y, 
        '^': lambda x, y: x**y,
        '/': lambda x, y: x/y,
        '*': lambda x, y: x*y,
        'x': lambda x, y: x*y
        }

    for i in postfix:
        try:
            if float(i):
                data.push(float(i))
        except:
            if data.size >= 2:
                number_1 = data.pop()
                number_2 = data.pop()
                result = op[i](number_2, number_1)
                data.push(result)

    return data.pop()


def run():
    
    infija = list(input())
    infija = [i for i in infija if i!=' ']
    
    postfix = postfix_notation(infija)
    result = postfix_solution(postfix)

    print(f'Postfix Notation: {"".join(postfix)}') 
    print(f'Result: {result}')
    

if __name__ == '__main__':
    run()