def stackless_recursive_function(initial_accumulator, initial_data, initial_counter)
    register = [[initial_accumulator, initial_data, initial_counter]]
    while True:
        if not register:
            break
        accum, data, counter = register.pop()
        new_counter = calculate_new_counter(accum, data, counter)
        if should_stop(accum, data, counter):
            break
        new_accum = calculate_new_accum(accum, data, counter)
        new_data = calculate_new_data(accum, data, counter)
        register.push(new_accum, new_data, new_counter)
    return new_accum
