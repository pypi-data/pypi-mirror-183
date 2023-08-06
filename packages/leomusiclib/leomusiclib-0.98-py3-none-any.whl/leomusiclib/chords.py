import leomusiclib.intervals as i
def T3_up(a):
    b = a;c = a
    d = i.b3_up(y)
    return(a,b,c,d)
def t3_up(a):
    b = a;c = a
    d = i.m3_up(y)
    return(a,b,c,d)
def t53_up(x):
    y = i.m3_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def T53_up(x):
    y = i.b3_up(x)
    z = i.m3_up(y)
    return(x,y,z)
def T53r1_up(a):
    b = a;c = i.b3_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
def T53r2_up(a):
    b = i.b3_up(b)
    c = i.m3_up(c)
    d = a
    return(a,b,c,d)
def t53r1_up(a):
    b = a;c = i.m3_up(b)
    d = i.b3_up(c)
    return(a,b,c,d)
def t53r2_up(a):
    b = i.m3_up(b)
    c = i.b3_up(c)
    d = a
    return(a,b,c,d)
def T6_up(x):
    y = i.m3_up(x)
    z = i.ch4_up(y)
    return(x,y,z)
def T6r_up(a):
    b = i.m3_up(a)
    c = i.ch4_up(b)
    d = c
    return(a,b,c,d)
def T64_up(x):
    y = i.ch4_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def t6_up(x):
    y = i.b3_up(x)
    z = i.ch4_up(y)
    return(x,y,z)
def t64_up(x):
    y = i.ch4_up(x)
    z = i.m3_up(y)
    return(x,y,z)

def s53_up(x):
    y = i.m3_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def S53_up(x):
    y = i.b3_up(x)
    z = i.m3_up(y)
    return(x,y,z)
def S6_up(x):
    y = i.m3_up(x)
    z = i.ch4_up(y)
    return(x,y,z)
def S64_up(x):
    y = i.ch4_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def s6_up(x):
    y = i.b3_up(x)
    z = i.ch4_up(y)
    return(x,y,z)
def s64_up(x):
    y = i.ch4_up(x)
    z = i.m3_up(y)
    return(x,y,z)

def d7_up(a):
    b = i.b3_up(a)
    c = i.m3_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
def d65_up(a):
    b = i.m3_up(a)
    c = i.m3_up(b)
    d = i.b2_up(c)
    return(a,b,c,d)
def d43_up(a):
    b = i.m3_up(a)
    c = i.b2_up(b)
    d = i.b3_up(c)
    return(a,b,c,d)
def d2_up(a):
    b = i.b2_up(a)
    c = i.b3_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
def vii7_up(a):
    b = i.m3_up(a)
    c = i.m3_up(b)
    d = i.b3_up(c)
    return(a,b,c,d)
def vii65_up(a):
    b = i.m3_up(a)
    c = i.b3_up(b)
    d = i.b2_up(c)
    return(a,b,c,d)
def vii43_up(a):
    b = i.b3_up(a)
    c = i.b2_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
def vii2_up(a):
    b = i.b2_up(a)
    c = i.m3_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
#ton
def s53_ton(t):
    x = t
    y = i.m3_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def S53_ton(t):
    x = t
    y = i.b3_up(x)
    z = i.m3_up(y)
    return(x,y,z)
def S6_ton(t):
    x = t
    y = i.m3_up(x)
    z = i.ch4_up(y)
    return(x,y,z)
def S64_ton(t):
    x = t
    y = i.ch4_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def s6_ton(t):
    x = t
    y = i.b3_up(x)
    z = i.ch4_up(y)
    return(x,y,z)
def s64_ton(t):
    x = t
    y = i.ch4_up(x)
    z = i.m3_up(y)
    return(x,y,z)

def T3_ton(t):
    a = t
    b = a;c = a
    d = i.b3_up(a)
    return(a,b,c,d)
def t3_ton(t):
    a = t
    b = a;c = a
    d = i.m3_up(a)
    return(a,b,c,d)
def t53_ton(t):
    x = t
    y = i.m3_up(x)
    z = i.b3_up(y)
    return(x,y,z)
def T53_ton(t):
    x = t
    y = i.b3_up(x)
    z = i.m3_up(y)
    return(x,y,z)
def T53r1_ton(t):
    a = t
    b = a;c = i.b3_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
def T53r2_ton(t):
    a = t
    b = i.b3_up(b)
    c = i.m3_up(c)
    d = a
    return(a,b,c,d)
def t53r1_ton(t):
    a = t
    b = a;c = i.m3_up(b)
    d = i.b3_up(c)
    return(a,b,c,d)
def t53r2_ton(t):
    a = t
    b = i.m3_up(b)
    c = i.b3_up(c)
    d = a
    return(a,b,c,d)
def T6_ton(t):
    x = t
    y = i.ch4_down(x)
    z = i.m3_down(y)
    return(z,y,x)
def T6r_ton(t):
    a = t
    b = i.ch4_down(a)
    c = i.m3_down(b)
    d = a
    return(c,b,d,a)
def T64_ton(t):
    x = t
    y = i.ch4_down(x)
    z = i.b3_up(y)
    return(y,x,z)
def t64_ton(t):
    x = t
    y = i.ch4_down(x)
    z = i.m3_up(y)
    return(y,x,z)
def t6_ton(t):
    x = t
    y = i.ch4_down(x)
    z = i.b3_down(y)
    return(z,y,x)

def d7_ton(t):
    a = t
    b = i.b3_up(a)
    c = i.m3_up(b)
    d = i.m3_up(c)
    return(a,b,c,d)
def d65_ton(t):
    a = t
    d = i.b2_down(a)
    c = i.m3_down(d)
    b = i.m3_down(c)
    return(b,c,d,a)
def d43_ton(t):
    a = t
    b = i.b3_up(a)
    c = i.b2_down(a)
    d = i.m3_down(c)
    return(d,c,a,b)
def d2_ton(t):
    a = t
    b = i.b2_down(a)
    c = i.b3_up(a)
    d = i.m3_up(c)
    return(b,a,c,d)
def vii7_ton(t):
    a = t
    b = i.m3_up(a)
    c = i.m3_up(b)
    d = i.b3_up(c)
    return(a,b,c,d)
def vii65_ton(t):
    a = t
    d = i.b2_down(a)
    c = i.b3_down(d)
    b = i.m3_down(c)
    return(b,c,d,a)
def vii43_ton(t):
    a = t
    c = i.b2_down(a)
    b = i.b3_down(c)
    d = i.m3_up(a)
    return(b,c,a,d)
def vii2_ton(t):
    a = t
    b = i.b2_down(a)
    c = i.m3_up(a)
    d = i.m3_up(c)
    return(b,a,c,d)
#down
def t3_down(a):
    b = a;c = a
    d = i.m3_down(y)
    return(a,b,c,d)
def T3_down(a):
    b = a;c = a
    d = i.b3_down(y)
    return(a,b,c,d)
def T53_down(x):
    y = i.b3_down(x)
    z = i.m3_down(y)
    return(x,y,z)
def t53_down(x):
    y = i.m3_down(x)
    z = i.b3_down(y)
    return(x,y,z)
def T6_down(x):
    y = i.ch4_down(x)
    z = i.m3_down(y)
    return(x,y,z)
def T64_down(x): 
    y = i.b3_down(x)
    z = i.ch4_down(y)
    return(x,y,z)
def t6_down(x):
    y = i.ch4_down(x)
    z = i.b3_down(y)
    return(x,y,z)
def t64_down(x):
    z = i.m3_down(y)
    y = i.ch4_down(x)
    return(x,y,z)

def S53_down(x):
    y = i.b3_down(x)
    z = i.m3_down(y)
    return(x,y,z)
def s53_down(x):
    y = i.m3_down(x)
    z = i.b3_down(y)
    return(x,y,z)
def S6_down(x):
    y = i.ch4_down(x)
    z = i.m3_down(y)
    return(x,y,z)
def S64_down(x): 
    y = i.b3_down(x)
    z = i.ch4_down(y)
    return(x,y,z)
def s6_down(x):
    y = i.ch4_down(x)
    z = i.b3_down(y)
    return(x,y,z)
def s64_down(x):
    z = i.m3_down(y)
    y = i.ch4_down(x)
    return(x,y,z)

def d7_down(a):
    b = i.m3_down(a)
    c = i.m3_down(b)
    d = i.b3_down(c)
    return(a,b,c,d)
def d65_down(a):
    b = i.b2_down(a)
    c = i.m3_down(b)
    d = i.m3_down(c)
    return(a,b,c,d)
def d43_down(a):
    b = i.b3_down(a)
    c = i.b2_down(b)
    d = i.m3_down(c)
    return(a,b,c,d)
def d2_down(a):
    b = i.m3_down(a)
    c = i.b3_down(b)
    d = i.b2_down(c)
    return(a,b,c,d)
def vii7_down(a):
    b = i.b3_down(a)
    c = i.m3_down(b)
    d = i.m3_down(c)
    return(a,b,c,d)
def vii65_down(a):
    b = i.b2_down(a)
    c = i.b3_down(b)
    d = i.m3_down(c)
    return(a,b,c,d)
def vii43_down(a):
    b = i.m3_down(a)
    c = i.b2_down(b)
    d = i.b3_down(c)
    return(a,b,c,d)
def vii2_down(a):
    b = i.m3_down(a)
    c = i.m3_down(b)
    d = i.b2_down(c)
    return(a,b,c,d)