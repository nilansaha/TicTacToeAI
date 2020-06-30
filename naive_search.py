import numpy as np
from copy import deepcopy
from tictactoe import TicTacToe
from collections import defaultdict

def search_tree(env):
    action_space = env.available_moves()
    if len(action_space) == 0:
        return [env.move_history + [env.winner]]
    else:
        moves = []
        for action in action_space:
            current_env = deepcopy(env)
            current_env.move(action)
            moves.extend(search_tree(current_env))
        return moves

def evaluate(env, moves):
    perspective = 1 - env.turn
    move_stats = defaultdict(lambda: defaultdict(int))
    for move in moves:
        idx = move[len(env.move_history)]
        move_stats[idx]['total'] += 1
        if move[-1] == perspective:
            move_stats[idx]['win'] += 1
        elif move[-1] == 1 - perspective:
            move_stats[idx]['loss'] += 1
        else:
            move_stats[idx]['draw'] += 1
    best_win, best_draw = -float('inf'), -float('inf')
    win_move, draw_move = None, None
    for move, stats in move_stats.items():
        win_p = stats['win']/stats['total']
        draw_p = stats['draw']/stats['total']
        if win_p > best_win:
            best_win = win_p
            win_move = move
        if draw_p > best_draw:
            best_draw = draw_p
            draw_move = move
    if best_win >= best_draw:
        return win_move
    else:
        return draw_move

if __name__ == '__main__':
    env = TicTacToe()
    env.move(0)
    env.move(2)
    env.move(1)
    env.move(5)
    env.move(6)
    env.render()
    moves = search_tree(env)
    print('Best Move', evaluate(env, moves))
