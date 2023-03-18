import random,time
user=input("Hi,Welcome to Hangman")
print("Start Guessing the word")
time.sleep(0.5)
word_list=['PYTHON','JAVA','CODING','PROGRAMMING']
word=random.choice(word_list).upper()
Total_Chances=10
guessed_word='-'*len(word)
while Total_Chances!=0:
    print(guessed_word)
    letter_Entered=input("Please,Guess a letter: ")
    if letter_Entered in word:
        for index in range(len(word)):
            if word[index]==letter_Entered:
                guessed_word=guessed_word[:index]+letter_Entered+guessed_word[index+1:]
        if guessed_word==word:
            print()
            print("Kudos,You are the Winner!")
            break
    else:
        Total_Chances=Total_Chances-1
        print("Sorry,Wrong Guess")
        print("The remaining chances are: ",Total_Chances)
else:
    print("Game is Over")
    print("All chances are done!!")
    print("Better luck next time")
print("Correct word is ",word)