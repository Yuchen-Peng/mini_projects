'''
Random move hanoi tower: at each step one of all valid moves is taken at uniform random; calculate the mean and standard deviation
for the center of mass for all plates after T random move
'''

def validstate(state,N):
# return all valid states given the previous state
    space = list()
    l = len(state)
    for i in range(l):
        if state[i] + 1 < N and (state[i] + 1) not in state[0:i] and state[i] not in state[0:i]:
            new_state = state[:]
            new_state[i] += 1
            if new_state not in space:
                space.append(new_state)
        if state[i] - 1 > -1 and (state[i] - 1) not in state[0:i] and state[i] not in state[0:i]:
            new_state = state[:]
            new_state[i] -= 1
            if new_state not in space:
                space.append(new_state)
    return space

def initial_state_space(M):
    ini_state = []
    for i in range(M):
        ini_state.append(0)
    ini_space = list()
    ini_space.append(ini_state)
    return ini_space

def endstate_space(M,N,T):
    initial_space = initial_state_space(M)
    space_old = initial_space
    for t in range(T):
        space_new = []
        for state in space_old:
            space = validstate(state,N)
            space_new += space
        space_old = space_new
    return space_old

def stats(space):
    center_list = list()
    for item in space:
        sum_m = 0
        sum_p = 0
        for i in range(len(item)):
            sum_m += (i+1)
            sum_p += (i+1)*item[i]
        center = sum_p/sum_m
        center_list.append(center)
    return np.array(center_list).mean(), np.array(center_list).std()

stats(endstate_space(3,3,16))

stats(endstate_space(6,6,256))
