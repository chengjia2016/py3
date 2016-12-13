import re




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


s = '2x'
varx=re.sub('(?P<value>\d[x|y|z]+)', addx, s)
varx=re.sub('=','==',varx)

