import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Login Logger.txt")
with open(file_path, "a") as f:
    user_name = input("Enter Your UserName: ").strip()
    f.write(user_name + "\n")
print(f"User {user_name} Added To Log.")
