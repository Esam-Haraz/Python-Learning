class User:
    users_number = 0
    def __init__(self, user_name):
        self.name = user_name
        User.users_number += 1
    @classmethod
    def get_users_count(cls):
        return f"Your Users Count is {cls.users_number}"

first_user = User("Ahmed")
second_user = User("Esam")
print(User.get_users_count())
