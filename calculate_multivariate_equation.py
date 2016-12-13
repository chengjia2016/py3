import re
import os


"""
<<<<<<<<<<<<<<<<<<<<<<<
    calculate Multivariate equation
    use integer only
    unknown number max is 6
    etc: x,y,z,a,b,c
    value max is -5000,5000
    def value is -10,10
    by zend@yeah.net
<<<<<<<<<<<<<<<<<<<<<<<

"""

x,y,z,a,b,c=0,0,0,0,0,0
x1,y1,z1,a1,b1,c1=0,0,0,0,0,0
maxv=10




def sp(matched):
    #print(matched)
    #matchObj = re.match(r'\d[^0-9]', matched)
    #print(matchObj)
    vbd = re.sub('\d', "", matched)
    vbD= re.sub('\D', "", matched)

    vb=vbD+"*"+vbd

    return str(vb)


def addx(matched):
    value = matched.group('value')
    return sp(value)



def strin(v,x):
    if (x in v):
        return True
    else:
        return False



def to_human_equation(v):
    varx = re.sub('(?P<value>\d[x|y|z]+)', addx, v)
    varx = re.sub('=', '==', varx)
    return varx


def cme(*v):
    newlist=[]
    global x1,y1,z1,a1,b1,c1
    for m in range(0,len(v)):
        if(strin(v[m],"x")):
            x1 = 1

    for m in range(0,len(v)):
        if (strin(v[m], "y")):
            y1 = 1

    for m in range(0,len(v)):
        if (strin(v[m], "z")):
            z1 = 1

    for m in range(0,len(v)):
        if (strin(v[m], "a")):
            a1 = 1

    for m in range(0,len(v)):
        if (strin(v[m], "b")):
            b1 = 1

    for m in range(0,len(v)):
        if (strin(v[m], "c")):
            c1 = 1

    for m in range(0,len(v)):
        #print(v[m])

        newlist.append(to_human_equation(v[m]))
        #print(to_human_equation(v[m]))
        #print(newlist)

    print(newlist)
#    global x1,y1,z1
    r_num = 1
    total=0


    for x in range(-maxv,maxv):
        for y in range(-maxv,maxv):
            for z in range(-maxv,maxv):
                total=total+1
                if(len(newlist)==1):
                    if (eval(newlist[0])):
                        print("----在", r_num, "次计算后得出这个解----")
                        print("x:", x)
                        print("y:", y)
                        print("z:", z)
                        r_num=r_num+1
                        #os._exit(0)
                if (len(newlist) == 2):
                    if (eval(newlist[0]) and eval(newlist[1])):
                        print("----在", r_num, "次计算后得出这个解----")
                        print("x:", x)
                        print("y:", y)
                        print("z:", z)
                        r_num = r_num+1
                        #os._exit(0)
                if (len(newlist) == 3):
                    if (eval(newlist[0]) and eval(newlist[1]) and eval(newlist[2])):
                        print("----在", r_num, "次计算后得出这个解----")
                        print("x:", x)
                        print("y:", y)
                        print("z:", z)
                        r_num = r_num+1
                        #os._exit(0)
    return  total
# human Multivariate equation
print(cme("x+y+z=6","2x+y+z=7"))





