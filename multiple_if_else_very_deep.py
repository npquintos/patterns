#/usr/bin/python
''' If you have a series of if-elif statement that is very
    deep, each if and else have their own if and else, this
    may be the way to go.

    it is something like
    if c1:
        if c2:
            if c3:
                do1
            else:
                do2
        else:
            if c4:
                do3
            else:
                do4
    else:
        if c5:
            if c6:
                do5
            else:
                do6
        else:
            if c7:
                do7
            else:
                do8

    In the example below, you are trying to provide gift
    recommendations. This means, it would be different
    for men and women, different for different age brackets,
    and say, finally, different if sports oriented

    There are 3 parts to fill up as shown in the example below:
    1.  Template
    2.  Conditions part composed of word generator and individual evaluation
    3.  Evaluation for individual conditions
'''
################################################################################
# This is using the pattern
################################################################################

class Recommend(object):
    # start of TEMPLATE ###############################################################
    def __init__(self):
        # sequence below follows the following convention. m = men, w=women
        # f = below 40yrs F=above 40yrs, s=sports oriented, S=not sports oriented
        # so, a word like wFS would mean a woman above 40yrs that is not sports oriented
        # The trick is to assign a function to each of this word, and another function
        # to create the word. The word and function name should match to avoid
        # having to create a dict
        # look at the 3 parts below
        pass

    def __call__(self, sex, age, sports_oriented):
        return self.__getattribute__(self.create_word(sex, age, sports_oriented))(sex, age, sports_oriented)
    # end of TEMPLATE #################################################################

    # start of CONDITIONS  ############################################################
    # WORD generator
    def create_word(self, sex, age, sports_oriented):
        return self.check_sex(sex)+self.check_age(age)+self.check_sport(sports_oriented)

    # below are where the individual conditions are evaluated
    def check_sex(self, sex):
        return 'm' if sex=='man' else 'w'

    def check_age(self, age):
        return 'f' if age<40 else 'F'

    def check_sport(self, sports_oriented):
        return 's' if sports_oriented=='yes' else 'S'
    # end of CONDITIONS  #############################################################

    # start of evaluation of individual CONDITIONS  ##################################
    def mfs(self, age, sex, sports_oriented):
        return 'man below forty sports oriented'

    def wfs(self, age, sex, sports_oriented):
        return 'women below forty sports oriented'

    def mFs(self, age, sex, sports_oriented):
        return 'man over 40 sports oriented'

    def wFs(self, age, sex, sports_oriented):
        return 'women over 40 sports oriented'

    def mfS(self, age, sex, sports_oriented):
        return 'man below 40 not sports oriented'

    def wfS(self, age, sex, sports_oriented):
        return 'women below 40 not sports oriented'

    def mFS(self, age, sex, sports_oriented):
        return 'man over 40 not sports oriented'

    def wFS(self, age, sex, sports_oriented):
        return 'woman over 40 not sports oriented'
    # end of evaluation of individual CONDITIONS  ####################################

print('using the pattern')
r = Recommend()
print(r('man', 32, 'no'))
print(r('woman', 26, 'yes'))
print(r('man', 50, 'yes'))
print(r('woman', 32, 'no'))
