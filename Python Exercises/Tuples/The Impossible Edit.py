server_config = ("192.168.1.1", 8080, "admin")
new_port = list(server_config)
new_port[1] = 443
print(tuple(new_port))
print(type((tuple(new_port))))