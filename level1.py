def level1(player, lives, score):

    print("\n" + "=" * 60)
    print("                 LEVEL 1")
    print("              PASSWORD CRACK")
    print("=" * 60)

    password_list = ["NEXUS", "PHANTOM", "CYBER"]
    password = random.choice(password_list)

    print("\nSYSTEM: PASSWORD PROTECTED")
    print("You have", lives, "lives.")

    print("\nHINT 1:")
    print("The password is related to the digital world.")

    print("\nHINT 2:")
    print("It contains 5 or 6 letters.")

    while lives > 0:

        answer = input("\nEnter password: ")

        if answer.upper() == password:

            print("\n" + "=" * 45)
            print("          ACCESS GRANTED!")
            print("=" * 45)

            print("Password cracked successfully!")
            print("Password:", password)

            score += 100

            print("Score:", score)

            return True, lives, score

        else:

            lives -= 1

            print("\n❌ ACCESS DENIED!")
            print("Wrong password.")
            print("Lives remaining:", lives)

            if lives > 0:

                if password == "NEXUS":
                    print("\n🔎 EXTRA HINT:")
                    print("It starts with the letter N.")

                elif password == "PHANTOM":
                    print("\n🔎 EXTRA HINT:")
                    print("It starts with the letter P.")

                elif password == "CYBER":
                    print("\n🔎 EXTRA HINT:")
                    print("It starts with the letter C.")

    print("\n" + "=" * 45)
    print("             GAME OVER 💀")
    print("=" * 45)

    return False, lives, score