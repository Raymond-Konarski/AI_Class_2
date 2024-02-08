# Raymond Konarski 2024
# https://www.scirp.org/journal/PaperInformation?PaperID=90972&#abstract heuristic ideas
# http://blog.gamesolver.org/solving-connect-four/01-introduction/ didn't really help...
# https://en.wikipedia.org/wiki/Negamax#Negamax_with_alpha_beta_pruning great images to visualize alpha-beta pruning
from typing import Optional, List, Dict

from environments.connect_four import ConnectFourState, ConnectFour
import numpy as np


def heuristic(state: ConnectFourState) -> int:
    lines: List[np.ndarray] = state.get_lines()
    val = 0
    for line in lines:
        if len(line) < 4: continue
        for idx, tile in enumerate(line):
            tmp1 = 0
            tmp2 = 0
            if tile > 0:
                tmp1 += 1
                tmp2 = 0
            elif tile == 0:
                tmp1 = 0
                tmp2 = 0
            elif tile < 0:
                tmp1 = 0
                tmp2 += 1
            val += tmp1 - tmp2
    return val


def negamax(state: ConnectFourState, env: ConnectFour, depth: int, turn: int, a, b) -> [float, int]:
    if state.is_terminal:
        return turn * env.utility(state), -1
    elif depth == 0:
        return turn * heuristic(state), -1
    v = -np.inf
    m = 2
    for action in env.get_actions(state):
        v2, _ = negamax(env.next_state(state, action), env, depth - 1, -turn, -b, -a)
        if -v2 > v:
            v, m = -v2, action
        if a >= b: break
    return v, m


def make_move(state: ConnectFourState, env: ConnectFour) -> int:
    """

    :param state: the current state
    :param env: the environment
    :return: the action to take
    """

    # tTable: Dict[ConnectFourState, int] = {} # how do i even memoize with alpha-beta pruning...
    _, m = negamax(state, env, 5, state.player_turn, -np.inf, np.inf)

    return m

    pass
