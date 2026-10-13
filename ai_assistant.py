
# CYBER ESCAPE 2.0 - OFFLINE CYBER ASSISTANT
# No OpenAI API, no API key, no credits required.

def ai_cyber_assistant():

    print("\n" + "=" * 55)
    print("           OFFLINE CYBER ASSISTANT")
    print("=" * 55)

    while True:
        print("\n1. Password Puzzle Hints")
        print("2. Code Breaking Help")
        print("3. Logical Puzzle Help")
        print("4. Python Help")
        print("5. Cybersecurity Basics")
        print("6. Ask a Question")
        print("7. Back to Main Menu")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            print("\nPASSWORD PUZZLE TIPS")
            print("- Read every clue carefully.")
            print("- Check the number of letters.")
            print("- Look at the first and last letters.")
            print("- Think of words matching all clues.")

        elif choice == "2":
            print("\nCODE BREAKING HELP")
            print("- Compare encrypted and decoded letters.")
            print("- Check whether letters shift forward or backward.")
            print("- Example: DBU becomes CAT.")
            print("- Each letter moves one step backward.")

        elif choice == "3":
            print("\nLOGIC PUZZLE HELP")
            print("- Identify a pattern in the examples.")
            print("- Write down each calculation.")
            print("- Test your rule using another example.")

        elif choice == "4":
            print("\nPYTHON HELP")
            print("- Variables store values.")
            print("- Conditions make decisions.")
            print("- Loops repeat instructions.")
            print("- Functions organise reusable code.")
            print("- File handling reads and writes files.")

        elif choice == "5":
            print("\nCYBERSECURITY BASICS")
            print("- Use strong, unique passwords.")
            print("- Never share API keys or passwords.")
            print("- Only test systems you are authorised to use.")
            print("- Keep software updated.")

        elif choice == "6":
            question = input("\nAsk your question: ").strip().lower()

            if not question:
                print("Please enter a question.")
                continue

            if any(word in question for word in
                   ["password", "hint", "clue", "guess"]):
                print("Check the word meaning, letter count,")
                print("first letter and last letter.")

            elif any(word in question for word in
                     ["decrypt", "decode", "encrypted", "code"]):
                print("Compare each encrypted letter with its")
                print("decoded letter to discover the shift.")

            elif any(word in question for word in
                     ["python", "function", "loop", "variable"]):
                print("Break the problem into small steps.")
                print("Test each step and check the output.")

            elif any(word in question for word in
                     ["file", "read", "write", "save"]):
                print("Use open() to access files.")
                print("Use read() to read and write() to save data.")

            elif any(word in question for word in
                     ["cyber", "security", "hacker"]):
                print("Learn about password safety, encryption,")
                print("authorisation and secure file handling.")

            else:
                print("No matching offline rule found.")
                print("Try asking about Python, passwords,")
                print("code breaking, files or cybersecurity.")

        elif choice == "7":
            print("\nReturning to Cyber Escape...")
            break

        else:
            print("Invalid choice. Select 1 to 7.")


if __name__ == "__main__":
    ai_cyber_assistant()
