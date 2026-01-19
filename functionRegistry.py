#!/usr/bin/python3

r'''
Usage: use the decorator on those functions that
    will be used given an 'event'. This builds
    a dictionary of functions with 'event' as
    key. Very useful to avoid using a lot of if-else.
    See main below on sample usage:
    The equivalent code is:

def process_event1(arg):
    return f"Event1: {arg}"

def process_event2(arg):
    return f"Event2: {arg}"

def process_event3(arg):
    return f"Event3: {arg}"

def process_event4(arg):
    return f"Event4: {arg}"

def process_event(event, arg):
    if event == 'event1':
        return process_event1(arg)
    elif event == 'event2':
        return process_event2(arg)
    elif event == 'event3':
        return process_event3(arg)
    elif event == 'event4':
        return process_event4(arg)
    else:
        return f"No function to process event {event}"

for event, arg in zip('xxx event3 event1 event4 event2'.split(), 'reading wedding birth death school'.split()):
    result = Registry.execute(event, arg)
    print(f'{event=} {result=}')

The advantage of the solution below is that, say, you want to add a function for event 'endOfTheWorld' called
bailOut, all you need to do is add code below and that is all you need. No need to add the event checking
in 'process_event' as in above

@Registry.register('endOfTheWorld')
def bailOut(arg):
    return f"Ignore {arg}. it is end of the world and would not matter"

'''

class Registry:
    function = {}
    @staticmethod
    def register(event):
        def decorator(base_function):
            Registry.function[event] = base_function
            def improved_function(*args, **kwargs):
                result = base_function(*args, **kwargs)
                return result
            return improved_function
        return decorator

    @staticmethod
    def execute(event, *args, **kwargs):
        fx = Registry.function.get(event)
        if fx is None:
            return f"No function to process event {event}"
        return fx(*args, **kwargs)

if __name__ == '__main__':
    @Registry.register('event1')
    def process_event1(arg):
        return f"Event1: {arg}"

    # code below is for both 'event2'
    # and 'event22' to use same function
    @Registry.register('event2')
    @Registry.register('event22')
    def process_event2(arg):
        return f"Event2: {arg}"

    @Registry.register('event3')
    def process_event3(arg):
        return f"Event3: {arg}"

    # code below is for both 'event43'
    # and 'event4' to use same function
    @Registry.register('event43')
    @Registry.register('event4')
    def process_event4(arg):
        return f"Event4: {arg}"

    for event, arg in zip('xxx event43 event3 event1 event4 event2 event22'.split(), 'reading child43 wedding birth death school catch22'.split()):
        result = Registry.execute(event, arg)
        print(f'{event=} {result=}')





