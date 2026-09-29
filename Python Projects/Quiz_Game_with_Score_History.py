import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "QuizGame")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "QuizGameHistory.txt")

