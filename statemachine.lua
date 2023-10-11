 return {
    StateMachine = {
	    sm = {},
	    __index = {
		    add = function(xstate, xfunction)
				    m.StateMachine.sm[xstate] = xfunction
			  end,
		    run = function(current_state, cargo)
				    repeat
					    next_state = m.StateMachine.sm[current_state](cargo)
					    current_state = next_state[1]
					    cargo = next_state[2]
				    until current_state == 'end'
			  end,
	    },
    },
    add_state = function(state, xfunction)
			dummy = {state = state, xfunction = xfunction}
			setmetatable(dummy, m.StateMachine)
			dummy.add(state, xfunction)
			return dummy
                end,

}

