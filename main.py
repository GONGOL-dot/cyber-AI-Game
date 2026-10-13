
import os
from ai_assistant import ai_cyber_assistant

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def file_path(filename):
    return os.path.join(BASE_DIR, filename)


def show_scores():
    print("\n========== LEADERBOARD ==========")

    try:
        players = []

        with open(file_path("scores.txt"), "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) != 3:
                    continue

                try:
                    name = parts[0].strip()
                    difficulty = parts[1].strip()
                    score = int(parts[2].replace("Score:", "").strip())
                    players.append((name, difficulty, score))
                except ValueError:
                    continue

        if not players:
            print("No scores yet.")
            return

        players.sort(key=lambda player: player[2], reverse=True)

        for rank, (name, difficulty, score) in enumerate(players, 1):
            print(f"{rank}. {name} | {difficulty} | {score} points")

    except FileNotFoundError:
        print("No scores yet.")


def main_menu():
    while True:
        print("\n" + "=" * 55)
        print("             CYBER ESCAPE 2.0")
        print("                MAIN MENU")
        print("=" * 55)

        print("1. Start New Game")
        print("2. Resume Game")
        print("3. View Leaderboard")
        print("4. Offline Cyber Assistant")
        print("5. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            print("\nConnect your existing start_game() function here.")
            print("Keep your existing game-level code in main.py.")

        elif choice == "2":
            print("\nConnect your existing resume_game() function here.")

        elif choice == "3":
            show_scores()

        elif choice == "4":
            ai_cyber_assistant()

        elif choice == "5":
            print("Closing Cyber System...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main_menu()
