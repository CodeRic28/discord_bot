import math

def brac(exp): ##This function evaluates the expression inside parentheses
    while "(" in exp:
        c_brac = o_pos = exp.index(")")
        while exp[o_pos] != "(":
            o_pos -= 1
        o_brac = o_pos
        brac_exp = exp[o_brac+1 : c_brac]
        while 'pi' in brac_exp:
            p = brac_exp.find('pi')
            p_left = brac_exp[:p]
            i = p + 1
            i_right = brac_exp[i+1:]
            brac_exp = p_left + '3.14' + i_right
        if '*-' in brac_exp or '/-' in brac_exp or '--' in exp or '+-' in exp:
            val = neg(brac_exp)
            exp = exp[:o_brac] + str(val) + exp[c_brac + 1:]
        else:
            if exp[o_brac-1].isnumeric() is True:
                exp = exp[:o_brac] + '*' + str(evaluate(brac_exp)) + exp[c_brac + 1:]
            else:
                exp = exp[:o_brac] + str(evaluate(brac_exp)) + exp[c_brac + 1:]
    return evaluate(exp)

#This function identifies the number to the left of the operator
def lft(exp, pos):
    i = pos-1
    while exp[i].isnumeric() is True or exp[i] == '.':
        i=i-1
        if i<0:
            break
    return exp[i+1:pos]

#This function identifies the number to the right of the operator
def rgt(exp, pos):
    i = pos+1
    while exp[i].isnumeric() is True or exp[i] == '.' or exp[i] == 'p' or exp[i] == 'i':
        i=i+1
        if i >= len(exp):
            break
    return exp[pos+1:i]

#If there is a * and / followed by a - sign then move the '-' sign until it encounters a '+' or '-' sign.
#If it encounters a '-' sign, it changes it to '+' sign and vice-versa.
#If there is a ^ followed by a - then it changes the expression to 1/a^b form
def stmin(exp, sgn):
    if sgn == '^':
        star_pos = exp.find(sgn+'-')
        l = lft(exp, star_pos)
        r = rgt(exp, star_pos)
        exp = exp[:star_pos - len(l)] + str('1/') + l + str('^') + r + exp[star_pos + len(r) + 2:]
    elif sgn == '-':
        star_pos = exp.find(sgn+'-')
        min_pos = star_pos + 1
        left = exp[:star_pos]
        right = exp[min_pos + 1:]
        exp = left + '+' + right
    elif sgn == '+':
        star_pos = exp.find(sgn+'-')
        min_pos = star_pos + 1
        left = exp[:star_pos]
        right = exp[min_pos + 1:]
        exp = left + '-' + right
    else:
        star_pos = exp.find(sgn+'-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos+1:]
        i = star_pos - 1
        while exp[i].isnumeric() is True or exp[i] == '.' or exp[i] == '*' or exp[i] == '/':
            i=i-1
            if exp[i] == '+' or exp[i] == '-':
                break
            elif i<0: break
        sign = i
        if exp[sign] == '+':
            exp = exp[:sign] + str('-') + exp[sign+1:min_pos] + exp[min_pos+1:]
        elif exp[sign] == '-':
            exp = exp[:sign] + str('+') + exp[sign+1:min_pos] + exp[min_pos+1:]
            if exp[0] == '+':
                exp = exp[1:]
        else:
            exp = exp[min_pos] + left + right
    return brac(exp)

#This function is used to identify is two operators are together. If there are, then the it is further executed in the "stmin" function.
def neg(exp):
    if '*-' in exp:
        exp = stmin(exp, '*')
    elif '/-' in exp:
        exp = stmin(exp, '/')
    elif '^-' in exp:
        exp = stmin(exp, '^')
    elif '+-' in exp:
        exp = stmin(exp, '+')
    elif '--' in exp:
        exp = stmin(exp, '-')
    elif 'n-' in exp:
        exp = stmin(exp, 'n')
    elif 's-' in exp:
        exp = stmin(exp, 's')
    return exp

#This function checks if there are two or more '-' sign in an expression
def check(exp, pos_op):
    if '*' in exp:
        pos = exp.find('*')
        exp = exp[:pos-1] + '(' + exp[pos-1:] + ')'
        return brac(exp)
    minus = exp[pos_op]
    if '-' in exp[pos_op + 1:]:
        r = rgt(exp, pos_op)
        f = r.find(r)
        l = exp[:pos_op+1]
        l = len(l)
        rpos = len(r)
        if exp[pos_op + rpos + 1] == '-':
            s = rgt(exp, pos_op + rpos + 1)
            exp = exp[:pos_op] + minus + '(' + r + '+' + s + ')' + exp[pos_op + rpos + len(s)+2:]
    return brac(exp)

def cos(exp, pos_op): #Solves cos function
    soc = pos_op + 2
    cos = exp[pos_op:soc + 1]
    left = exp[:pos_op]
    if 's-' in exp:
        exp = left + cos + exp[soc+2:]
    cos_exp = rgt(exp, soc)
    min = pos_op - 1
    # if exp[min] == '-':
    #     exp = exp[:min] + cos + cos_exp
    if cos_exp == 'pi' or cos_exp == 'pi radians' or cos_exp == '3.14':
        cos_exp = '3.14'
        val = math.cos(float(cos_exp))
        val = math.floor(val)
    else:
        val = math.cos(float(cos_exp))
    return val

def sin(exp, pos_op): #Solves sin function
    nos = pos_op + 2
    sin = exp[pos_op:nos + 1]
    left = exp[:pos_op]
    sin_exp = rgt(exp, nos)
    # if exp[nos+3] == '-':

    if sin_exp == 'pi' or sin_exp == 'pi radians' or sin_exp == '3.14':
        sin_exp = '3.14'
        val = math.sin(float(sin_exp))
        val = math.floor(val)
    else:
        val = math.sin(float(sin_exp))
    return val

def evaluate(exp): #This is the function in which to expression actually executes
    if '*-' in exp or '/-' in exp or '^-' in exp or '--' in exp or '+-' in exp or 'n-' in exp:
        exp = neg(exp)
        if type(exp) is float:
            exp = str(exp)
    elif 's-' in exp:
        pos_op = exp.find('s-')
        exp = cos(exp, pos_op)

    if "+" in exp:
        pos_op = exp.find("+")
        left = exp.split("+")[0]
        right = exp[pos_op+1:]
        return evaluate(left) + evaluate(right)
    elif "-" in exp:
        pos_op = exp.find("-")
        count = 0
        for x in exp:
            if x == '-':
                count+=1
        if count>=2:
            return float(check(exp, pos_op))
        else:
            left = exp.split("-")[0]
            if left == '':
                left = '0'
            right = exp[pos_op + 1:]
            return evaluate(left) - evaluate(right)

    elif "*" in exp:
        pos_op = exp.find("*")
        left = exp.split("*")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) * evaluate(right)
    elif "/" in exp:
        pos_op = exp.find("/")
        left = exp.split("/")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) / evaluate(right)
    elif "^" in exp:
        pos_op = exp.find("^")
        left = exp.split("^")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) ** evaluate(right)
    elif 'cot' in exp:
        pos_op = exp.find('cot')
        cos_val = cos(exp, pos_op)
        sin_val = sin(exp, pos_op)
        cot_val = cos_val/sin_val
        return cot_val
    elif 'sec' in exp:
        pos_op = exp.find('sec')
        cos_val = cos(exp, pos_op)
        sec_val = 1/cos_val
        return sec_val
    elif 'cosec' in exp:
        pos_op = exp.find('cosec')
        c_pos = pos_op+4
        left = exp[:pos_op]
        right = exp[c_pos+1:]
        exp = left + 'sin' + right
        pos_op = exp.find('sin')
        sin_val = sin(exp, pos_op)
        cosec_val = 1/sin_val
        return cosec_val
    elif 'tan' in exp:
        pos_op = exp.find('tan')
        sin_val = sin(exp, pos_op)
        cos_val = cos(exp, pos_op)
        tan_val = sin_val/cos_val
        return tan_val
    elif 'cos' in exp:
        pos_op = exp.find('cos')
        cos_val = cos(exp, pos_op)
        return cos_val
    elif 'sin' in exp:
        pos_op = exp.find('sin')
        sin_val = sin(exp, pos_op)
        return sin_val
    else:
        return float(exp)

# inp = input("Enter an expression: ")
# if "(" in inp:
#     print(brac(inp))
# elif inp == '':
#     quit()
# else:
#     print(evaluate(inp))
