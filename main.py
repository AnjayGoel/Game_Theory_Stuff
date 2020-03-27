import numpy as np
import traceback

arr = np.zeros((3, 3), dtype=int)
cons = (-3, 3)
counter = 0


class Node:
    def __init__(self, state, p_type):
        global counter
        counter += 1
        self.value = 0
        self.p_type = p_type
        self.state = state
        self.nodes = {}
        self.opt_next = None
        if is_filled(state) or cal_val(state) is not None:
            return
        for i in empty(state):
            state_n = np.copy(state)
            state_n[int(i / 3)][i % 3] = p_type
            self.nodes[i] = Node(state_n, -1 * p_type)


def is_filled(state) -> bool:
    for i in state:
        for j in i:
            if j == 0:
                return False
    return True


def empty(state) -> list:
    ret_val = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                ret_val.append(i * 3 + j)
    return ret_val


def cal_val(state):
    depth = len(empty(state))
    for i in range(3):
        if sum(state[i]) in cons:
            return int(sum(state[i]) / 3)*(1.0+depth)/10
        if sum([row[i] for row in state]) in cons:
            return int(sum([row[i] for row in state]) / 3)*(1.0+depth)/10

    if state[0][0] + state[1][1] + state[2][2] in cons:
        return int((state[0][0] + state[1][1] + state[2][2]) / 3)*(1.0+depth)/10
    if state[0][2] + state[1][1] + state[2][0] in cons:
        return int((state[0][2] + state[1][1] + state[2][0]) / 3)*(1.0+depth)/10
    elif not is_filled(state):
        return None
    return 0


def max_min(n: Node) -> int:
    n.value = 0
    if len(n.nodes) == 0:
        n.value = cal_val(n.state)
    else:
        if n.p_type == 1:
            n.value = -100
            for child in list(n.nodes.values()):
                max_min(child)
                if child.value > n.value:
                    n.value = child.value
                    n.opt_next = child
        elif n.p_type == -1:
            n.value = 100
            for child in list(n.nodes.values()):
                max_min(child)
                if child.value < n.value:
                    n.value = child.value
                    n.opt_next = child
    return n.value


def play(n:Node):
    while n is not None:
        print(n.state)
        print("value: "+str(n.value))
        print("stage value: "+str(cal_val(n.state)))
        print("cells left:"+str(len(empty(n.state))))
        n = n.opt_next


node: Node = None


def ex():
    try:
        print("Starting Minmax")
        max_min(node)
        play(node)
        print("----------\n")
    except Exception as e:
        traceback.print_exc()
