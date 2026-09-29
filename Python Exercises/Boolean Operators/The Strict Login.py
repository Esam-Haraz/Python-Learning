db_username = "admin"
db_password = "12345"
input_username = "admin"
input_password = "wrong_pass"
is_authenticated = input_username == db_username and input_password == db_password
print(is_authenticated)