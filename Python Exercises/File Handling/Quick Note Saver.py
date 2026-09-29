import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Quick Note Saver.txt")
with open(file_path, "w") as f:
    f.write(input("Enter Your Note: ").strip().title())
print("Note Saved!")
