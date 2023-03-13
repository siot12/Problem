def shortest_chain(network, A, B):
    queue = [(A, 0)]
    visited_friends = {A}
    while queue:
        current_node, current_distance = queue.pop()
        if current_node == B:
            return current_distance

        for friend in network[current_node]:
            if friend not in visited_friends:
                visited_friends.add(friend)
                queue.append((friend, current_distance + 1))
    return -1


if __name__ == '__main__':
    network = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}
    A = 'C'
    B = 'D'
    print(shortest_chain(network, A, B))
