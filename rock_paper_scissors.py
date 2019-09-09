#lets play rock,paper,scissors coded by RifatRobin
import random
print("    Rock_paper_scissors coded by RifatRobin     ")

print(" _______________________________________________")
print("<___________________Lets play___________________>")
player1=["rock","paper","scissors","rock","paper","scissors","scissors","rock","paper","scissors","rock","paper","scissors"]
player2=["rock","paper","scissors","rock","paper","scissors","scissors","rock","paper","scissors","rock","paper","scissors"]
print("")
while(True):

    ch=input("to play please press 'P' and any key to exit :")
    print("\n")
    if ch=='p' or ch=='P':
        a=random.choice(player1)
        b=random.choice(player2)
        print("player1: <"+a+">      vs      player2: <"+b+">")
        print("")
        if a=="rock" and b=="scissors":
            print("               Winner:   player1")
            print("")
        elif b=="rock" and a=="scissors":
            print("               Winner:   player2")
            print("")

        elif b=="scissors" and a=="scissors":
            print("               Winner:   <draw>")
            print("")
        elif b=="rock" and a=="rock":
            print("               Winner:   <draw>")
            print("")
        elif b=="paper" and a=="paper":
            print("               Winner:   <draw>")
            print("")

        elif a=="paper" and b=="scissors":
            print("               Winner:   player2")
            print("")
        elif b=="paper" and a=="scissors":
            print("               Winner:   player1")
            print("")

        elif a=="rock" and b=="paper":
            print("               Winner:   player2")
            print("")
        elif a=="paper" and b=="rock":
            print("               Winner:   player1")
            print("")
    else:
        break
        print("")
