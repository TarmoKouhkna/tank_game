def initial_user_input():
    options = ["1","2","3"]
    while True:
        user_input = input("Choose your action form below: \n"
                           "1: Play the Game \n"
                           "2: See Results \n"
                           "3: Exit the game")
        if user_input in options:
            return user_input
        print(f"Please pick one of the options {options}")


def tm_input():
    options = ["w","s","a","d","t"]
    while True:
        user_input = input("Chose where the tank will go: \n"
                           "w: Up \n"
                           "s: Down \n"
                           "a: Left \n"
                           "d: Right \n"
                           "t: Shoot!")
        if user_input.lower() in options:
            return user_input.lower()
        print(f"Please pick one of the options {options}")
