import numpy as np
from copy import deepcopy
from tictactoe import TicTacToe
from collections import defaultdict

def search(env, iterations):
    perspective = 1 - env.turn
    move_stats = defaultdict(lambda: defaultdict(int))
    for _ in range(iterations):
        current_env = deepcopy(env)
        while 1:
            action_space = current_env.available_moves()
            action = np.random.choice(action_space, 1)[0]
            result = current_env.move(action)
            if result[0] == True:
                required_moves = current_env.move_history[len(env.move_history):]
                next_move = current_env.move_history[len(env.move_history)]
                move_stats[next_move]['total'] += 1
                if result[1] == perspective:
                    move_stats[next_move]['win'] += 1
                elif result[-1] == 1 - perspective:
                    move_stats[next_move]['loss'] += 1
                else:
                    move_stats[next_move]['draw'] += 1
                current_env.reset()
                break
    max_prob, best_move = -float('inf'), None
    for move, stats in move_stats.items():
        win_prob = stats['win']/stats['total']
        loss_prob = stats['loss']/stats['total']
        if  win_prob > max_prob and win_prob > loss_prob:
            max_prob = win_prob
            best_move = move
    if best_move == None:
        least_loss = float('inf')
        for move, stats in move_stats.items():
            loss_prob = stats['loss']/stats['total']
            if loss_prob < least_loss:
                least_loss = loss_prob
                best_move = move
    return best_move 

if __name__ == '__main__':
    env = TicTacToe()
    env.move(5)
    env.move(0)
    env.move(2)
    env.move(1)
    env.move(7)
    env.render()
    move = search(env, 2000)
    print('Best Move', move)
