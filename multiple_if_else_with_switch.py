#!/usr/bin/python
''' Use this pattern when you have several if-elif that could be
    conveniently handled by switch statement
'''
################################################################################
# PATTERN
################################################################################

class Addition(object):
    def __init__(self, a):
        self.a = a
        self.func = {'add 1':self.add_1, 'add 2':self.add_2, 'add 3':self.add_3, 'add 4':self.add_4}

    def run(self, b):
        return self.func[b]()

    def add_1(self):
        return self.a + 1

    def add_2(self):
        return self.a + 2

    def add_3(self):
        return self.a + 3

    def add_4(self):
        return self.a + 4

print('using pattern')
selection = 'add 4'
a = 10
print(Addition(a).run(selection))

################################################################################
# Code to be replaced
################################################################################

print('\n\nusing ordinary approach')
selectior = 'add 4'
a = 10
if selection == 'add 1':
    a += 1
elif selection == 'add 2':
    a += 2
elif selection == 'add 3':
    a += 3
elif selection == 'add 4':
    a += 4
print(a)
