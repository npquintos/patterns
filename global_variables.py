# instead of having several global variables, declare
# just one (object) and use attributes. In that way, it is
# easier to track the global variables and you also need not
# pass a lot of parameters to a function calls
def f1():
    global g
    g.d = {}
    g.d['a'] = 'at f1'
    f2()
    print('at f1', g.t)

def f2():
    global g
    # create a new dict t
    g.t = {}
    g.t['b'] = 'at f2'
    # access the dict created from the calling function
    g.t['a'] = g.d['a']

class G(object):
    pass

g = G
f1()
print('at main')
print(g.d)
print(g.t)

# instead of

def f1():
    global d
    d['a'] = 'at f1'
    f2()
    print('at f1,', t)

def f2():
    global t
    t['b'] = 'at f2'
    t['a'] = d['a']

d = {}
t = {}
f1()
print('at main')
print(d)
print(t)

