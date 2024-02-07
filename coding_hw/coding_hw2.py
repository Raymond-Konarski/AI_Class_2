from environments.connect_four import ConnectFourState, ConnectFour
import numpy as np


def heuristic(state: ConnectFourState) -> int:
    pass


# def negascout(state: ConnectFourState, depth, a, b, turn: bool, env: ConnectFour):
#     if depth == 0 or state.is_terminal():
#         return (-heuristic(state)) if turn else heuristic(state)
#     first = True
#     move = -1
#     for action in env.get_actions(state):
#         if first:
#             score = -negascout(env.next_state(state, action), depth - 1, -b, -a, ~turn, env)
#             first = False
#         else:
#             score = negascout(env.next_state(state, action), depth - 1, -a - 1, -a, ~turn, env)
#             if a < score < b:
#                 score = -negascout(env.next_state(state, action), depth - 1, -b, -a, ~turn, env)
#         a = max(a, score)
#         if a >= b:
#             move = action
#             break
#     return move


def min_value(state: ConnectFourState, env: ConnectFour, depth: int, max_depth: int) -> [int, int]:
    if env.is_terminal(state): return env.utility(state), None
    if depth >= max_depth: pass  # TODO: this
    v = np.inf
    m = None
    for a in env.get_actions(state):
        v2, a2 = max_value(env.next_state(state, a), env, depth + 1)
        if v2 > v:
            v, m = v2, a
    return v, m


def max_value(state: ConnectFourState, env: ConnectFour, depth: int, max_depth: int) -> [int, int]:
    if env.is_terminal(state): return env.utility(state), None
    if depth >= max_depth: pass  # TODO: this
    v = -np.inf
    m = None
    for a in env.get_actions(state):
        v2, a2 = min_value(env.next_state(state, a), env, depth + 1)
        if v2 > v:
            v, m = v2, a
    return v, m


def make_move(state: ConnectFourState, env: ConnectFour) -> int:
    """

    :param state: the current state
    :param env: the environment
    :return: the action to take
    """

    # player = state.player_turn
    v, m = max_value(state, env, 0, 18)
    actions = env.get_actions(state)
    return actions[0]

    pass
