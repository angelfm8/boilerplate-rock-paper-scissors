# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history = [], play_order = {}):
    
    n = 6
    acciones = ['R', 'P', 'S']
    respuestas = ['P', 'S', 'R']
    potential = {}
    guess = 'R'

    if not prev_play:
        opponent_history.append('R')
    else:
        opponent_history.append(prev_play)

    if len(opponent_history) >= n:
        if "".join(opponent_history[-(n):]) in play_order.keys():
            play_order["".join(opponent_history[-(n):])] += 1
        else:
            play_order["".join(opponent_history[-(n):])] = 1
    
        for i in acciones:
            potential["".join(opponent_history[-(n-1):])+ i] = 0 
        
        for i in potential.keys():
            if i in play_order.keys():
                potential[i] = play_order[i]
        
        prediction = max(potential, key = potential.get)[-1]
        guess = respuestas[acciones.index(prediction)]
    
    return guess