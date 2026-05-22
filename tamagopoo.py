import time
<<<<<<< HEAD
class animations:
    @staticmethod
    def comiendo_frame1():
        print("""
      .-----------------. 
     /   🍖 COMIENDO 🍖 \\ 
    /  _________________  \\ 
   |  |                 |  |
   |  |     _ _   _ _   |  |
   |  |    ( o ) ( o )  |  |
   |  |     \_______/   |  |
   |  |     / 🍖 🍖 \   |  |
   |  |    (  munch  )  |  |
   |  |     \_______/   |  |
   |  |     ||     ||   |  |
   |  |_________________|  |
   |                       |
   |      (O)   (O)   (O)  |
    \\_____________________/
        """)
    @staticmethod
    def eating():
        # alias for comiendo_frame1 to match calls in main loop
        animations.comiendo_frame1()
    @staticmethod
    def sleeping():
        print("""
        ╔═════════════════════════╗
        ║   😴 sleeping... 😴    ║
        ╠═════════════════════════╣
        ║                         ║
        ║      _ _   _ _         ║
        ║     ( - ) ( - )        ║
        ║      \_____/           ║
        ║     / Z Z Z \          ║
        ║    (   zzz   )         ║
        ║     \_______/          ║
        ║     ||     ||          ║
        ║                         ║
        ╚═════════════════════════╝
        """)
    @staticmethod
    def playing():
        print("""
        ╔═════════════════════════╗
        ║   🎉 playing... 🎉      ║
        ╠═════════════════════════╣
        ║                         ║
        ║      _ _   _ _         ║
        ║     ( ^ ) ( ^ )        ║
        ║      \_____/           ║
        ║     / 🎾 🎾 \          ║
        ║    (   fun   )         ║
        ║     \_______/          ║
        ║     ||     ||          ║
        ║                         ║
        ╚═════════════════════════╝
        """)
    @staticmethod
    def dead():
        print("""
        ╔═════════════════════════╗
        ║   💀 RIP... 💀         ║
        ╠═════════════════════════╣
        ║                         ║
        ║      _ _   _ _         ║
        ║     ( x ) ( x )        ║
        ║      \_____/           ║
        ║     /  R.I.P  \         ║
        ║    (  your pet )       ║
        ║     \_______/          ║
        ║     ||     ||          ║
        ║                         ║
        ╚═════════════════════════╝
        """)
=======
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
class Tamagot:
    def __init__(self, name):
        self.name = name
        self.isfull = 6
        self.happines = 7
        self.energy = 6
        self.isalive = True
        self.isoverfull = 4
<<<<<<< HEAD
        self.money = 0
    def petdraw(self):
=======
    def petdraw(self):        
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
        print("      .-----------------. ")
        print("     /       TAMAGOTCHI  \\ ")
        print("    /  _________________  \\ ")
        print("   |  |                 |  |")
        print("   |  |     _ _   _ _   |  |")
        print("   |  |    ( @ ) ( @ )  |  |")
        print("   |  |     \_______/   |  |")
        print("   |  |     / o   o \   |  |")
        print("   |  |    (    v    )  |  |")
        print("   |  |     \_______/   |  |")
        print("   |  |     ||     ||   |  |")
        print("   |  |_________________|  |")
        print("   |                       |")
        print("   |      (O)   (O)   (O)  |")
<<<<<<< HEAD
        print("    \\_____________________/")
=======
        print("    \_____________________/")
        self.sleep(1)
        print("     .-----------------. ")
        print("     /     TAMAGOTCHI  \\ ")
        print("    /_________________  \\ ")
        print("   |  |               |  |")
        print("   |  |   _ _   _ _   |  |")
        print("   |  |  ( @ ) ( @ )  |  |")
        print("   |  |   \_______/   |  |")
        print("   |  |   / o   o \   |  |")
        print("   |  |  (    v    )  |  |")
        print("   |  |   \_______/   |  |")
        print("   |  |   ||     ||   |  |")
        print("   |  |_______________|  |")
        print("   |                       |")
        print("  |      (O)   (O)   (O)  |")
        print("   \_____________________/")
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
    def feed(self):
        if self.isfull < 10:
            self.isfull += 2
            self.energy -= 1
            print(f"{self.name} is being fed. Fullness: {self.isfull}")
<<<<<<< HEAD
=======
            time.sleep(2)
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
        else:
            self.energy -= 1
            self.isfull= 10
            print(f"{self.name} is already full, pay attetntion to your pet if the you feed the pet him too much he could be died")
            self.isoverfull -= 1
<<<<<<< HEAD
=======
            time.sleep(2)
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
    def  sleep(self):
        if self.energy < 10:
            self.energy += 2
            self.happines -= 1
            self.isfull -= 1
            print(f"{self.name} is sleeping haha.  Energy: {self.energy}")
<<<<<<< HEAD
            
=======
            time.sleep(2)
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
        else:
            self.isfull -= 1
            self.energy = 10
            print(f"{self.name} is already fully rested, pay attetntion to your pet if the you let the pet sleep too much, it will be overfull and died")
            self.isoverfull -= 1
<<<<<<< HEAD
            
=======
            time.sleep(2)
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
    def play(self):
        if self.happines < 10:
            self.happines += 2
            self.energy -= 1
            self.isfull -= 1
            print(f"{self.name} is playing hes doing too well. Happines: {self.happines}")
<<<<<<< HEAD
            
=======
            time.sleep(2)
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
        else:
            self.energy -= 1
            self.happines = 10
            print(f"{self.name} is already happy, pay attetntion to your pet he could be overexcited and coulbe be died")
            self.isoverfull -= 1
            time.sleep(2)
<<<<<<< HEAD
    def check_alive(self):
=======
    def isalive(self):
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
        if self.isoverfull <= 0:
            self.isalive = False
            print(f"{self.name} has died due to overfeeding, over sleeping or over playing. Please take care of your pet.")
        elif self.isfull <= 0:
            self.isalive = False
            print(f"{self.name} has died due to starvation. Please feed your pet.")
        elif self.energy <= 0:
            self.isalive = False
            print(f"{self.name} has died due to exhaustion. Please let your pet sleep.")
        elif self.happines <= 0:
            self.isalive = False
            print(f"{self.name} has died due to sadness. Please play with your pet.")
<<<<<<< HEAD
    def work(self):
        self.money += 2
        print("the tamagotchi is working in the call center...")
        time.sleep(3)
        print("tu mascota" + self.name + "has earned 2 coins! total money: is" + str(self.money))

=======
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
print("Welcome to the Tamagotchi created by me xd!")
print("You can feed, sleep, or play with your pet to keep it happy and healthy.")
print("how do you want to name your beauty pet?")
name = input("Enter your pet's name: ")
mypet = Tamagot(name)
while mypet.isalive:
<<<<<<< HEAD
    print("the stats of " + mypet.name + " are:")
    print ("the happines of " + mypet.name + " is: " + str(mypet.happines))
    print ("the energy of " + mypet.name + " is: " + str(mypet.energy))
    print ("the fullness of " + mypet.name + " is: " + str(mypet.isfull))
=======
    print("the estats of " + mypet.name + "are:")
    print ("the happines of " + mypet.name + "is : " + str(mypet.happines))
    print ("the energy of " + mypet.name + "is : " + str(mypet.energy))
    print ("the fullness of " + mypet.name + "is :" + str(mypet.isfull))
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
    mypet.petdraw()
    print ("what do you want to do with " + mypet.name + "?")
    print("1. Feed , 2. Sleep, 3. Play, 4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        mypet.feed()
<<<<<<< HEAD
        animations.eating()
        mypet.check_alive()
        time.sleep(2)
    elif choice == "2":
        mypet.sleep()
        animations.sleeping()
        mypet.check_alive()
        time.sleep(2)
    elif choice == "3":
        mypet.play()
        animations.playing()
        mypet.check_alive()
        time.sleep(2)
    elif choice == "4":
        print("Goodbye! Thanks for playing my game")
=======
    elif choice == "2":
        mypet.sleep()
    elif choice == "3":
        mypet.play()
    elif choice == "4":
        print("Goodbye!, thanks for play my game")
>>>>>>> ec0de506fdad8e9f0bfc00f2e1d0175d65c95b19
        break
    else:
        print("Invalid choice. Please try again.")