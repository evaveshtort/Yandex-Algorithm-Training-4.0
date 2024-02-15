def is_good(str1):
    if str1 == "":
        return True
    elif str1[0] == ")" or str1[0] == "]" or str1 == "}":
        return False
    s = []

    for i in str1:
        if i == "(" or i == "{" or i == "[":
            s.append(i)
 
        elif i == ")":
            if len(s) != 0 and s[-1] == "(":
                del s[-1]
            else:
                return False
        elif i == "]":
            if len(s) != 0 and s[-1] == "[":
                del s[-1]
            else:
                return False
        elif i == "}":
            if len(s) != 0 and s[-1] == "{":
                del s[-1]
            else:
                return False
            
    if len(s) == 0:
        return True
    return False

str2 = input()
if is_good(str2): print('yes')
else: print('no')