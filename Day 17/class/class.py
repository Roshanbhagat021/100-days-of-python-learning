class User:
    def __init__(self,id , username):
        self.id = id
        self.username = username
        self.followers = 0
        self.followings =0


    def follow(self, user):
        user.followers += 1
        self.followings += 1



acc_1 = User(1, "Roshan")

acc_2 = User(2, "Raj")
acc_1.follow(acc_2)

print(acc_1.followers)
print(acc_1.followings)
print(acc_2.followers)
print(acc_2.followings)