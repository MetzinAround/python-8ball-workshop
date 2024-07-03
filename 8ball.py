import random
import time
#REMOVE ME
#This section creates a list of all the possible replies and prints out an ASCII 8ball with a pause between each line. This is to indicate that the code has started running. 
answers = ["It is certain", "It is decidely so", "Without a doubt", "Yes Definitely", "You may rely on it", "As I see it, yes", "Most Likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot Predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
print("  .-'''-.")
time.sleep(.5)
print(" /   _   \\")
time.sleep(.5)
print(" |  (8)  |")
time.sleep(.5)
print(" \   ^   /")
time.sleep(.5)
print("  '-...-'")

#The main function of the 8ball. 
def ask_the_ball():
    #asks the user to input a name and questions.  
    name = input("What is your name?")
    #capitalizes the name with .upper
    cap_name = name.upper()
    question = input("What would you like an answer to?")
    cap_question = question.upper()
    #This uses random to create a random integer between two numbers, in this case 0 and the length of the list minus 1 to account for 0 indexing. 
    get_the_i = random.randint(0, len(answers)-1)
    #this selectes the answer by using the random number as the index from the list
    answer = answers[get_the_i]

    #fun filler to pretend like it's thinking
    print(f"{cap_name}, you asked {cap_question}.")
    print("Pondering the Orb")
    time.sleep(random.randint(1, 5))
    print("🔮 ✨ 🔮")
    time.sleep(1)
    print(f"{answer}")
    ask_again = input("Would you like to ask again? yes/no ")
    #runs play again to check if user wants another round
    play_again(ask_again)

#if the user answers something other than yes or no, this frunction runs with a new input
def wrong_answer(user_answer2):
    play_again(user_answer2)

#play again is the logic for deciding how the player answered about another question
def play_again(user_answer):
    #upper case to account for random capitalization
    more = user_answer.upper()
    #if yes, runs ask_the_ball again
    if more == "YES":
        ask_the_ball()
    #exits program
    elif more == "NO":
        print("Thank you for playing.")
        exit()
    #any answer other than yes or no reminds the user to use an approved answer 
    else:
        wrong = input("Please type 'yes' or 'no'. ")
        wrong_answer(wrong)
        
#runs the game function    
if __name__ == "__main__":
    ask_the_ball()
