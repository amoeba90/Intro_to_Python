#!/usr/bin/env python3
#Emma Ryan

#Choose your own adventure
#Dablooooooooooooooons
#version 1.1

import time

def print_with_delay(content): #function so i dont have to write this every time
  for line in content.split('\n'): #splits up the big long strings into each line
    print(line)#prints each line one by one
    time.sleep(0.6) #sets a timer of .5 sec between each print
    #without all the stuff before the timer, the timer barely does anything since my strings are grouped up and stuff.
    #i didnt like it just printing normal either, cause theres some long narration/dialogue portions.

inventory = [0] #setting the inventory, specifically, the number is for the dabloon count (money)
#also i know dabloons are actually spelt doubloons, its for the laughs
def zero(): #i made functions for each separate "page" of the choose your own adventure". So each one is one set of words and one set of Q/A
    inventory.clear() #this is for the reruns
    inventory.append(0)#without these you can exploit the inventory system by getting more and more stuff each additional run.
    print_with_delay('''\nYou are a citizen of the far away nation of Canada. 
You are relaxing inside your humble home in your village, churning butter or something, when you hear a knock on the door.\n
        1. Answer the door
        2. Ignore
        ''') #the canada things a joke btw, and the butter. this is just some royal monarchy kingdom somewhere
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            one() #invoking the next function
            break #no infinite loops here
        elif answer == 2:
            five()
            break
        else:
            print("Not a valid number")

def one():
    print_with_delay('''\nA knight in full armour stands before you holding an official document.
    "Hello peasant, the Princess has been kidnapped by a evil witch."
    "We need your help to stop her plans and rescue our beloved lady." 
    "Will you comply?"\n
        1. Yes, I was made for this.
        2. Nah I'm good, you have fun with that though.
        3. What's in it for me?
        4. ...
        ''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            six()
            break
        elif answer == 2:
            three()
            break
        elif answer == 3:
            two()
            break
        elif answer == 4:
            two()
            break
        else:
            print("Not a valid number")

def two():
    print_with_delay('''\n"Wouldn't the joy from knowing you helped your amazing wonderful lovely beautiful rich royal family be the greatest reward there is?"\n
        1. You're so right, tell me where to start.
        2. No thanks then, I deserve a real reward.
        3. ...
        ''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            six()
            break
        elif answer == 2:
            three()
            break
        elif answer == 3:
            three()
            break
        else:
            print("Not a valid number")

def three():
    print_with_delay('''\n"WAIT!!!”
    "I suppose we could compensate you for your troubles.”
    "If you can rescue the princess safely that is”\n
        1. Bet, point the way.
        2. I think I'd rather stay at home thank you very much.
        3. …
        ''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            six()
            break
        elif answer == 2:
            three()
            break
        elif answer == 3:
            three()
            break
        else:
            print("Not a valid number")
def four():
    print_with_delay('''\n"Fine, if that's how you are, have it your way.”
    "But just know as soon as the princess is saved we are coming back and having a little 'chat'.”
The guard leaves your house and you go back to your daily activities, now slightly more scared than before.
    ''')
    five() #no input on this one, but i wanted to make it separate from the next so i could go the the next on other occasions.

def five():
    print_with_delay('''\n-3 months later-
\nYou hear commotion outside your house and step out to investigate.
All your neighbors are looking at an official document posted on the bulletin board in the square.	.
The princess returned home safely and was able to share a new way of governing to the people.
Her ideas garnered the support of the people so hugely, that there was nothing the current King could do against her.
There will now be an election for the new leader, and anyone is allowed to run.
However, it is expected the Princess will win, as she still has the most supporters, and people like what they are used to.
\nTHE END
        \n1.  RESTART FROM BEGINNING
        2.  QUIT
    ''') #ending one, the good ending imo, lots of paths lead to this ending, though it makes the most sense through just a few paths
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            zero() #replaying from beginning
            break
        elif answer == 2:
            quit() #if you dont wanna play anymore!
        else:
            print("Not a valid number")

def six():
    print_with_delay('''\n"Alright, the Princess's last known location was a pub in this town.”
    "Don't ask why.”
    "But if I were you, I'd start there”
The guard leaves.
You decide to grab your bag before you leave.
What do you pack? (You may only bring one)\n
        1.  Your life's savings (5 gold dabloons)
        2.  Your father's sword (Don't lose it)
        3.  An extra pair of socks (it couldn't hurt)
    ''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            inventory[0] = 5 #changing number to 5, this is dabloon counter basically.
            break
        elif answer == 2:
            inventory.append("sword") #adding sword as new item in list at the end
            break
        elif answer == 3:
            inventory.append("socks") #adding socks as new item in list at the end
            break
        else: print("Not a valid number")
    print_with_delay('''\nWith your bag packed you lock the door and head to the pub.
A couple hours later and you arrived, you can hear laughter and music coming from inside.
You open the front door and glance around.
The Pub's Owner is running the bar and cleaning a glass.
You approach her.
    "Hey there traveler, what can I do you for?”\n
        1.  Do you have any info on the missing princess?
        2.  How much for a glass of your finest mead?''')
    if 'sword' in inventory: #this option will only come up if you chose to bring sword
        print_with_delay("        3.  *point sword* GIVE ME ALL YOUR MONEY RIGHT NOW RAHHHHHHHHH!!!")
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onenine()
            break
        elif answer == 2:
            nine()
            break
        elif answer == 3 and 'sword' in inventory: #both need to be true in order for you to be able to take this path
            seven()
            break
        else:
            print("Not a valid number")


def seven():
    print_with_delay('''\nThe pubowner sees your sword and pulls out a crossbow from under the table
    "You shouldn't have done that friend.”
The arrow flies through the air and pierces your heart.''')
    death(six) #first death path! the six indicates the last choice function to recall to

def death(previous): #the only function with a parameter
    print_with_delay('''\nYOU HAVE DIED
…BUT ITS NOT OVER YET\n
        1.  REPLAY FROM LAST CHECKPOINT 
        2.  RESTART FROM BEGINNING [0]
        3.  QUIT''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            previous()
            break
        elif answer == 2:
            zero()
            break
        elif answer == 3:
            quit()
            break
        else:
            print("Not a valid number")


def nine():
    print_with_delay('''\n"Its one gold dabloon for a glass”
    "Be careful though, that stuff is strong, any more than four and you might not wake up in the morning”
    "So what'll it be?”\n
        1.  Actually, do you have any info on the missing princess?"''')
    while True:
        if inventory[0]==5:
            print_with_delay("        2.  One glass please!(-1 dabloon)")
            break
        else:
            break
    while True:
        if inventory[0]==5:
            print_with_delay("        3.  Pfff, I'm no child, pour me five to the rim!(-5 dabloons)")
            break
        else:
            break
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onenine()
            break
        if answer == 2:
            inventory[0] = 4
            onefour()
            break
        elif answer == 3:
            inventory[0] = 0
            onezero()
            break
        else:
            print("Not a valid number")


def onezero(): #I didn't go with eleven, twelve, etc cause i didnt want to write out the future long ones like twentyseven, although in retrospect, this way didn't really make a difference. Whatever though, its my decision
    print_with_delay('''\n"Don't say I didn't warn you friend, its your funeral.”
The pub owner pours 5 overflowing glasses of mead and pushes them across to you.

You down the first glass with ease and start on the next.
Some people glance over at you and roll their eyes.

The second glass goes down the hatch and you let out a big sigh.

After a brief pause you go back for more, chugging the third glass.
There are more onlookers now, all impressed at your brave feat.

You start on the fourth glass and hear cheers from your audience.
Everyone expects you to stop now, but you still have a fifth glass.

Do you finish what you started?\n
        1.  Mama didn't raise no quitter.
        2.  That's good enough, you someone could use this drink more than you anyways.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            oneone()
            break
        elif answer == 2:
            onetwo()
            onethree()
            break
        else:
            print("Not a valid number")


def oneone():
    print_with_delay('''\nYou pick up the final glass and raise it to the ceiling, giving a hearty yell.
The onlookers' faces change from joy to horror as they watch you swallow every last drop of your drink.
But you feel fine!
Yeah…
You feel okay!
…
It's normal to get tired after drinking so much!
…
You're just gonna take a little nap.
…
The princess can wait one day.
…
This floor looks very comfy.
…
…
…''')
    death(onezero) #another death, with the savepoint being onezero, meaning you could go a different path and not die if you chose a diff option.

def onetwo():
    print_with_delay('''\nYou pass the glass to the thirsty stranger in front of you who accepts it with a smile on his face.
    "Thank you friend! The pub owner wouldn't accept my trade for a drink, so you have it!”
He gives you a crudely drawn map with the words 'shortcut' written on it.
    "You're welcome!”  ''')
    
def onethree():
    print_with_delay('''\nYou're feeling great after your drinks and act of charity,
so you decide to take it easy and dance to the music with all your new friends.

-The Next Morning-
    
You wake up outside the pub by the trash pile.
Oh yeah, you were feeling adventurous last night and tried to steal the bard's guitar.
You're banned from the establishment for a week, so there's no going back there for info now.
You have no leads except for the map you got from the stranger, so you decide to follow it and see where it takes you.''')
    twoseven()
    
def onefour():
    print_with_delay('''\nThe pub owner pours you a single glass and slides it over to you.
As you are about to drink, however, a stranger approaches you.
He looks like he has something to ask you.
    "Hello friend, would you be so kind and let me have that drink of yours? I could really use a drink but I don't have any money."\n
    1.	Too bad pal, this one's mine.
    2.	Uhhh sure I guess?''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onefive()
            break
        elif answer == 2:
            onetwo()
            onesix()
            break
        else:
            print("Not a valid number")

def onefive():
    print_with_delay('''\n"That's okay, I'm used to rejection anyways”
The stranger frowns and turns away.
You can hear him sniffling as he shuffles to the corner of the room and curls into a ball on the floor.
...
I hope you're happy now.
...
Meanie.
...
You enjoy your glass of fine mead, your stomach happy, and your wallet lighter.
You plop the empty glass back on the counter and look at the pub owner again.

    "Something else you needed traveler?”\n
        1.  Yesh,  di uou hace any info on the mosssing priinceas?
        2.  Whst's uour namE?''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onenine()
            break
        elif answer == 2:
            oneseven()
            break
        else:
            print("Not a valid number")

def onesix():
    print_with_delay('''\nYou turn around and see the pub owner smiling at you
    "That was very kind of you to give up your drink, what can I call you, traveler?"\n
        1.  I'm not here to flirt, I need info on the missing princess.
        2.  You can call me whatever you like, what's yours? ''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onenine()
            break
        elif answer == 2:
            twozero()
            break
        else:
            print("Not a valid number")
            
def oneseven():
    print_with_delay('''\n"Um, it's Jinx. Anything else for you traveler?"
        1.  YES, do uou hscr sny info on tthe missing pribcess?
        2.  Tgat's a pretty name, y. iu''re verY prettyy.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onenine()
            break
        elif answer == 2:
            oneeight()
            break
        else:
            print("Not a valid number")
            
def oneeight():
    print_with_delay('''\n"That's very sweet of you to say.”

She smiles
    "I like you.”
    
    "You know, once I close here for the night, would you like to come with me and I can show you something special?\n
        1.  Np, I'm tryimg to find thee missing oroncess, dp you ha. ve an. y info?
        2.  I woukd love yo. ! ''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            onenine()
            break
        elif answer == 2:
            twotwo()
            break
        else:
            print("Not a valid number")
            
def onenine():
    print_with_delay('''\n"Oh… that…”

    "Yeah I have some information for you I guess.”
    "Somebody saw her being led into the dark forest the other day.”
    "But I wouldn't go there if I were you, Its pitch black and covered with monsters.”
    "You'll be lost or dead in an hour.”

You thank her and turn to leave the pub.
    "Good luck I guess...”

Where do you want to go now?\n
        1.  Enter the dark forest ''')
    if "map" in inventory:
        print_with_delay("      2.  See where the shortcut on map leads.")
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threethree()
            break
        elif answer == 2 and "map" in inventory:
            twoseven()
            break
        else:
            print("Not a valid number")
            
def twozero():
    print_with_delay('''\n"Its Jinx!”
    "You know I wouldnt usually do this, but I have a feeling you share my ideals and I wanna show something to you.”
    "I have to close up here first, but once Im done, would you follow me?”\n
        1.  Sounds fun!
        2.  Sounds dangerous… Ill pass.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            twotwo()
            break
        elif answer == 2:
            twoone()
            break
        else:
            print("Not a valid number")
            
def twoone():
    print_with_delay('''\n"Aww thats too bad, well let me know if you change your mind”\n
        1.  Actually… Ill come with you.
        2.  Sorry, but do you have any info on the missing princess?''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            twotwo()
            break
        elif answer == 2:
            onenine()
            break
        else:
            print("Not a valid number")
            
def twotwo():
    print_with_delay('''\n"Really?! Yay!! Feel free to mingle and have fun in the meantime and I'll let you know when I'm ready”
You take a seat by the fireplace and listen to the upbeat music the bard is playing.
People are singing and dancing.
Peoplewatching is pretty fun. 

-Later that evening-

All the customers have left the pub and Jinx is sweeping the floor.
She walks up to you and brushes her hands off her apron.
    "Alright, all done, let's go!”
You leave the pub with her and start walking.
She leads you to the edge of town and to the dark forest.
Its very dark out, and once you're under the tree line, not even the moonlight reaches you.

This seems sketchy.

All of a sudden, you hear a growl from the bushes next to you.
You jump with surprise, but Jinx still looks calm.
    "Don't worry, they won't touch you.”
You are about to say something, but then she looks over at you and smiles, and you feel bad for even considering the worst.

You keep walking further into the forest, further than seems reasonable, further than any normal person would go.
    "We're almost there”

Finally, you walk into a clearing and see a little wooden house with smoke coming out of the chimney.
    "When we walk in, please don't jump to conclusions and hear me out, okay?”
You agree tentatively and she opens the front door.

In front of you, you see the princess, reading a book and snacking on cookies.
What do you do?\n
        1.  Run away to tell someone what you found.
        2.  Attack Jinx.
        3.  Look to Jinx for an explanation.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            twothree()
            break
        elif answer == 2:
            twofour()
            break
        elif answer == 3:
            twofive()
            break
        else:
            print("Not a valid number")
            
def twothree():
    print_with_delay('''\nYou bolt out the house and back into the forest.
    *Sigh* "I was hoping you wouldn't do that.” You hear her mutter in the distance.
Too bad, you're GONE.

She didn't even chase after you.
You're pretty far away from town, but you're running this time, so it shouldn't take long to get back.

Wow its dark.

From the bushes you hear a growl.
Oh no.

Maybe they would forgive you if you turned back around?

Too late.
A flash of teeth and claws lunges at you.
...''')
    death(twotwo)
    
def twofour():
    print_with_delay('''\nYou swing your fist in her direction, but she was expecting this, and she dodges back.
You try to knock her off balance with a kick.

But while you are focused looking at her's legs, the Princess is now focused on you.
The Princess is pointing a crossbow in your direction, and she fires.

Why would she protect her kidnapper?

It doesn't make any sense.
...
It's too late.
...
There's no point in finding reason.
It's over.
...''')
    death(twotwo)
    
def twofive():
    print_with_delay('''\nYou stay silent and look back and forth between her and the Princess.
Is she the witch?

    "I'm not a witch.” She starts, almost like she knew exactly what you were thinking.
    "Well maybe by some standards I am, but not technically.”
    "Its not like I can use magic or anything, I'm just a radical thinker.”
    "I'm not someone the monarchy would want throwing ideas around.”
    
She walks over to the Princess.

    "And technically I did kidnap you, but we're cool now, right?”
    
The Princess looks up and smiles

    "Yep! We're cool.”\n
        1.  So why DID you kidnap her?
        2.  What are these crazy ideas?''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            twosix()
            break
        elif answer == 2:
            twosix()
            break
        else:
            print("Not a valid number")
            
def twosix():
    print_with_delay('''"I believe in a better leadership, one that is decided by the people, for the people.”
    "I want our leader to be someone who actually cares about us, not letting us eat scraps while they sit on their gold thrones.”
    "And in order to make a change, I needed someone with power and influence to hear me.”
    "So, you know, I got my own captive audience.”
    The princess waves
    "Once she was out of her castle and actually able to hear my message, she agreed with me.”
    "I still need to teach her more about leadership and prepare her, but once we're done, she will be a candidate in the upcoming election.”
    "We can do this on our own, but I would love to have your support.”
    "Can I count on you?”
        1.  Yes, just tell me what to do.
        2.  You're crazy, see ya!''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            five()
            break
        elif answer == 2:
            twothree()
            break
        else:
            print("Not a valid number")
            
def twoseven():
    print_with_delay('''The map seems to lead in the direction of the dark forest, but a little different?
    You follow it to what it say is 'entrance'.
    It appears to be a hollow, fallen tree on the edge of the dark forest.
    With no other apparent options, you get down on your hands and knees and crawl inside.
    Once your head is inside, you can see that it actually leads to a tunnel underneath the dirt.
    Its pitch black inside, but its so small that you can't image you would get turned around, so you head inside. 
    You've heard how big the dark forest is, so if this leads somewhere in there, this may take a while.
    -6 hours later-
    You are thirsty, hungry, and exhausted from crawling for so long.
    Finally, you see a light and the end of the tunnel. 
    You make it out and look around.
    You appear to be in a clearing in the middle of the dark forest, and in the middle with you, is a wooden house with smoke coming out of the chimney.
    You've made it this far, and you are in desperate need of some water, so you knock on the door. 
    …
    You hear footsteps.
    …
    Finally someone answers the door.
    It's the missing Princess.
    "Who are you?” She asks.
    You can see she is hiding something behind her.
        1.  What are you doing here? Are you okay? Do you know everyone is looking for you?
        2.  *Grab her arm* I'm taking you back to the castle where you should be.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threezero()
            break
        elif answer == 2:
            twoeight()
            break
        else:
            print("Not a valid number")
            
def twoeight():
    print_with_delay('''You grab her arm and try to lead her out the house but she slips out of your grasp and pulls a crossbow from behind her.
She is pointing it at you.
    "NO!”
    "I'm staying here, I'll ask again, who are you?”
        1.  Okay, calm down, let's try this again. I'm not going to hurt you, I'm here to help you.
        2.  Who I am doesn't matter, I'm just doing my job. Now come with me.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threezero()
            break
        elif answer == 2:
            twonine()
            break
        else:
            print("Not a valid number")
            
def twonine():
    print_with_delay('''You reach to grab the Princess again and she panics.
She shot you.
    …
    …''')
    death(twoeight)
    
def threezero():
    print_with_delay('''\n"I'm fine.”
    "I don't want help.”
    "I'm happy here.”
    "You don't understand.”
    "You're not supposed to be here”
    "She didn't say you were coming”
    "Can you leave, please?”\n
        1.  Okay, I'll leave.
        2.  Wait! I want to understand, can I stick around until 'she' gets here? Maybe we can talk this out.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threeone()
            break
        elif answer == 2:
            threetwo()
            break
        else:
            print("Not a valid number")
            
def threeone():
    print_with_delay('''\nYou turn around and leave the way you came.
You don't understand the full story, but what else could you do?
You go back to your house and lay in bed, pondering all you've been through.''')
    five()
    
def threetwo():
    print_with_delay('''…
    "Okay.”
    
    "She's better at talking than me.”
    
    "But you're waiting outside.”
    "She wouldn't like it if you stayed inside.”
You agree and wait outside the house for 'her' to get home.
Luckily theres a well, so you are able to take a few swigs of water to quench your thirst.
You're nervous.

    -The Sun Sets-
    
You are about to drift off to sleep by the side of the house when you hear footsteps.
You look up to see who it is.

It's the pub owner from earlier.
    "Well isn't this a surprise.”
    
She looks angry.

    "I don't know how you got here, but I'm assuming you already saw who's inside,
    so come inside and let's talk.”
You walk into the house with her and take a seat at the table.\n''')
    twofive()
    
def threethree():
    print_with_delay('''\nYou heard the warnings from the pub owner, but you'll be fine!

The entrance to the dark forest was just a quick walk away.
You look into the dark abyss that is in front of you, brace yourself, and start walking.
There's kind of a path, but its hard to differentiate from the rest of the foliage.
It's more like an animal trail.
But animals have a good sense of direction, so you decide to trust their judgement.

After many hours of wandering, you question if you are making any progress at all.
Everything looks the same, and this trail just keeps going.

It's dark out.

It's getting cold too.

Suddenly, you hear a woman's voice.
    "Hello…?” The voice echoes.
What if it's the princess?
You run towards the source of the voice.
    "Is there someone there?” The voice says again.
You know exactly where it's coming from now.
You get closer and see a cloaked figure.
They see you.
    "Oh thank god someone is here, can you help me?”\n
        1.  Are you the princess by chance?''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threefour()
            break
        else:
            print("Not a valid number")
            
def threefour():
    print_with_delay('''\n"What? No, I'm not a princess.”
    "I need help, I was scavenging looking for food and I got lost.”
    "It's so cold.”\n
        1.  I don't have anything to spare and I'm busy looking for someone, sorry.''')
    if "socks" in inventory:
        print_with_delay("       2.  *give socks* I'm lost too. This is all I have, but you probably need it more than me. At least It'll keep you warm.")
    if inventory[0] == 5 or inventory[0] == 4:
        print_with_delay("       3.  *give all remaining dabloons* I'm lost too. It's not much now, but if you make it out, these should help you eat for a while.")
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threeseven()
            break
        elif answer == 2 and "socks" in inventory:
            threefive()
            break
        elif answer == 3 and (inventory[0] == 5 or inventory[0] == 4):
            threefive()
            break
        else:
            print("Not a valid number")
            
def threefive():
    print_with_delay('''\n"Oh bless you.”
    "Thank you so much.”\n''')
    threesix()
    
def threesix():
    print_with_delay('''\n"You're a very kind soul.”
...
    "You would understand.”
...
She removes her cloak and you get a look at her face.
It's the pub owner.
What is she doing out here?
    "I'm sorry for tricking you but I have to take precautions, I needed to know I can trust you.”
    "You probably have a lot of questions but please, just come with me, everything will make sense after”
As strange as this whole situation is, you feel as if your only choice is to follow her, you feel nowhere close to finding the Princess anyways.
She leads you further through the forest, but she seems to have a purpose, like she knows where she is.
All of a sudden, you hear a growl from the bushes next to you.
You jump with surprise, but she still looks calm.
    "Don't worry, they won't touch you.”
You are about to say something, but then she looks over at you and smiles, and you feel a little reassured.
    "We're almost there.”
Finally, you walk into a clearing and see a little wooden house with smoke coming out of the chimney.
    "When we walk in, please don't jump to conclusions and hear me out, okay?”
You agree tentatively and she opens the front door.
In front of you, you see the princess, reading a book and snacking on cookies.
What do you do?\n
        1.  Run away to tell someone what you found.
        2.  Attack.
        3.  Wait for an explanation.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            twothree2()
            break
        elif answer == 2:
            twofour2()
            break
        elif answer == 3:
            twofive2()
            break
        else:
            print("Not a valid number.")

def threeseven():
    print_with_delay('''\nYou continue on what you presume to be the same path.
All of a sudden, you hear a growl from the bushes next to you.
Out jumps a massive wolf, teeth bared.\n
        1.  Try to defend yourself barehanded.
        2.  Pray it's a good boy.''')
    while True:
        if 'sword' in inventory:
            print_with_delay("        3.  Try to defend yourself with your sword.")
            break
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            threeeight()
            break
        elif answer == 2:
            threenine()
            break
        elif answer == 3 and 'sword' in inventory:
            fourzero()
            break
        else:
            print("Not a valid number.")
    
def threeeight():
    print_with_delay('''\nAs the wolf lunges at you, you attempt to subdue it with a punch to the nose.

You miss.
...''')
    death(threeseven)
    
def threenine():
    print_with_delay('''\nYou could never hurt a dog, even one as scary as this one.
You lean down with the back of your hand pointed at it.
You talk to the wolf in a baby voice, calling it a good boy, saying that you love him.
    
The wolf pauses.
    
Maybe this is actually going to work.
    
Just kidding.
    
The wolf bares its teeth again.
It growls and stalks towards you.
You close your eyes.
...
...
...?
You're still alive.
    
You open your eyes and see the wolf sitting down, tail wagging.
Next to the wolf is the cloaked woman.
    
What is going on?
    
    "I was going to let him eat you, you know.”
    "You turned your back on someone in need.”
    "But everyone deserves a second chance.”
    "After I saw your reaction to the wolf, I could see the goodness in your heart.”''')
    threesix()

def fourzero():
    print_with_delay('''\nYou draw your sword.
The wolf lunges at you.
The tip of your sword goes through the belly of the beast and it falls to the side.
Oh my god.

That was close.

Good thing you brought your sword, right?
Regardless, you must go on.
You continue through the woods, and not far away from your fight, you see a light.

Finally.

You follow the light and break through the woods.
You look around and see you are in a clearing.
In front of you is the source of the light, a wooden house with smoke coming out the chimney.
Someone's inside.
You approach the front door.
Before you can knock, it opens.
Standing there is the cloaked woman.
Her hood is down and you can see her face in the light.
It's the pub owner.
    "You are not welcome here.”
She is holding a crossbow, pointed directly at you.
    "Leave now, or I will shoot, there are no other options.”
Looking past her in the doorway, you see the Princess.

You understand.

The pub owner has been trying to keep you away from here this whole time because she is the witch.

She is the kidnapper.

She is the enemy.

        1.  Kill her.
        2.  Just leave.''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            fourone()
            break
        elif answer == 2:
            five()
            break
        else:
            print("Not a valid number.")
            
def fourone():
    print_with_delay('''\nTypically a crossbow would beat a sword in a battle, but you are right in front of her.
Her weapon's reach means nothing.
She has no time to react as you lean away from the aim of her crossbow and drive your sword into her heart.
Her body falls to the ground, leaving you with a direct path to your goal, the Princess.
The Princess's face is filled with shock and fear looking at what you have done.
You extend your hand expectingly to the Princess.
You see her reach her hand across the kitchen counter.
She's reaching for a knife.
Before you can stop her, she grabs it and plunges it into her belly.
You watch as she falls to the floor.

Why did she do that?
...
What do you do now?
...
...
...
CONGRATULATIONS!!! YOU KILLED EVERYONE!!!
        1.  REPLAY FROM LAST CHECKPOINT
        2.  RESTART FROM BEGINNING
        3.  QUIT''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            fourzero()
            break
        elif answer == 2:
            zero()
            break
        elif answer == 3:
            quit()
        else:
            print("Not a valid number.")

def twothree2():
    print_with_delay('''\nYou bolt out the house and back into the forest.
    *Sigh* "I was hoping you wouldn't do that.” You hear her mutter in the distance.
Too bad, you're GONE.

She didn't even chase after you.
You're pretty far away from town, but you're running this time, so it shouldn't take long to get back.

Wow its dark.

From the bushes you hear a growl.
Oh no.

Maybe they would forgive you if you turned back around?

Too late.
A flash of teeth and claws lunges at you.
...''')
    death(threesix)

def twofour2():
    print_with_delay('''\nYou swing your fist in her direction, but she was expecting this, and she dodges back.
You try to knock her off balance with a kick.

But while you are focused looking at her's legs, the Princess is now focused on you.
The Princess is pointing a crossbow in your direction, and she fires.

Why would she protect her kidnapper?

It doesn't make any sense.
...
It's too late.
...
There's no point in finding reason.
It's over.
...''')
    death(threesix)

def twofive2():
    print_with_delay('''\nYou stay silent and look back and forth between her and the Princess.
Is she the witch?

    "I'm not a witch.” She starts, almost like she knew exactly what you were thinking.
    "Well maybe by some standards I am, but not technically.”
    "Its not like I can use magic or anything, I'm just a radical thinker.”
    "I'm not someone the monarchy would want throwing ideas around.”
    
She walks over to the Princess.

    "And technically I did kidnap you, but we're cool now, right?”
    
The Princess looks up and smiles

    "Yep! We're cool.”\n
        1.  So why DID you kidnap her?
        2.  What are these crazy ideas?''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            twosix2()
            break
        elif answer == 2:
            twosix2()
            break
        else:
            print("Not a valid number")
            
def twosix2():
    print_with_delay('''"I believe in a better leadership, one that is decided by the people, for the people.”
    "I want our leader to be someone who actually cares about us, not letting us eat scraps while they sit on their gold thrones.”
    "And in order to make a change, I needed someone with power and influence to hear me.”
    "So, you know, I got my own captive audience.”
    The princess waves
    "Once she was out of her castle and actually able to hear my message, she agreed with me.”
    "I still need to teach her more about leadership and prepare her, but once we're done, she will be a candidate in the upcoming election.”
    "We can do this on our own, but I would love to have your support.”
    "Can I count on you?”
        1.  Yes, just tell me what to do.
        2.  You're crazy, see ya!''')
    while True:
        answer = int(input("Enter number: "))
        if answer == 1:
            five()
            break
        elif answer == 2:
            twothree2()
            break
        else:
            print("Not a valid number")


print('Welcome to the "Save the Princess" Choose your own Adventure Game!\n') #Welcome Statement
while True:
    start = input('Type "start" to start the game! ') #Start
    start = start.lower()
    if start == "start":
        print("Lets begin!")
        zero() #start running the first function (zero)
        break
    else:
        print('"',start,'" is not a valid command. Please try again.', sep = '')

#This took me about 16 hours, probably too long, but I hope you enjoy it :)
#This was originally written in a word doc for the story, so if I forgot to take out any weird looking quotes, that's why.
#No Ai used, all me (plus occasional help from bf) :3


