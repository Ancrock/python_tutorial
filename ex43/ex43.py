from random import randint

class Scene(object):
    def __init__(self):
        print "This class is not to be used directly but inherited in other classes"

class Engine(object):
    def __init__(self):
        self.name = "Ngine next"
        
    def play(self, name):
        scene = main_corridor()
        correct_choice = randint(1, 5)
        choice = scene.init_action(name)
        dead = Death()
        if choice == correct_choice:
            print "Saved! Now you take on both the pirates and are able to defeat them. "
        else:
            dead.died(name)
            return -1
        answer = scene.init_puzzle(name)
        if answer == 0:
            print "Congratulations! you move to the next round!! "
        else:
            dead.died(name)
            return -1
        
            
        
class main_corridor(Scene):
    def __init__(self):
        self.name = "Main Corridor"
    
    def init_action(self, name):
        print """Okay %s So you have reached the main corridor. You have to make way to the 
        engine room. There are two pirates in front of you approaching at you with
        their sword. And when you look closely, the other one is slowly taking out his GUN!!!
        What do you do now.
        1: Duck and take cover
        2: Grab the gun
        3: Grab the person with the sword
        4: Take out your sword and kill the person with the gun
        5: Take out your sword and kill the person apporoaching with sword.\n""" %name
        selection = int(raw_input("> "))
        return selection
    
    def init_puzzle(self, Name):
        print """Okay %s You reach the door and you see that there is a door with a mechanism 
        with letters on its gears. There is a phrase written on the door. It goes like this:
        \" This famous pirate looks scruffy
        As he doesnt seem to have shaved
        By not buying razors
        Lots of money he must have saved \n""" %Name
        
        answer = raw_input("> ")
        count = 0
        while (answer != "blackbeard"):
            count += 1
            answer = raw_input("That does not seem to be right. You have used %d chances. You only have 10 in total. Try again : " %count)
            if count >= 10:
                return -1
        return 0
    
class Death(Scene):
    def __init__(self):
        self.death_dialogues = ["You are pathetic. Now you are dead too",
        "My dog would have done better than that. You dead.",
        "Fatality. This is not a child's play kid.",
        "You are dead. You are not worthy for fighting pirates yet.",
        "Here is a lolipop kid:  0-- . Now get put of here. you are dead.",
        "I thought you are better than this. Obvoiusly I was wrong.",
        "Go home crying to you mama.. You are dead"]
    
    def died(self, name):
        num = randint(0,6)
        print "Hmmm...This does not look good for you %s \n" %name
        print self.death_dialogues[num]

class Player(object):
    def __init__(self, name):
        self.name = name
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age


print """_____________HUNT FOR THE GOLDEN ARCH___________

Welcome to the hunt player !! To start the game, enter your name and age and we will start on an epic journey to 
win the treasure back and destroy the pirates ship along the way!! """

#player_name = raw_input("\n Name > ")
#player_age = int(raw_input("\n Age > ")) 
player_name = "Amit"
player_age = 25
player_one = Player(player_name)
player_one.set_age(player_age)
game_engine = Engine()
game_engine.play(player_one.name)

