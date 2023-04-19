# This is a text-adventure game where the player goes through a hard quest to get the legendary magic and kill the dragon
import sys
import os
import time
import webbrowser
from emoji import emojize


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


typewriter(
    "Hoi, this is my first game, and there is no save system, and something might be kinda cringy, so yea, enjoy :) \n")

final_choice = input("Do you want to start the game? ")

while True:
    if final_choice.lower().strip() == "yes":
        finall = input("Are you really sure?? ")

        if finall.lower().strip() == "yes":
            typewriter("Well, you got what you asked for....\n ")
            os.system("cls")
            break

        else:
            typewriter("It's a good game, type \"Yes\" \n")

    else:
        typewriter("Okay cool, goodbye")
        exit()

typewriter("As you open your eyes, you see the bright light of the sun shining through the window of your house.... \n")
typewriter("The bright light was enough to wake you up and get you started on your mission you had planned earlier.... \n")
typewriter("You had planned to kill the dragon that ate your family.... \n")
typewriter("And thuss...\n")
typewriter("Now begins your quest to kill the dragon that converted your whole family into a pile of shit.....\n")
typewriter("And now, you have to kill: \"Jeff\", the dragon.\n")

while True:
    choices = input("Do you want to exit the house? ")
    magic_power = 0

    if choices.lower().strip() == "yes":
        typewriter(
            "You: Wait, last night I had soo much booze I forgot what my name is. Can you help me remember my name?\n")
        name = input("What is your name? ")
        typewriter(f"{name}: Oh yeah, I forgot. I'm such a dumbass \n")
        typewriter(
            "You have two roads ahead of you, choose any one: the left or the right? \n")

        choice = input("Which road do you choose? ")

        if choice.lower().strip() == "left":
            typewriter(
                "You just stepped on dog shit, and you say to yourself... \n")
            typewriter(f"{name}: I am such a frickin dumbass.\n")
            typewriter(
                "As you move down the road, you see a royal guard, and you decide to go talk to him. \n")

            typewriter(
                "As you go towards him, you cannot believe your eyes as you see him turn into a ball. \n")
            typewriter(
                "As you approach the ball and touch it, (you're not gay, I believe you) and you get a basic spell.... \n")
            typewriter("You turned gay.")
            typewriter(
                "Just kidding, you have obtained a basic spell of your bloodline.... \n")
            typewriter("And the name of the spell is..... \n")
            typewriter("Jizz burst \n")
            typewriter(emojize(":eyes:"))
            magic_power += 1

            typewriter("Now, you encounter a cow and you decide to kill it. \n")

            kill = input("Are you sure you want to kill the cow? ")

            if kill.lower().strip() == "yes":
                typewriter(
                    "You kill the cow and get steak, but due to the guilt, you jump into the well nearby and kill yourself.")
                typewriter("""
                🅶🅰🅼🅴 🅾🆅🅴🆁        
                """)
                break

            else:
                typewriter(
                    "You kill the cow anyways, and get another SHINY ball from it. \n")
                typewriter(
                    "You have now obtained the legendary power of your bloodline...... \n")
                typewriter("Releasing Rush of Hidden Wolf \n")

                magic_power += 10

                typewriter(
                    "Now you enter the cave of Jeff, the dragon. \n")
                typewriter(
                    "As the long battle drags on, you decide to use your final attack, Releasing Rush of Hidden Wolf. \n")

                killer = input("Are you sure you want to use the power? ")

                if killer.lower().strip() == "yes" & magic_power > 10:
                    typewriter("You have successfully killed the dragon. \n")
                    typewriter(
                        "You are now the strongest magician on the planet with plenty of babes around you. \n")
                    typewriter(
                        "You have won, now get on with your life, and here is your reward. \n")

                elif killer.lower().strip() == "yes" or magic_power <= 10:
                    typewriter(
                        "You are half-dead, waiting for help, as you have killed the dragon. \n")
                    typewriter(
                        "You have won, now get on with your life, and here is your reward. \n")

                else:
                    typewriter("You ded")
                    typewriter("""
                    🅶🅰🅼🅴 🅾🆅🅴🆁        
                    """)
                    break

        elif choice.lower().strip() == "right":
            typewriter(
                "You just stepped on cow shit, and you say to yourself... \n")
            typewriter(f"{name}: I hope it's atleast tasty. \n")
            typewriter(
                "As you move down the road, you see a glowing ball, and you decide to go near it. \n")
            typewriter(
                "You now have obtained the rare magic of your bloodline.... \n")
            typewriter("And the name of the spell is... \n")
            typewriter("Chaos Clap")

            magic_power += 3

            typewriter("Now, you encounter a cow and you decide to kill it. \n")

            kill = input("Are you sure you want to kill the cow? ")

            if kill.lower().strip() == "yes":
                typewriter(
                    "You kill the cow and get steak, but due to the guilt, you jump into the well nearby and kill yourself.")
                typewriter("""
                🅶🅰🅼🅴 🅾🆅🅴🆁        
                """)
                break

            else:
                typewriter(
                    "You kill the cow anyways, and get another SHINY ball from it. \n")
                typewriter(
                    "You have now obtained the legendary power of your bloodline...... \n")
                typewriter("Releasing Rush of Hidden Wolf \n")

                magic_power += 1500

                typewriter(
                    "Now you enter the cave of Jeff, the dragon. \n")
                typewriter(
                    "As the long battle drags on, you decide to use your final attack, Releasing Rush of Hidden Wolf. \n")

                killer = input("Are you sure you want to use the power? ")

                if killer.lower().strip() == "yes" & magic_power > 10:
                    typewriter("You have successfully killed the dragon. \n")
                    typewriter(
                        "You are now the strongest magician on the planet with plenty of babes around you. \n")
                    typewriter(
                        "You have won, now get on with your life, and here is your reward. \n")

                elif killer.lower().strip() == "yes" or magic_power <= 10:
                    typewriter(
                        "You are half-dead, waiting for help, as you have killed the dragon. \n")
                    typewriter(
                        "You have won, now get on with your life, and here is your reward. \n")

                else:
                    typewriter("You ded")
                    typewriter("""
                    🅶🅰🅼🅴 🅾🆅🅴🆁        
                    """)
                    break

        else:
            typewriter(
                "You stay in that same spot for several days until you die of starving, and they construct a statue in honor of your stupidity.")
            typewriter("""
                🅶🅰🅼🅴 🅾🆅🅴🆁        
            """)
            break

    else:
        typewriter("Get out of the house, you weeb. \n")

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
webbrowser.open_new_tab(url=url)

# Shinra tensei
