log_entry = "2024-01-25|Osama_Elzero|Login_Attempt|0.45"
log_list = list(log_entry.split("|"))
print("Date: {}".format(log_list[0]))
print("User: {}".format(log_list[1].replace("_", " ")))
print("Action: {}".format(log_list[2]))
print("Time Taken: {}".format(log_list[3]))
print("Expected Time for 1000 Requests: {}".format(float(log_list[3]) * 1000))
