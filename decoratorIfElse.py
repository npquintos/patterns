''' This is intended to implement if-else using dictionary, with
    automatic dictionary update using a decorator

    usage pattern:
    say, you want to invoke process_event1 if "event1" happens,
    invoke process_event2 if "event2" happens,
    invoke process_event3 if "event3" happens,
    invoke process_event4 if "event4" happens, and so on ...
'''

# if-else dictionary container
function_given_event = {}

# this is the decorator to the decorator definition
# You can use it as is. Only thing you might have to
# change is the name 'function_given_event' and
# customize the name to your needs
def event_register(event):
    def decorator(base_function):
        function_given_event[event] = base_function
        def improved_function(*args, **kwargs):
            # global function_given_event
            result = base_function(*args, **kwargs)
            return result
        return improved_function
    return decorator

@event_register('event1')
def process_event1(event):
    return f"Event1:  {event}"

@event_register('event2')
def process_event2(event):
    return f"Event2:  {event}"

@event_register('event3')
def process_event3(event):
    return f"Event3:  {event}"

@event_register('event4')
def process_event4(event):
    return f"Event4:  {event}"

# Test if it works
for event, name in zip('xxx event3 event1 event4 event2'.split(), 'reading wedding birth death school'.split()):
    f = function_given_event.get(event)
    if f is None:
        continue
    result = f(name)
    print(f"{result}")





