server_ip = "192.168.1.1"
server_port = 8080
server_config = (server_ip, server_port)
admins = ["Osama", "Ahmed", "Sayed"]
admins.append("Mahmoud")
full_access = (server_config, admins)
print("Full Access Data: ", full_access)
print("Total Elements: ", len(full_access))
new_server_config = list(server_config)
new_server_config[1] = 433
print(tuple(new_server_config))