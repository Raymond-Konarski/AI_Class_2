# https://www.scirp.org/journal/PaperInformation?PaperID=90972&#abstract
from typing import Optional, List

from environments.connect_four import ConnectFourState, ConnectFour
import numpy as np


class Node:
    def __init__(self, state: ConnectFourState, score: int, parent, previous_move: int):
        self.state = state
        self.score: int = score
        self.parent: Optional[Node] = parent
        self.previous_move = previous_move


def heuristic(state: ConnectFourState) -> int:
    lines: List[np.ndarray] = state.get_lines()
    turn = state.player_turn
    for line in lines:
        val = 0
        if len(line) < 4: continue
        for idx, tile in enumerate(line):
            tmp1 = 0
            tmp2 = 0
            if tile > 0:
                tmp1 = tmp1 + 1
                tmp2 = 0
            elif tile == 0:
                tmp1 = 0
                tmp2 = 0
            elif tile < 0:
                tmp1 = 0
                tmp2 = tmp2 + 1
            val = tmp1 - tmp2
            # if tmp1 > 0:
            #     val = val + tmp1 * 3
            #     # if idx - 2 > 0:
            #     #     val = val + 2
            #     # if idx + 1 < len(line):
            #     #     val = val + 2
            # if tmp2 > 0:
            #     val = val - tmp2 * 3
            #     # if idx - 2 > 0:
            #     #     val = val - 5
            #     # if idx + 1 < len(line):
            #     #     val = val + 2
        return val

        # if idx == 0 or idx == len(line): pass  # TODO
    pass


# def negascout(node: Node, depth, a, b, turn: bool, env: ConnectFour, depth_limit: int) -> [int, int]:
#     state = node.state
#     if depth == 0 or state.is_terminal(): return (-heuristic(state)) if turn else heuristic(state)
#     if depth >= depth_limit: pass  # TODO: this
#     first = True
#     move = -1
#     for action in env.get_actions(state):
#         if first:
#             score = -negascout(env.next_state(state, action), depth - 1, -b, -a, ~turn, env, depth_limit)
#             first = False
#         else:
#             score = negascout(env.next_state(state, action), depth - 1, -a - 1, -a, ~turn, env, depth_limit)
#             if a < score < b:
#                 score = -negascout(env.next_state(state, action), depth - 1, -b, -a, ~turn, env, depth_limit)
#         a = max(a, score)
#         if a >= b:
#             move = action
#             break
#     return a, move


def min_value(state: ConnectFourState, env: ConnectFour, depth: int, max_depth: int) -> [float, float]:
    if env.is_terminal(state): return env.utility(state), -1
    if depth >= max_depth: heuristic(state), -1  # TODO: this
    v = np.inf
    m = -1
    for a in env.get_actions(state):
        v2, a2 = max_value(env.next_state(state, a), env, depth + 1, max_depth)
        if v2 < v:
            v, m = v2, a
    return v, m


def max_value(state: ConnectFourState, env: ConnectFour, depth: int, max_depth: int) -> [float, float]:
    if env.is_terminal(state): return env.utility(state), -1
    if depth >= max_depth: return heuristic(state), -1  # TODO: this
    v = -np.inf
    m = -1
    for a in env.get_actions(state):
        v2, a2 = min_value(env.next_state(state, a), env, depth + 1, max_depth)
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
    v, m = max_value(state, env, 0, 4)
    return m

    pass
