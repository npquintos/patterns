'''
    To use, use main below as a guide. In summary,
    1. Define which functions to call for which state. 'state'
        is an arbitrary string the new state you are in now and
        which function should be called when you reach this state.

    2. For every function you define in step 1 above,
        decorate them with:

        @StateMachine.Do('state name')

        replacing 'state name' with the name of the state that
        this function should respond to.

    3. Create a StateMachine instance.

    4. Invoke 'run' with the starting state passed, as well as
        cargo, the data container. This will automatically
        stop once state 'end' is encountered. There should be at
        least one function defined in step1 that will return
        ['end', cargo] or else, the state machine will not stop.
'''
class StateMachine:
    proc_given_state = {}
    @staticmethod
    def Do(event):
        def decorator(base_function):
            StateMachine.proc_given_state[event] = base_function
            def improved_function(*args, **kwargs):
                result = base_function(*args, **kwargs)
                return result
            return improved_function
        return decorator

    def run(self, state, cargo):
        while state != 'end':
            state, cargo = StateMachine.proc_given_state[state](cargo)

if __name__ == '__main__':
    ######### These are steps 1 to 2 #################
    @StateMachine.Do('first')
    def first_function(cargo): # state 'first'
        print(f"first_function called with cargo {cargo}, now calling third")
        cargo = 'AAA'
        return ['third', cargo]

    @StateMachine.Do('second')
    def second_function(cargo): # state 'second'
        print(f"second_function called with cargo {cargo}, now calling end")
        cargo = 'CCC'
        return ['end', cargo] ######### VERY IMPORTANT to have at least one
                              ######### returnung ['end', cargo]

    @StateMachine.Do('third')
    def third_function(cargo): # state 'third'
        print(f"third_function called with cargo {cargo}, now calling second")
        cargo = 'BBB'
        return ['second', cargo]
    ######## end of steps 1 to 2 ####################

    ######## step3 #########
    sm = StateMachine()
    ######## end of step3 #########

    ######## Step 4 ########
    cargo = '000'
    sm.run('first', cargo)

