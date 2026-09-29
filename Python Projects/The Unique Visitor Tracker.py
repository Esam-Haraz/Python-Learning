gate_a_log = [105, 102, 101, 105, 103]
gate_b_log = [101, 104, 102, 106]
gate_a_log.extend(gate_b_log)
gate_a_log.append(100)
gate_a_log.sort()
Unique_Visitors = set(gate_a_log)
print("Final Log: {}".format(list(Unique_Visitors)))
print("Total Unique Visitors: {}".format(len(Unique_Visitors)))

# AI Suggestion

gate_a_log = [105, 102, 101, 105, 103]
gate_b_log = [101, 104, 102, 106]
unique_set = set(gate_a_log + gate_b_log)
unique_set.add(100)
final_list = list(unique_set)
final_list.sort() 

print("Final Log: {}".format(final_list))
print("Total Unique Visitors: {}".format(len(final_list)))