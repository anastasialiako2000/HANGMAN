import random
print("H A N G M A N\n")
won = 0
lost = 0

move = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
while(move!= "play"):
    if(move == "exit"):
        flag = 1
        break
    if(move == "results") :
        print("You won: " + str(won) + " times.")
        print("You lost: " + str(lost) + " times." )
    move = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

step = 1
list1 = ["python", "java", "swift", "javascript"]
choice = random.choices(list1) # a list with one index that contains the word ['javascript']
x = choice[0]
chars = x[0:len(x)] # contains the word as a string         javascript
chars_list = [] # contains the list that each index has - ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
k = len(chars)
i=0
keep = []
while(i < k):
    a = chars[i]
    a = "-"
    chars_list.append(a)
    i = i+1
finalword ="".join(chars_list) # contains the word that pc chose with - as one word   ----------
chars_splitted = list(chars) # the letters from the word that pc chose splitted , each index is a letter ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']
tries = 8
if(move!="exit"):
    print()
    print(finalword)

while(move == "play"):
    if(step != 1):
        list1 = ["python", "java", "swift", "javascript"]
        choice = random.choices(list1) # a list with one index that contains the word ['javascript']
        x = choice[0]
        chars = x[0:len(x)] # contains the word as a string         javascript
        chars_list = [] # contains the list that each index has - ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        k = len(chars)
        i=0
        keep = []
        while(i < k):
            a = chars[i]
            a = "-"
            chars_list.append(a)
            i = i+1
        finalword ="".join(chars_list) # contains the word that pc chose with - as one word   ----------
        chars_splitted = list(chars) # the letters from the word that pc chose splitted , each index is a letter ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']
        tries = 8
        print()
        print(finalword)
    while(tries!=0):
        ans = input( "Input a letter: ")
        while(len(ans)!=1):
            print("Please, input a single letter.")
            print()
            finalword ="".join(chars_list)
            print(finalword)
            ans = input( "Input a letter: ")
        while(ans.islower()==False):
            print("Please, enter a lowercase letter from the English alphabet.")
            print()
            finalword ="".join(chars_list)
            print(finalword)
            ans = input( "Input a letter: ")
            while(len(ans)!=1):
                print("Please, input a single letter.")
                print()
                finalword ="".join(chars_list)
                print(finalword)
                ans = input( "Input a letter: ")

        while(len(ans)!=1):
            print("Please, input a single letter.")
            print()
            finalword ="".join(chars_list)
            print(finalword)
            ans = input( "Input a letter: ")
            while(ans.islower()==False):
                print("Please, enter a lowercase letter from the English alphabet.")
                print()
                finalword ="".join(chars_list)
                print(finalword)
                ans = input( "Input a letter: ")

        while(ans in keep):
            print("You've already guessed this letter.")
            print()
            finalword ="".join(chars_list)
            print(finalword)
            ans = input( "Input a letter: ")
            while(len(ans)!=1):
                print("Please, input a single letter.")
                print()
                finalword ="".join(chars_list)
                print(finalword)
                ans = input( "Input a letter: ")
            while(len(ans)!=1):
                print("Please, input a single letter.")
                print()
                finalword ="".join(chars_list)
                print(finalword)
                ans = input( "Input a letter: ")
                while(ans.islower()==False):
                    print("Please, enter a lowercase letter from the English alphabet.")
                    print()
                    finalword ="".join(chars_list)
                    print(finalword)
                    ans = input( "Input a letter: ")
            while(ans.islower()==False):
                print("Please, enter a lowercase letter from the English alphabet.")
                print()
                finalword ="".join(chars_list)
                print(finalword)
                ans = input( "Input a letter: ")
                while(len(ans)!=1):
                    print("Please, input a single letter.")
                    print()
                    finalword ="".join(chars_list)
                    print(finalword)
                    ans = input( "Input a letter: ")
        keep.append(ans)

        count = 0
        boolean = False
        while(len(chars_splitted)>count):
            if(ans == chars_splitted[count]):
                if(chars_list[count]== "-"):
                    chars_list[count] = ans
                    boolean = True
                count+=1
            else:
                count+=1
        if(boolean == True): #he guessed right letter for a first time putting that letter
            finalword ="".join(chars_list)
            print()
            print(finalword)
        elif(ans in chars and boolean==False): #if the input exists in the word but he has already guessed it
            tries-=1
            finalword ="".join(chars_list)
            print("No improvements.")
            print()
            print(finalword)
        else: #if the letter doesnt exist in the word
            tries-=1
            print("That letter doesn't appear in the word.\n")
            print(finalword)
        if(finalword == chars):
            print("you guessed the word " +chars+ "!")
            print("You survived!")
            won +=1
            tries = 0
    if(finalword!= chars):
        print()
        print("You lost!")
        lost+=1

    move = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    step = 2
    if(move == "play"):
        tries = 8
    while(move!= "play"):
        if(move == "exit"):
            tries = 0
            flag = 1
            break
        if(move == "results") :
            print("You won: " + str(won) + " times.")
            print("You lost: " + str(lost) + " times." )
        move = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')