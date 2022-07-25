import getpass
def drawbase():
    '''Draws the empty gallows for hangman'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(3):
        gallowsstring+="     |     |\n"
    for i in range(6):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return
def draw1():
    '''draws the head/ first mistake'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(2):
        gallowsstring+="     |     |\n"
    gallowsstring+="     |     O\n" #head
    for i in range(6):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return

def draw2():
    '''draws the body/ second mistake'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(2):
        gallowsstring+="     |     |\n"
    gallowsstring+="     |     O\n" #head
    gallowsstring+="     |     |\n" #body
    for i in range(5):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return

def draw3():
    '''draws the right arm/ third mistake'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(2):
        gallowsstring+="     |     |\n"
    gallowsstring+="     |     O\n" #head
    gallowsstring+="     |     |/\n" #body and arm
    for i in range(5):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return

def draw4():
    '''draws the left arm/ fourth mistake'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(2):
        gallowsstring+="     |     |\n"
    gallowsstring+="     |     O\n" #head
    gallowsstring+="     |    \|/\n" #body and arm
    for i in range(5):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return

def draw5():
    '''draws the right leg/ fifth mistake'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(2):
        gallowsstring+="     |     |\n"
    gallowsstring+="     |     O\n" #head
    gallowsstring+="     |    \|/\n" #body and arm
    gallowsstring+="     |      \\\n"
    for i in range(4):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return

def draw6():
    '''draws the left leg/ sixth mistake'''
    gallowsstring=""
    for i in range(6):
        gallowsstring+=" "
    for i in range(5):
        gallowsstring+="_"
    gallowsstring+="\n"
    for i in range(2):
        gallowsstring+="     |     |\n"
    gallowsstring+="     |     O\n" #head
    gallowsstring+="     |    \|/\n" #body and arm
    gallowsstring+="     |    / \\"
    gallowsstring+='\n'
    for i in range(4):
        gallowsstring+= "     |\n"
    for i in range(10):
        gallowsstring+= "_"
    print(gallowsstring)
    return 

def main():
    displaystring1=""
    displaystring2=""
    alreadyplayed=""

    print("Welcome to this game of Hangman! You can make up to 6 mistakes before the game is over")
    word= getpass.getpass(prompt = "Please enter a word for your partner to guess, you won't be able to see what you are typing.")
    savedword=word
    for i in range(len(word)):
        displaystring1+= "- "
        displaystring2+="  "
    drawbase()
    print (displaystring1)
    mistakecounter=0


    while True:
        global guess
        repeat=False
        while repeat == False:
            print()
            guess=input("Please enter the letter you would like to guess: ")
            if guess in alreadyplayed:
                print("letter already played")
                repeat=False
            else:
                repeat=True
        alreadyplayed+= guess
        

        counter=0
        savedindex=0
        if guess not in word:
            mistakecounter+=1
            if mistakecounter ==1:
                print("Oops! First mistake")
                draw1()
                print(displaystring2)
                print (displaystring1)
            elif mistakecounter ==2:
                draw2()
                print("Darn, thats two")
                print(displaystring2)
                print (displaystring1)
            elif mistakecounter ==3:
                print("Three already???? Ouch")
                draw3()
                print(displaystring2)
                print (displaystring1)
            elif mistakecounter == 4:
                print("FOUR?!?! There's a monster at the end of this game you know...")
                draw4()
                print(displaystring2)
                print (displaystring1)
            elif mistakecounter ==5:
                print("Dayummmmm, try checkers next time")
                draw5()
                print(displaystring2)
                print (displaystring1)
            elif mistakecounter >=6:
                draw6()
                print(displaystring2)
                print (displaystring1)
                print("You lost! That's embarassing :(  The word was", savedword)
                return
        else:
            for letter in word:
                if letter == guess:
                    counter+=1
                    index=word.index(guess)
                    word=word[:index]+" "+ word[index +1:]
                    firsthalf=displaystring2[:index*2]
                    secondhalf=displaystring2[index*2:]

                    
                    displaystring2=firsthalf + guess + secondhalf[1:]
                    savedindex=index
                    teststring=displaystring2
                    teststring = teststring.replace(" ", "")
                    if teststring == savedword:
                        print(displaystring2)
                        print(displaystring1)
                        print("you have won the game! The word was", savedword, ", and you only missed", mistakecounter, "guesses")
                        return
                        
            print(displaystring2)
            print(displaystring1)





main()
