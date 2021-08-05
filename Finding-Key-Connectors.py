users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
    ]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# To find all the friendships for one user we will make adjacency list

friendships = {item["id"]: [] for item in users}  # initialize each user friendship list by empty one

for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j


def number_of_friends(user):
    user_id = user["id"]
    friends = friendships[user_id]
    return len(friends)


def total_connections():
    return sum(number_of_friends(user) for user in friendships)


def average_connections():
    return total_connections() / len(users)

# print(number_of_friends(users[3])) --> 3


'''to find the most connected users we need to have a list of the users sorted by number of friends'''


def most_connections():
    users_by_number_of_friends = [(user["id"], number_of_friends(user))for user in users]
    users_by_number_of_friends.sort(key=lambda x: x[1], reverse=True)
    return users_by_number_of_friends


def print_by_number_of_friends():
    curr_list = most_connections()
    print(curr_list)
    
    
print_by_number_of_friends() 

# Output
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

# This result doesn't mean the user with id = "1" is the most centralized user in our network
