team_name = 'Strawberry mango'
strategy_name = 'Revenge'
strategy_description = '''\
It will collude until betrayed after that it will only betray.'''
    
def move(my_history, their_history, my_score, their_score):

    if 'b' in their_history:
        return 'b'
    else:
        return 'c'
        
