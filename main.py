import json


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


def load_data():
    with open('G:\Python\social-network\Shoreline_Challenge\data.json') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    A = 'A'
    B = 'B'
    network = load_data()
    print("Network: ", network)
    if shortest_chain(network, A, B) == -1:
        print("There is no chain between user " + A + " and user " + B + "!")
    else:
        print("Chain length: " + str(shortest_chain(network, A, B)))
