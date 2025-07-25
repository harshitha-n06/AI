
class Person:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __repr__(self):
        return self.name


class State:
    def __init__(self, left, right, umbrella_side, time_spent, path):
        self.left = left  # List of Person
        self.right = right
        self.umbrella = umbrella_side  # 'left' or 'right'
        self.time_spent = time_spent
        self.path = path  # List of State

    def is_goal(self):
        return len(self.left) == 0 and self.umbrella == 'right' and self.time_spent <= 60

    def __repr__(self):
        return f"Time: {self.time_spent} | Left: {[p.name for p in self.left]} | Right: {[p.name for p in self.right]} | Umbrella: {self.umbrella}"

    def get_successors(self):
        successors = []
        if self.umbrella == 'left':
            # Move two people from left to right
            for i in range(len(self.left)):
                for j in range(i + 1, len(self.left)):
                    p1 = self.left[i]
                    p2 = self.left[j]
                    new_left = [p for p in self.left if p != p1 and p != p2]
                    new_right = self.right + [p1, p2]
                    new_time = self.time_spent + max(p1.time, p2.time)
                    if new_time <= 60:
                        new_path = self.path + [self]
                        successors.append(State(new_left, new_right, 'right', new_time, new_path))
        else:
            # Bring one person back from right to left
            for p in self.right:
                new_left = self.left + [p]
                new_right = [r for r in self.right if r != p]
                new_time = self.time_spent + p.time
                if new_time <= 60:
                    new_path = self.path + [self]
                    successors.append(State(new_left, new_right, 'left', new_time, new_path))
        return successors


from collections import deque

def bfs(initial_state):
    visited = set()
    queue = deque([initial_state])

    while queue:
        current = queue.popleft()

        if current.is_goal():
            return current.path + [current]

        state_key = (
            tuple(sorted(p.name for p in current.left)),
            tuple(sorted(p.name for p in current.right)),
            current.umbrella
        )
        if state_key in visited:
            continue
        visited.add(state_key)

        for next_state in current.get_successors():
            queue.append(next_state)

    return None


def dfs(initial_state):
    visited = set()
    stack = [initial_state]

    while stack:
        current = stack.pop()

        if current.is_goal():
            return current.path + [current]

        state_key = (
            tuple(sorted(p.name for p in current.left)),
            tuple(sorted(p.name for p in current.right)),
            current.umbrella
        )
        if state_key in visited:
            continue
        visited.add(state_key)

        for next_state in current.get_successors():
            stack.append(next_state)

    return None


# Define people
Amogh = Person("Amogh", 5)
Ameya = Person("Ameya", 10)
Grandma = Person("Grandma", 20)
Grandpa = Person("Grandpa", 25)

# Initial state
initial_state = State(left=[Amogh, Ameya, Grandma, Grandpa], right=[], umbrella_side='left', time_spent=0, path=[])

# Run BFS
print("BFS Solution:")
bfs_result = bfs(initial_state)
if bfs_result:
    for step in bfs_result:
        print(step)
    print(f"Total Time: {bfs_result[-1].time_spent} minutes")
else:
    print("No solution found.")

# Run DFS
print("\nDFS Solution:")
dfs_result = dfs(initial_state)
if dfs_result:
    for step in dfs_result:
        print(step)
    print(f"Total Time: {dfs_result[-1].time_spent} minutes")
else:
    print("No solution found.")
