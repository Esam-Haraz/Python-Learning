file_name = "data.txt"
try:
    the_file = open(file_name, "r")
    print(the_file.read())
    the_file.close()
except FileNotFoundError:
    print("Warning, Your File Is not Found, Make Sure You Wrote It Name Right!")
finally:
    print("Read Operation Finished")
