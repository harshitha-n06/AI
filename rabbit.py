from collections import deque

def get_next_states(state):
    states = []
    s = list(state)
    for i in range(len(s)):
        if s[i] == 'E':
            # Move right by 1
            if i + 1 < len(s) and s[i + 1] == '_':
                temp = s.copy()
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
                states.append(''.join(temp))
            # Jump over one rabbit
            if i + 2 < len(s) and s[i + 1] in 'WE' and s[i + 2] == '_':
                temp = s.copy()
                temp[i], temp[i + 2] = temp[i + 2], temp[i]
                states.append(''.join(temp))
        elif s[i] == 'W':
            # Move left by 1
            if i - 1 >= 0 and s[i - 1] == '_':
                temp = s.copy()
                temp[i], temp[i - 1] = temp[i - 1], temp[i]
                states.append(''.join(temp))
            # Jump over one rabbit
            if i - 2 >= 0 and s[i - 1] in 'WE' and s[i - 2] == '_':
                temp = s.copy()
                temp[i], temp[i - 2] = temp[i - 2], temp[i]
                states.append(''.join(temp))
    return states

def bfs(start, goal):
    queue = deque()
    visited = set()
    queue.append((start, [start]))
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for next_state in get_next_states(current):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    return None

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for next_state in get_next_states(current):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))
    return None

# Test
start_state = 'EEE_WWW'
goal_state = 'WWW_EEE'

print("BFS Path:")
print(bfs(start_state, goal_state))

print("\nDFS Path:")
print(dfs(start_state, goal_state))
