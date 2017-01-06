import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The team Better Than Mine' # Only 10 chars displayed.
self = 'Shenanagins'
strategy_description = 'random choice'
def strategy(my_history, opponent_history, result, my_score, their_score):
    if not opponent_history:
        return 'c'


    if len(opponent_history) > (self.tournament_attributes['length'] - 3):
        return 'b'

    if len(opponent_history) < 180:
        if len(opponent_history) > 6:
            if 'b' not in opponent_history[:7]:
                 return 'C'

    else:

        return random.choice('b' or 'c')
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'.'''

'''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'
'''
    
