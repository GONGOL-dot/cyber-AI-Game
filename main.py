import os
import random

# ==================================================
# CYBER ESCAPE 2.0 - THE DIGITAL PRISON
# ==================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_FILE = os.path.join(BASE_DIR, "savegame.txt")
SCORES_FILE = os.path.join(BASE_DIR, "scores.txt")
SECRET_FILE = os.path.join(BASE_DIR, "secret.txt")


# ==================================================
# GAME PUZZLES
# ==================================================

PASSWORD_PUZZLES = [
    {
        "password": "CYBER",
        "hint": "A word related to computers and digital security.",
        "points": 100
    },
    {
        "password": "NEXUS",
        "hint": "A connection or central link between things.",
        "points": 100
    },
    {
        "password": "MATRIX",
        "hint": "A simulated digital world.",
        "points": 150
    },
    {
        "password": "PHANTOM",
        "hint": "Something mysterious that appears and disappears.",
        "points": 150
    }
]

CODE_PUZZLES = [
    {
        "code": "DBTF",
        "answer": "CASE",
        "hint": "Move each letter one step backward."
    },
    {
        "code": "DBU",
        "answer": "CAT",
        "hint": "Move each letter one step backward."
    },
    {
        "code": "IPHOF",
        "answer": "HOGNE",
        "hint": "Move each letter one step backward."
    }
]

MATH_PUZZLES = [
    {
        "question": "5 + 6",
        "answer": "55",
        "hint": "Multiply the first number by the sum of both numbers."
    },
    {
        "question": "6 + 7",
        "answer": "78",
        "hint": "Multiply the first number by the sum of both numbers."
    },
    {
        "question": "7 + 8",
        "answer": "105",
        "hint": "Multiply the first number by the sum of both numbers."
    }
]


# ==================================================
# SAVE AND RESUME
# ==================================================

def save_game(player, difficulty, level, lives, score):
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            file.write(
                f"{player}|{difficulty}|{level}|{lives}|{score}"
            )
    except OSError:
        print("Unable to save game.")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = file.read().strip().split("|")

        if len(data) != 5:
            return None

        player = data[0]
        difficulty = data[1]
        level = int(data[2])
        lives = int(data[3])
        score = int(data[4])

        return player, difficulty, level, lives, score

    except (OSError, ValueError):
        return None


# ==================================================
# LEADERBOARD
# ==================================================

def save_score(player, score):
    try:
        with open(SCORES_FILE, "a", encoding="utf-8") as file:
            file.write(f"{player}|{score}\n")
    except OSError:
        print("Unable to save score.")


def show_scores():
    print("\n" + "=" * 50)
    print("                 LEADERBOARD")
    print("=" * 50)

    if not os.path.exists(SCORES_FILE):
        print("No scores available yet.")
        return

    scores = []

    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 2:
                    try:
                        scores.append((parts[0], int(parts[1])))
                    except ValueError:
                        continue
    except OSError:
        print("Unable to read leaderboard.")
        return

    scores.sort(key=lambda item: item[1], reverse=True)

    if not scores:
        print("No scores available yet.")
        return

    for position, (player, score) in enumerate(scores[:10], start=1):
        print(f"{position}. {player} - {score} points")


# ==================================================
# LEVEL 1 - FIND THE PASSWORD
# ==================================================

def level1(player, lives, score):
    print("\n" + "=" * 50)
    print("LEVEL 1 - FIND THE PASSWORD")
    print("=" * 50)

    puzzle = random.choice(PASSWORD_PUZZLES)

    print("Mission: Find the secret password.")
    print("Hint:", puzzle["hint"])

    while lives > 0:
        answer = input("\nEnter password: ").strip().upper()

        if answer == puzzle["password"]:
            print("Correct password! Access granted.")
            score += puzzle["points"]
            print("Points earned:", puzzle["points"])
            return True, lives, score

        lives -= 1
        print("Incorrect password!")
        print("Lives remaining:", lives)

        if lives > 0:
            print("Try again.")

    print("Mission failed! You lost all your lives.")
    return False, lives, score


# ==================================================
# LEVEL 2 - DECODE THE CLUE
# ==================================================

def level2(player, lives, score):
    print("\n" + "=" * 50)
    print("LEVEL 2 - DECODE THE CLUE")
    print("=" * 50)

    puzzle = random.choice(CODE_PUZZLES)

    print("Encrypted code:", puzzle["code"])
    print("Hint:", puzzle["hint"])

    while lives > 0:
        answer = input("\nEnter decoded word: ").strip().upper()

        if answer == puzzle["answer"]:
            print("Code decoded successfully!")
            score += 150
            print("You earned 150 points.")
            return True, lives, score

        lives -= 1
        print("Wrong answer!")
        print("Lives remaining:", lives)

    print("Mission failed!")
    return False, lives, score


# ==================================================
# LEVEL 3 - FIND THE HIDDEN FILE
# ==================================================

def level3(player, lives, score):
    print("\n" + "=" * 50)
    print("LEVEL 3 - FIND THE HIDDEN FILE")
    print("=" * 50)

    if not os.path.exists(SECRET_FILE):
        try:
            with open(SECRET_FILE, "w", encoding="utf-8") as file:
                file.write(
                    "TOP SECRET: The final escape password is CYBER."
                )
        except OSError:
            print("Could not create the secret file.")
            return False, lives, score

    print("Mission: Find the hidden file.")
    print("Hint: The filename starts with 'secret'.")

    while lives > 0:
        answer = input("\nEnter filename: ").strip()

        if answer.lower() == "secret.txt":
            print("Hidden file discovered!")

            try:
                with open(SECRET_FILE, "r", encoding="utf-8") as file:
                    print("\nFile contents:")
                    print(file.read())
            except OSError:
                print("Unable to read the file.")

            score += 200
            print("You earned 200 points.")
            return True, lives, score

        lives -= 1
        print("File not found!")
        print("Lives remaining:", lives)

    print("Mission failed!")
    return False, lives, score


# ==================================================
# LEVEL 4 - SECURITY CHALLENGE
# ==================================================

def level4(player, lives, score):
    print("\n" + "=" * 50)
    print("LEVEL 4 - SECURITY CHALLENGE")
    print("=" * 50)

    puzzle = random.choice(MATH_PUZZLES)

    print("Solve the following challenge:")
    print("Question:", puzzle["question"])
    print("Hint:", puzzle["hint"])

    while lives > 0:
        answer = input("\nEnter answer: ").strip()

        if answer == puzzle["answer"]:
            print("Security challenge passed!")
            score += 250
            print("You earned 250 points.")
            return True, lives, score

        lives -= 1
        print("Incorrect answer!")
        print("Lives remaining:", lives)

    print("Security challenge failed!")
    return False, lives, score


# ==================================================
# FINAL LEVEL - ESCAPE THE DIGITAL PRISON
# ==================================================

def final_level(player, lives, score, difficulty):
    print("\n" + "=" * 50)
    print("FINAL LEVEL - ESCAPE SYSTEM")
    print("=" * 50)

    print("You reached the final security system!")
    print("Enter the final escape password.")
    print("Hint: The answer is related to digital security.")

    while lives > 0:
        answer = input("\nFinal password: ").strip().upper()

        if answer == "CYBER":
            print("\nACCESS GRANTED!")
            print("Congratulations! You escaped the Digital Prison!")

            score += 500
            print("Final score:", score)

            save_score(player, score)

            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)

            print("\nMISSION COMPLETED!")
            return True

        lives -= 1
        print("Wrong password!")
        print("Lives remaining:", lives)

    print("\nGAME OVER!")
    print("You could not escape the Digital Prison.")
    print("Final score:", score)

    save_score(player, score)

    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)

    return False


# ==================================================
# GAME PROGRESSION
# ==================================================

def play_from_level(player, difficulty, level, lives, score):
    levels = {
        1: level1,
        2: level2,
        3: level3,
        4: level4
    }

    while level <= 4:
        save_game(player, difficulty, level, lives, score)

        success, lives, score = levels[level](
            player, lives, score
        )

        if not success:
            print("\nGAME OVER!")
            print("Final score:", score)
            save_score(player, score)

            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)

            return

        level += 1
        save_game(player, difficulty, level, lives, score)

        print("\nCurrent score:", score)
        print("Remaining lives:", lives)

        input("\nPress Enter to continue...")

    final_level(player, lives, score, difficulty)


# ==================================================
# START NEW GAME
# ==================================================

def start_game():
    print("\n" + "=" * 50)
    print("              START NEW GAME")
    print("=" * 50)

    player = input("Enter your player name: ").strip()

    if not player:
        player = "Player"

    print("\nChoose difficulty:")
    print("1. Easy   - 5 lives")
    print("2. Medium - 3 lives")
    print("3. Hard   - 2 lives")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        difficulty = "Easy"
        lives = 5
    elif choice == "2":
        difficulty = "Medium"
        lives = 3
    elif choice == "3":
        difficulty = "Hard"
        lives = 2
    else:
        print("Invalid difficulty. Medium selected.")
        difficulty = "Medium"
        lives = 3

    score = 0

    print(f"\nWelcome, {player}!")
    print("Difficulty:", difficulty)
    print("Lives:", lives)

    play_from_level(player, difficulty, 1, lives, score)


# ==================================================
# RESUME GAME
# ==================================================

def resume_game():
    saved_data = load_game()

    if saved_data is None:
        print("\nNo saved game found!")
        print("Please start a new game first.")
        return

    player, difficulty, level, lives, score = saved_data

    print("\nSaved game found!")
    print("Player:", player)
    print("Difficulty:", difficulty)
    print("Current level:", level)
    print("Lives:", lives)
    print("Score:", score)

    confirm = input("\nResume this game? (yes/no): ").strip().lower()

    if confirm in ("yes", "y"):
        play_from_level(player, difficulty, level, lives, score)
    else:
        print("Resume cancelled.")


# ==================================================
# OFFLINE CYBER ASSISTANT
# ==================================================

def ai_cyber_assistant():
    while True:
        print("\n" + "=" * 50)
        print("            OFFLINE CYBER ASSISTANT")
        print("=" * 50)

        print("1. Password Puzzle Hints")
        print("2. Code Breaking Help")
        print("3. Logical Puzzle Help")
        print("4. Python Help")
        print("5. Cybersecurity Basics")
        print("6. Ask a Question")
        print("7. Back to Main Menu")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            print("\nASSISTANT:")
            print("Read the hint carefully.")
            print("Look for the word's meaning and letter count.")
            print("Example: CYBER relates to computers and security.")

        elif choice == "2":
            print("\nASSISTANT:")
            print("Try shifting every letter backward by one.")
            print("Example: DBU becomes CAT.")
            print("D -> C, B -> A, U -> T.")

        elif choice == "3":
            print("\nASSISTANT:")
            print("Read the entire question before answering.")
            print("Look for number patterns and hidden clues.")
            print("Use the hint to find the correct approach.")

        elif choice == "4":
            print("\nASSISTANT:")
            print("Python is a programming language.")
            print("print() displays output.")
            print("input() accepts user input.")
            print("if/else makes decisions.")
            print("while loops repeat instructions.")

        elif choice == "5":
            print("\nASSISTANT:")
            print("Use strong and unique passwords.")
            print("Never share OTPs or passwords.")
            print("Avoid suspicious links and unknown downloads.")
            print("Enable two-factor authentication when available.")

        elif choice == "6":
            question = input("\nAsk your question: ").strip().lower()

            if any(word in question for word in
                   ["password", "hint", "level 1"]):
                print("Try reading the password clue carefully.")

            elif any(word in question for word in
                     ["decode", "code", "cipher", "level 2"]):
                print("Try shifting each encrypted letter backward by one.")

            elif any(word in question for word in
                     ["file", "secret", "level 3"]):
                print("Look for a file named secret.txt.")

            elif any(word in question for word in
                     ["math", "number", "level 4"]):
                print("Read the mathematical hint and identify the pattern.")

            elif any(word in question for word in
                     ["python", "programming", "code"]):
                print("Python uses variables, conditions, loops and functions.")

            elif any(word in question for word in
                     ["security", "cyber", "hacking"]):
                print("Practice ethical cybersecurity and protect your accounts.")

            else:
                print("I am an offline, rule-based assistant.")
                print("Try asking about passwords, decoding, files,")
                print("math puzzles, Python or cybersecurity.")

        elif choice == "7":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice! Please enter 1-7.")


# ==================================================
# MAIN MENU
# ==================================================

def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("          CYBER ESCAPE 2.0")
        print("          THE DIGITAL PRISON")
        print("=" * 50)

        print("1. Start New Game")
        print("2. Resume Game")
        print("3. View Leaderboard")
        print("4. Offline Cyber Assistant")
        print("5. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            start_game()

        elif choice == "2":
            resume_game()

        elif choice == "3":
            show_scores()

        elif choice == "4":
            ai_cyber_assistant()

        elif choice == "5":
            print("\nClosing Cyber System...")
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice! Please enter 1-5.")


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":
    main_menu()