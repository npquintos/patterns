#include <array>
#include <tuple>
#include <string>
using namespace std;

template <typename T>
using StateAndData = tuple<int, T>;

template <typename T>
using StateProcedure = StateAndData<T> (*)(T);

template <typename T, std::size_t sz>
class StateMachine {
    std::array<StateProcedure<T>, sz> proc_given_state;
    int endState{0};
    public:
        void add(int i, StateProcedure<T> func_ptr, bool end_state=false) {
            proc_given_state[i] = func_ptr;
            if (end_state)
                endState = i;
        };
        void run(int state, T cargo) {
            do {
                tie(state, cargo) = proc_given_state[state](cargo);
            } while (state != endState);
        };
};
