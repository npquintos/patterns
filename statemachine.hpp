#include <unordered_map>
#include <tuple>
#include <string>
using namespace std;

template <typename T>
using StateAndData = tuple<std::string, T>;

template <typename T>
using StateProcedure = StateAndData<T> (*)(T);

template <typename T>
class StateMachine {
    unordered_map<string, StateProcedure<T>> proc_given_state;
    public:
        void add(string s, StateProcedure<T> func_ptr) {
            proc_given_state[s] = func_ptr;
        };
        void run(string state, T cargo) {
            do {
                tie(state, cargo) = proc_given_state[state](cargo);
            } while (state != "end");
        };
        StateMachine() {
            std::unordered_map<string, StateProcedure<T>> proc_given_state;
        };
        ~StateMachine() {};
};
