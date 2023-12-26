#include <string>
#include <tuple>
#include <iostream>
#include "include/statemachine_enum.hpp"

using namespace std;

/**   To use statemachine, 
 *    1.  define the functions that will be called for
 *        a given state. Below are those functions.
 *        -   first_step is called for state "start"
 *        -   second_step is called for state "second"
 *        -   third_step is called for state "third"
 *        -   If you need to terminate, return state "end"
 *        - NOTE: define these states as enums
 *    2.  On the body, add this functions and states using
 *        add() method of the instantiated statemachine instance.
 *        In the example below, that would be "sm". The 
 *        StateMachine is paremeterized with struct Cargo that holds
 *        the data or data stream to be processed. You have to
 *        define struct Cargo depending on your needs. 
 *        Place this Cargo definition on this main.
 *    3.  Start the statemachine by calling function "run",
 *        supplying it with the first state, in this case, "start",
 *        and the struct that will hold the data or data stream
 *        to be processed in struct Cargo. Below are
 *        more details of these steps.
**/


// STEP 1:
// Cargo is the data container to be passed around.
// Needs to define what it is. If you are parsing
// a file, Cargo must contain the file handle so that
// you could pass it around. So, define this structure
// accordingly depending on your needs. Note that when
// reading a file, the next state is usually dictated
// by the currently read line. Since it is inconvenient
// to push this line back to the file stream, save it
// as part of the Cargo structure so that the receiving
// function may be able to read it again.

using Cargo = struct { int x; };

// STEP 2:
// Need to parametize StateAndData
// All it does is define that the "Data" part of "StateAndData"
// is carrying data taype "Cargo" which we just
// defined in STEP 1 above
// The 'first_step', 'second_step' and 'third_step'
// defined below are the procedures to be called for
// a given state. They return the next 'state' and
// data container 'Cargo', hence, data type StateAndData
// "StateAndData" is defined in statemachine.hpp

StateAndData<Cargo> first_step(Cargo);
StateAndData<Cargo> second_step(Cargo);
StateAndData<Cargo> third_step(Cargo);

// STEP 3:
// Define the functions declared above; take note
// of the function signatures. These are the 
// procedures to be done at that state until the
// need to transition to a new state is detected.
// Then, the next state it should go, plus the
// data container 'cargo' is returned as tuples
// at this point, you need to define enums that will
// correspond to the states. Use namespace to avoid
// vaviable pollution
//
namespace MyState {
    enum state {start, second, third, end};
}

StateAndData<Cargo> first_step(Cargo cargo) // procedure for StateMachine::start state
{
  std::cout << "first step, cargo is " << cargo.x << std::endl;
  cargo.x = 2;
  return std::make_tuple(MyState::third, cargo);
}

StateAndData<Cargo> second_step(Cargo cargo) // procedure for state StateMachine::second
{
  std::cout << "second step, cargo is " << cargo.x << std::endl;
  cargo.x = 3;
  return std::make_tuple(MyState::end, cargo);
}

StateAndData<Cargo> third_step(Cargo cargo) // procedure for state StateMachine::third
{
  std::cout << "third step, cargo is " << cargo.x << std::endl;
  cargo.x = 4;
  return std::make_tuple(MyState::second, cargo); // "end" marks end of the steps
}

// STEP 4: See STEP 4 in the main.
// The 'states' and 'functions' are registered
// to the statemachine for eventual running in STEP 5

int main()
{
    Cargo c;
    c.x = 1;
    StateMachine<Cargo, 3> sm = StateMachine<Cargo, 3>();

    // add the procedures to call for a given "state"
    // This is STEP 4
    sm.add(MyState::start, first_step);
    sm.add(MyState::second, second_step);
    sm.add(MyState::third, third_step);
    // for the 'end' state, function call is irrelevant
    // because it will never be called, hence, it could
    // be anything; just dont forget the third argument 'true'
    sm.add(MyState::end, third_step, true);

    // STEP 5:
    // then run it. If, at any point in the procedure,
    // you need to end the process, send "end" as
    // the next state. Notice that "end" is returned
    // after the second_step above, assuming that
    // no more processing is needed after that.
    // You have to state the "start" state. It could
    // be another name, like "abcd". For example, if
    // the procedure you want at the start is "start_here"
    // then, you should say sm.add("abcd", start_here) and
    // then, invoke 'sm.run("abcd", c)'. However, when
    // you want to terminate the statemachine, you should
    // ALWAYS use "end" as the next state if you want to
    // terminate; contents of cargo does not matter at
    // this stage
    sm.run(MyState::start, c);
}
