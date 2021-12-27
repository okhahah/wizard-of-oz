import time

#figuring out how user might respond
answer_A = ["a", "A"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#grabing objects
sword = 0
flower = 0

requird = ("\nuse only A, B, C\n")

#the story is broken into sections, starting with intro
def intro():
    print ("After a night out with friends, you awaken the \nnext morning in a thick, dank forest. Head spinning and \nfighting the urge to vomit, you stand and marvel at your new,  unfamiliar    setting. The peace quickly fades when you hear a grotesque sound    emitting behind you. A slobbering orc is \n running towards you. You    will:")
    time.sleep(2)
    print("A. Grab a nearby rock and throw it at the orc\nB. Lie down and wait to br mauled\nC. Run")
    choice = input(">>>")  #here's ur first choice
    if choice in answer_A:
      option_rock()
    elif choice in answer_B:
      print("\nwelp that was quick.\n\nyou died!")
    elif choice in answer_c:
      option_run()
    else:
      print(required)
      intro()

def option_rock():
    print("\nThe orc is stunned, but regains control. He begins \nrunning towards you again. Will you:")
    time.sleep(2)
    print("A. run\nB. Throw another rock\nC. run towards nearby cave")
    choice = input(">>>")
    if choice in answer_A:
     option_run()
    elif choice in answer_B:
     print ("\nYou decided to throw another rock, as if the first \nrock thrown did much damage. The rock flew well over the \norcs head. You missed. \n\nYou died!")
    elif choice in answer_C:
     option_cave()
    else:
     print (required)
     option_rock()

def option_cave():
    print("\nYou were hesitant, since the cave was dark and \nominous. Before you fully enter, you notice a shiny sword on \nthe ground. Do you pick up a sword. Y/N?")
    choice = input(">>>")
    if choice in yes:
     sword = 1 #adds a sword
    else:
     sword = 0
     print ("\nwhat do you do next?")
     time.sleep(1)
     print (" A. Hide in silence\nB. Fight\nC. Run")
    choice = input(">>>")
    if choice in answer_A:
     print("\nReally? You're going to hide in the dark? I think \norcs can see very well in the dark, right? Not sure, but \nI'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
     if sword > 0:
      print ("\nYou laid in wait. The shimmering sword attracted \nthe orc, which thought you were no match. As he walked \ncloser and closer, your heart beat rapidly. As the orc \n    reached out to grab the sword, you pierced the blade into \n  its chest. \n\nYou survived!")
     else:
      print ("\nYou should have picked up that sword. You're defenseless. \n\nYou died!")
    elif choice in answer_C:
     print ("As the orc enters the dark cave, you sliently \nsneak out. You're several feet away, but the orc turns\naround and sees you running.")
     option_run()
    else:
     print (required)
     option_cave()

def option_run():
    print ("\nWhile frantically running, you notice a rusted \nsword lying in the mud. You quickly reach down and grab it, \nbut miss. You try to calm your heavy breathing as you hide \n  behind a delapitated building, waiting for the orc to come \ncharging around the corner. You notice a purple flower \n  near your foot. Do you pick it up? Y/N")
    choice = input(">>>")
    if choice in yes:
        flower = 1
    else:
       flower = 0
    print ("You hear its heavy footsteps and ready yourself for \nthe impending orc.")
    time.sleep(1)
    if flower > 0:
        print ("\nYou quickly hold out the purple flower, somehow \nhoping it will stop the orc. It does! The orc was looking \nfor love. \n\n\nThis got weird, but you survived!")
    else:
        print ("\nMaybe you should have picked up the flower. \n\n\nYou died!")

intro()            
                  
                 
                    
            
