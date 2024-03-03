"""Write a program for a matchstick game being played between the computer and a user.
Your program should ensure that the computer always wins. Rules for the game are as
follows: - There are 21 matchsticks. - The computer asks the player to pick 1, 2, 3, or 4
matchsticks. - After the person picks, the computer does its picking. - Whoever is forced to
pick up the last matchstick loses the game.
"""
total=21
make=16
while total!=1:
    print(f"Remaining Sticks: {total} ")
    ppick=int(input("Choose 1/2/3/4 \n"))
    temp=total-ppick-make
    total-=ppick
    if total>0:
        print(f"Computer picked: {temp}")
        total-=temp
        make-=5
    else:
        print("Player lost.")
        break
    print("Player lost.")