import re
stack = ''
final_str = ''
def getExp(str):
    stack = 0
    startIndex = None
    results = []
    results1 = []
    for i, c in enumerate(str):
        if c == '(':
            if stack == 0:
                startIndex = i + 1 # string to extract starts one index later

            # push to stack
            stack += 1
        elif c == ')':
            # pop stack
            stack -= 1

            if stack == 0:
                results.append(str[startIndex:i])
    return results

str = '(A=2 && B=3) || (C=4 && D=5)'
count = 0
for i in str:
    if i == "(":
        count += 1
    elif i == ")":
        count -= 1
if count != 0:
    print("Syntax invalid")
elif count == 0:
    print(True)
    print(str)
    res1 = getExp(str)

    print(res1) #checking the input for outer paranthesis
    str1 = str.split('||')
    print(str1)
    res2 = getExp(str1[0])[0]
    res3= res2.split('&&')[0].split('=')
    print(res3)
