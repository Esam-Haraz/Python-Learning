import os
base_path = os.getenv("localappdata")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Vocabulary Builder.txt")

while True:
    print("Welcome To Your Vocabulary Safe")
    print("1. Add a New Word")
    print("2. Start Quiz")
    print("3. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        the_word = input("Enter Your Word: ").strip().lower()
        if the_word.replace(" ", "").isalpha():
            print("Word Added!")
        else:
            print("Only Words Allowed!")
            continue
        word_meaning = input("Enter The Meaning Of The Word: ").strip().lower()
        if word_meaning.replace(" ", "").isalpha():
            print("Meaning Added!")
        else:
            print("Only Words Allowed!")
            continue
        with open(file_path, "a") as f:
            f.write(the_word + ":" + word_meaning + "\n")
    elif user_input == "2":
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = f.readlines()
                if len(lines) == 0:
                    print("Add Words First!")
                else:
                    score = 0
                    for line in lines:
                        parts = line.split(":")
                        word = parts[0].strip()
                        meaning = parts[1].strip()
                        user_answer = input(f"What is The Meaning Of the {word}?").strip().lower()
                        if user_answer == meaning:
                            print("correct!")
                            score += 1
                        else:
                            print(f"Wrong, The Correct Answer is {meaning}")
                    print(f"Your Final Score: {score}/{len(lines)}")
    else:
        break
