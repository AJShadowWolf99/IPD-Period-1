####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Ragnarok'
strategy_name = 'Timesaver'
strategy_description = 'Collude if collude, perma betray if betray'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    if their_history[-1]=='b':
        return 'b'
    else:
        return 'c'           
