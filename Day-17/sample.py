class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 2
        self.folling = 0
        print("New User is created!!!")
        
    def follow(self, user):
        user.followers += 1
        self.folling += 1

user1 = User(1, "Maharshi")
user2 = User(2, "Leader")

user1.follow(user2)
print(user1.followers)
print(user1.folling)

print(user2.followers)
print(user2.folling)