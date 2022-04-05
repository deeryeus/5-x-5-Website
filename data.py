user1 = {
    "Username": "JohnSmith",
    "Name": "John",
    "Picture": "john.png",
    "Bio": "Looking forward to making new friends!",
    "Zip Code": 12345,
    "Interests": [
        "Football",
        "Hiking",
        "Photography",
        "Video Games",
        "Coding"
    ]
}

user2 = {
    "Username": "JackSparrow",
    "Name": "Jack",
    "Picture": "jack.png",
    "Bio": "Name's Sparrow. Captain Jack Sparrow. I'm looking for a crew to sail the seven seas with and slay krakens.",
    "Zip Code": 12345,
    "Interests": [
        "Coding",
        "Skydiving",
        "Piano",
        "Photography",
        "Hiking"
    ]
}

user3 = {
    "Username": "JaneDoe",
    "Name": "Jane",
    "Picture": "jane.png",
    "Bio": "Hi, I'm Jane. It's nice to meet you!",
    "Zip Code": 12345,
    "Interests": [
        "Hiking",
        "Traveling",
        "Coding",
        "Art",
        "Photography"
    ]
}

user4 = {
    "Username": "JillJohnson",
    "Name": "Jill",
    "Picture": "jill.png",
    "Bio": "Hi, my name is Jill. I love doing physical outdoor activities, spending time with my dogs, and taking photos in the process!",
    "Zip Code": 12345,
    "Interests": [
        "Snowboarding",
        "Hiking",
        "Dogs",
        "Coding",
        "Photography"
    ]
}

user5 = {
    "Username": "KevinWilliams",
    "Name": "Kevin",
    "Picture": "kevin.png",
    "Bio": "Hello, Kevin here. I enjoy a good balance between indoor and outdoor activities. Can't wait to hang out with some new friends!",
    "Zip Code": 12345,
    "Interests": [
        "Gardening",
        "Coding",
        "Chess",
        "Photography",
        "Hiking"
    ]
}

# To store User IDs
users = {
    1: user1,
    2: user2,
    3: user3,
    4: user4,
    5: user5
}

# Return User ID (key) from the 'users' dictionary. Parameter examples include: user1, user2, etc.
def get_user_id(user):
    for key, value in users.items():
         if user == value:
             return key

# To store 5-person lists of connected users within the same area with at least 3 common interests
connection = {
    1: [
        user1,
        user2,
        user3,
        user4,
        user5
    ]
}

# Return a list of 3 common interests that 5 people have in common
def get_same_interests(connection_id):

    common_interests = []

    person1_interests = connection[connection_id][0]["Interests"]
    person2_interests = connection[connection_id][1]["Interests"]
    person3_interests = connection[connection_id][2]["Interests"]
    person4_interests = connection[connection_id][3]["Interests"]
    person5_interests = connection[connection_id][4]["Interests"]

    for interest in person1_interests:
        if interest in person2_interests and \
            interest in person3_interests and \
                interest in person4_interests and \
                    interest in person5_interests:
                    common_interests.append(interest)

    sorted_interests = sorted(common_interests)

    return sorted_interests