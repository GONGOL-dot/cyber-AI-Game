import random
import time
import os


# ============================================================
# CYBER ESCAPE 2.0
# THE DIGITAL PRISON
# ============================================================


# ============================================================
# BASE FOLDER
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def file_path(filename):
    return os.path.join(BASE_DIR, filename)


# ============================================================
# LOADING
# ============================================================

def loading(text):

    print("\n" + text)

    time.sleep(0.5)

    print(">>>>>")

    time.sleep(0.5)


# ============================================================
# BANNER
# ============================================================

def show_banner():

    print("\n" + "=" * 60)
    print("              CYBER ESCAPE 2.0")
    print("               THE DIGITAL PRISON")
    print("=" * 60)


# ============================================================
# SAVE GAME
# ============================================================

def save_game(player, difficulty, level, lives, score):

    with open(file_path("progress.txt"), "w") as file:

        file.write("PLAYER=" + player + "\n")
        file.write("DIFFICULTY=" + difficulty + "\n")
        file.write("LEVEL=" + str(level) + "\n")
        file.write("LIVES=" + str(lives) + "\n")
        file.write("SCORE=" + str(score) + "\n")

    print("\nGAME PROGRESS SAVED!")


# ============================================================
# LOAD GAME
# ============================================================

def load_game():

    try:

        with open(file_path("progress.txt"), "r") as file:

            data = {}

            for line in file:

                line = line.strip()

                if "=" in line:

                    key, value = line.split("=", 1)

                    data[key] = value

        if "PLAYER" not in data:

            return None

        player = data["PLAYER"]
        difficulty = data["DIFFICULTY"]
        level = int(data["LEVEL"])
        lives = int(data["LIVES"])
        score = int(data["SCORE"])

        return player, difficulty, level, lives, score

    except (FileNotFoundError, ValueError):

        return None


# ============================================================
# CREATE PROFILE
# ============================================================

def create_profile():

    print("\n" + "-" * 60)
    print("                 CREATE PROFILE")
    print("-" * 60)

    player = input("Enter your hacker name: ")

    print("\nChoose difficulty:")

    print("1. EASY   - 5 Lives")
    print("2. MEDIUM - 3 Lives")
    print("3. HARD   - 2 Lives")

    choice = input("\nEnter choice: ")

    if choice == "1":

        difficulty = "EASY"
        lives = 5

    elif choice == "2":

        difficulty = "MEDIUM"
        lives = 3

    elif choice == "3":

        difficulty = "HARD"
        lives = 2

    else:

        print("\nInvalid choice!")
        print("MEDIUM difficulty selected.")

        difficulty = "MEDIUM"
        lives = 3

    # Save player profile

    with open(file_path("players.txt"), "a") as file:

        file.write(
            player
            + " | "
            + difficulty
            + "\n"
        )

    return player, difficulty, lives


# ============================================================
# LEVEL 1
# PASSWORD CRACK
# ============================================================

def level1(player, lives, score):

    print("\n" + "=" * 60)
    print("                 LEVEL 1")
    print("              PASSWORD CRACK")
    print("=" * 60)

    try:

        with open(file_path("levels.txt"), "r") as file:

            lines = file.readlines()

        passwords = []

        for line in lines:

            line = line.strip()

            if line.startswith("PASSWORD="):

                password = line.split("=", 1)[1]

                passwords.append(password)

        if not passwords:

            passwords = [
                "NEXUS",
                "PHANTOM",
                "CYBER"
            ]

    except FileNotFoundError:

        passwords = [
            "NEXUS",
            "PHANTOM",
            "CYBER"
        ]

    password = random.choice(passwords).upper()

    print("\nSYSTEM: PASSWORD PROTECTED")

    print("You have", lives, "lives.")

    print("\nHINT:")
    print("The password is related to the digital world.")

    while lives > 0:

        answer = input("\nEnter password: ")

        if answer.upper() == password:

            print("\nACCESS GRANTED!")

            print("Password cracked successfully!")

            score += 100

            print("Score:", score)

            return True, lives, score

        lives -= 1

        print("\nACCESS DENIED!")

        print("Wrong password.")

        print("Lives remaining:", lives)

    print("\nGAME OVER!")

    return False, lives, score


# ============================================================
# LEVEL 2
# CODE BREAKER
# ============================================================

def level2(player, lives, score):

    print("\n" + "=" * 60)
    print("                 LEVEL 2")
    print("               CODE BREAKER")
    print("=" * 60)

    encrypted = "DBTF"
    decoded = "CASE"

    try:

        with open(file_path("levels.txt"), "r") as file:

            lines = file.readlines()

        for line in lines:

            line = line.strip()

            if line.startswith("ENCRYPTED="):

                encrypted = line.split("=", 1)[1]

            elif line.startswith("DECODED="):

                decoded = line.split("=", 1)[1]

    except FileNotFoundError:

        pass

    print("\nEncrypted message:")

    print(encrypted)

    print("\nHINT:")

    print("Move every letter ONE step backward.")

    while lives > 0:

        answer = input("\nEnter decoded word: ")

        if answer.upper() == decoded.upper():

            print("\nCODE DECRYPTED!")

            print("Security layer bypassed.")

            score += 150

            print("Score:", score)

            return True, lives, score

        lives -= 1

        print("\nDECRYPTION FAILED!")

        print("Lives remaining:", lives)

    print("\nGAME OVER!")

    return False, lives, score


# ============================================================
# LEVEL 3
# DIGITAL VAULT
# ============================================================

def level3(player, lives, score):

    print("\n" + "=" * 60)
    print("                 LEVEL 3")
    print("               DIGITAL VAULT")
    print("=" * 60)

    print("\nScanning system files...")

    files = [
        "system.log",
        "readme.txt",
        "secret.txt",
        "notes.txt"
    ]

    for number, name in enumerate(files, 1):

        print(f"{number}. {name}")

    while lives > 0:

        choice = input("\nSelect suspicious file: ")

        if choice == "3":

            try:

                with open(
                    file_path("secret.txt"),
                    "r"
                ) as file:

                    secret_data = file.read()

                print("\n" + "-" * 50)

                print("        SECRET FILE ACCESSED!")

                print("-" * 50)

                print("\nSecret file contents:")

                print(secret_data)

                score += 200

                print("\nVault access granted!")

                print("Score:", score)

                return True, lives, score

            except FileNotFoundError:

                print("\nERROR!")

                print("secret.txt file not found.")

                return False, lives, score

        else:

            lives -= 1

            print("\nWrong file!")

            print("Security alert triggered!")

            print("Lives remaining:", lives)

    print("\nGAME OVER!")

    return False, lives, score


# ============================================================
# LEVEL 4
# FIREWALL
# ============================================================

def level4(player, lives, score):

    print("\n" + "=" * 60)
    print("                 LEVEL 4")
    print("              FIREWALL LOGIC")
    print("=" * 60)

    question = "5 + 6"
    correct_answer = "55"

    try:

        with open(file_path("levels.txt"), "r") as file:

            lines = file.readlines()

        for line in lines:

            line = line.strip()

            if line.startswith("QUESTION="):

                question = line.split("=", 1)[1]

            elif line.startswith("ANSWER="):

                correct_answer = line.split("=", 1)[1]

    except FileNotFoundError:

        pass

    print("\nFirewall question:")

    print(question, "= ?")

    print("\nHINT:")

    print("Find the hidden mathematical pattern.")

    while lives > 0:

        answer = input("\nEnter answer: ")

        if answer == correct_answer:

            print("\nFIREWALL BYPASSED!")

            print("Security system unlocked.")

            score += 250

            print("Score:", score)

            return True, lives, score

        lives -= 1

        print("\nFIREWALL BLOCKED YOU!")

        print("Lives remaining:", lives)

    print("\nGAME OVER!")

    return False, lives, score


# ============================================================
# FINAL LEVEL
# ============================================================

def final_level(player, lives, score, difficulty):

    print("\n" + "=" * 60)
    print("                 FINAL LEVEL")
    print("              DIGITAL ESCAPE")
    print("=" * 60)

    print("\nAll security layers are unlocked.")

    vault_number = 3
    firewall_code = 55

    final_code = vault_number + firewall_code

    print("\nVault number:", vault_number)

    print("Firewall code:", firewall_code)

    print("\nCalculate:")

    print(
        vault_number,
        "+",
        firewall_code
    )

    answer = input("\nEnter final code: ")

    if answer == str(final_code):

        score += 500

        print("\n" + "=" * 60)

        print("             SYSTEM UNLOCKED")

        print("=" * 60)

        print("\nCONGRATULATIONS!")

        print("YOU ESCAPED THE DIGITAL PRISON!")

        print("\n----------------------------------------")

        print("Hacker:", player)

        print("Difficulty:", difficulty)

        print("Final Score:", score)

        print("Lives Remaining:", lives)

        print("----------------------------------------")

        print("\nMISSION COMPLETE!")

        print("DIGITAL PRISON: ESCAPED")

        # Save final score

        with open(file_path("scores.txt"), "a") as file:

            file.write(
                player
                + " | "
                + difficulty
                + " | Score: "
                + str(score)
                + "\n"
            )

        # Delete completed progress

        try:

            os.remove(file_path("progress.txt"))

        except FileNotFoundError:

            pass

        return True

    else:

        print("\nFINAL SECURITY FAILED!")

        print("Wrong escape code.")

        return False


# ============================================================
# LEADERBOARD
# ============================================================

def show_scores():

    print("\n" + "=" * 60)

    print("                  LEADERBOARD")

    print("=" * 60)

    try:

        with open(file_path("scores.txt"), "r") as file:

            scores = file.readlines()

        if not scores:

            print("\nNo scores available yet.")

            return

        print()

        for number, score in enumerate(scores, 1):

            print(
                str(number)
                + ". "
                + score.strip()
            )

    except FileNotFoundError:

        print("\nNo scores available yet.")


# ============================================================
# START NEW GAME
# ============================================================

def start_game():

    show_banner()

    player, difficulty, lives = create_profile()

    score = 0

    loading("Initializing Cyber System...")

    print("\nPlayer:", player)

    print("Difficulty:", difficulty)

    print("Lives:", lives)

    print("\nStarting game...")

    # -------------------------------
    # LEVEL 1
    # -------------------------------

    success, lives, score = level1(
        player,
        lives,
        score
    )

    if not success:

        save_game(
            player,
            difficulty,
            1,
            lives,
            score
        )

        return

    save_game(
        player,
        difficulty,
        2,
        lives,
        score
    )

    # -------------------------------
    # LEVEL 2
    # -------------------------------

    success, lives, score = level2(
        player,
        lives,
        score
    )

    if not success:

        save_game(
            player,
            difficulty,
            2,
            lives,
            score
        )

        return

    save_game(
        player,
        difficulty,
        3,
        lives,
        score
    )

    # -------------------------------
    # LEVEL 3
    # -------------------------------

    success, lives, score = level3(
        player,
        lives,
        score
    )

    if not success:

        save_game(
            player,
            difficulty,
            3,
            lives,
            score
        )

        return

    save_game(
        player,
        difficulty,
        4,
        lives,
        score
    )

    # -------------------------------
    # LEVEL 4
    # -------------------------------

    success, lives, score = level4(
        player,
        lives,
        score
    )

    if not success:

        save_game(
            player,
            difficulty,
            4,
            lives,
            score
        )

        return

    save_game(
        player,
        difficulty,
        5,
        lives,
        score
    )

    # -------------------------------
    # FINAL LEVEL
    # -------------------------------

    final_level(
        player,
        lives,
        score,
        difficulty
    )


# ============================================================
# RESUME GAME
# ============================================================

def resume_game():

    game = load_game()

    if game is None:

        print("\nNO SAVED GAME FOUND!")

        return

    player, difficulty, level, lives, score = game

    print("\n" + "=" * 60)

    print("             SAVED GAME FOUND")

    print("=" * 60)

    print("\nPlayer:", player)

    print("Difficulty:", difficulty)

    print("Saved Level:", level)

    print("Lives:", lives)

    print("Score:", score)

    print("\nResuming game...")

    # -------------------------------
    # RESUME LEVEL 2
    # -------------------------------

    if level == 2:

        success, lives, score = level2(
            player,
            lives,
            score
        )

        if not success:

            save_game(
                player,
                difficulty,
                2,
                lives,
                score
            )

            return

        save_game(
            player,
            difficulty,
            3,
            lives,
            score
        )

        level = 3

    # -------------------------------
    # RESUME LEVEL 3
    # -------------------------------

    if level == 3:

        success, lives, score = level3(
            player,
            lives,
            score
        )

        if not success:

            save_game(
                player,
                difficulty,
                3,
                lives,
                score
            )

            return

        save_game(
            player,
            difficulty,
            4,
            lives,
            score
        )

        level = 4

    # -------------------------------
    # RESUME LEVEL 4
    # -------------------------------

    if level == 4:

        success, lives, score = level4(
            player,
            lives,
            score
        )

        if not success:

            save_game(
                player,
                difficulty,
                4,
                lives,
                score
            )

            return

        save_game(
            player,
            difficulty,
            5,
            lives,
            score
        )

        level = 5

    # -------------------------------
    # RESUME FINAL
    # -------------------------------

    if level == 5:

        final_level(
            player,
            lives,
            score,
            difficulty
        )


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        print("\n" + "=" * 60)

        print("              CYBER ESCAPE 2.0")

        print("                 MAIN MENU")

        print("=" * 60)

        print("\n1. Start New Game")

        print("2. Resume Game")

        print("3. View Leaderboard")

        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            start_game()

        elif choice == "2":

            resume_game()

        elif choice == "3":

            show_scores()

        elif choice == "4":

            print("\nClosing Cyber System...")

            print(
                "Thank you for playing "
                "CYBER ESCAPE 2.0!"
            )

            break

        else:

            print("\nInvalid choice!")

            print(
                "Please select "
                "1, 2, 3 or 4."
            )


# ============================================================
# PROGRAM START
# ============================================================

main_menu()