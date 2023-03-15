#!/usr/bin/python

class StateMachine(object):
  def __init__(self):
      self.handlers = {}
      self.startState = None
      self.endStates = []

  def add_state(self, name, handler, end_state=0):
      # name = name.upper()
      self.handlers[name] = handler
      if end_state:
           self.endStates.append(name)

  def set_start(self, name):
      self.startState = name

  def run(self, cargo):
      try:
         handler = self.handlers[self.startState]
      except:
         raise Exception('InitializationError, must call .set_start() before .run()')

      if not self.endStates:
         raise  Exception('InitializationError, at least one state must be an end_state')

      while True:
         # cargo should contain the data needed by the handler, like file handle
         newState, cargo = handler(cargo)
         if newState in self.endStates:
            break
         else:
            handler = self.handlers[newState]

################################################################################
# NOTES:
# First define your states and what you want to do at each state. In the
# example below, we want to do f1 while in STATE0, f2 while in STATE1, etc.
# Then, continue doing what it is supposed to do while at that state and
# inside that function. Then, determine the next state and return it together
# with what remains of the data/datasource
#
#
# Usage: cargo contains data. or it could be a file handle
#     from statemachines import StateMachine
#     def f1(cargo): # will be called for STATE0
#         do something with cargo, perhaps recalculate a new cargo
#         return ['STATE1', cargo]
#
#     def f2(cargo): # will be called for STATE1
#         do something with cargo, perhaps recalculate a new cargo
#         return ['STATE2', cargo]
#
#     def f3(cargo): # will be called for STATE2
#         do something with cargo, perhaps recalculate a new cargo
#         return ['STATE3', cargo]
#
#     def f4(cargo): # will be called for STATE3
#         do something with cargo, perhaps recalculate a new cargo
#         return ['STATE4', cargo]
#
#     if __name__ == '__main__':
#         m = StateMachine()
#         m.add_state('STATE0', f1)
#         m.add_state('STATE1', f2)
#         m.add_state('STATE2', f3)
#         m.add_state('STATE3', f4)
#         m.add_state('STATE4', None, end_state=True)
#         m.set_start('STATE0')
#         m.run(cargo)
################################################################################
