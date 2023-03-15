''' This is a general framework for handling multiple if-else statements.
    Usage:
        1.  Define arrays of tests and returns

                tests_and_returns   = [
                        test1,  return1,
                        test2,  return2,
                        test3,  return3,
                        ...
                        test-k, return-k
                        True,   return_value_for_default_catch_all
                        ]

            In most general terms, test-k is a function that do tests and return-k are those
            functions that calculate returned value when test-k is true. The last entry should
            be the catch-all condition.

        2.  Then, create an instance of GeneralIfElse

            gimme_result = GeneralIfElse(tests_and_returns)

        3.  Use it

            value = gimme_result(3) <-- this will test 3 for conditions and evaluate the
                                        value for the matching condition.
'''
from inspect import isfunction

class GeneralIfElse(object):
    def __init__(self, tests_and_returns):
        self.tests = tests_and_returns[::2]
        self.returns = tests_and_returns[1::2]
        self.condition = {'F':self.evaluate_function, 'C':self.evaluate_const, 'B':self.evaluate_bool}
        self.rreturn = {'F':self.evaluate_function, 'C':self.return_const, 'B':self.evaluate_bool}
        self.range_based_test = all((type(x) == int or type(x) == float) for x in self.tests[:-1])

    def __call__(self, x):
        if self.range_based_test:
            return self.call_for_range_based(x)
        else:
            return self.call_for_non_range_based(x)

    def call_for_non_range_based(self, x):
        for t, r in zip(self.tests, self.returns):
            if self.condition[self.test_type(t)](t, x):
                return self.rreturn[self.test_type(r)](r, x)

    def call_for_range_based(self, x):
        for t, r in zip(self.tests, self.returns):
            if (type(t) == bool and t) or x < t:
                return self.rreturn[self.test_type(r)](r, x)

    def evaluate_function(self, f, arg):
        return f(arg)

    def evaluate_const(self, f, arg):
        return f == arg

    def evaluate_bool(self, f, arg):
        return f

    def return_const(self, r, arg):
        return r

    def test_type(self, x):
        if isfunction(x):
            return 'F' # is a function
        elif type(x) == bool:
            return 'B'
        else:
            return 'C' # a constant


if __name__ == '__main__':
################################################################################
    # GeneralIfElse sample usage
    print('this is general usage')

    def f(x):
        return 'a'*x

    def g(x):
        return x*x

    def divisible_by_40(x):
        if x % 40:
            return False
        return True

    tests_and_returns = [
            # Tests,            Return value or Function to call when test is true
            lambda x: x<3,      'less than 3',
            lambda x: 3<=x<7,   'between 3 and 7',
            lambda x: 7<=x<20,  f,
            divisible_by_40,     g,
            lambda x: x>=100,   5000,
            True,               'This is the catchall default'
            ]

    gimme_result = GeneralIfElse(tests_and_returns)
    print('100', gimme_result(100))
    print('2', gimme_result(2))
    print('5', gimme_result(5))
    print('120', gimme_result(120))
    print('11', gimme_result(11))
    print('78', gimme_result(78))

    # GeneralIfElse sample usage END
################################################################################
# This example is for more common use where you are checking for range and the
    # decision is based on which range you fell.

    print('This is range-based usage')

    def teenager(x):
        return 'you are a teenager of age %s' % (x)

    def medium_age(x):
        return 'you should save for retirement. Age %s is too old!' % (x)

    tests_and_returns = [
            3,          'newborn',
            6,          'toddler',
            13,         'pre-teen',
            20,         teenager,
            50,         medium_age,
            True,       'you are outside the calendar'
            ]

    age_definition = GeneralIfElse(tests_and_returns)
    print('1', age_definition(1))
    print('4', age_definition(4))
    print('11', age_definition(11))
    print('15', age_definition(15))
    print('30', age_definition(30))
    print('100', age_definition(100))
