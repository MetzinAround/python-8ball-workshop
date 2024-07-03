# Code Breakdown

This app uses several functions so that a user can get an answer to a yes or no question asked of the app. We'll go through it in chunks of lines to discuss how the app works. The next section will define one way to run this workshop using the PRIMM method. 

## Import statements and initial List. 

```python
import random
import time
```
In order to use a random number easily, we use the `import random` statement. This gives us access to `.randint()` later so we can have the program pick a random number within given parameters. This will be how the 8-ball "selects" the response. `import time` is purely aesthetic; we use this when making an ASCII image in the beginning and later when the program is "thinking" about the answer to the user. 

```python
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
```
The first thing we do is define a list to hold all our answers. We created a list of several clear affirmatives, somewhat affirmatives, neutrals, somehwat negatives, and clear negatives for answers to choose from. We name this list `answers` and will call on it later. Finally, for fun, we line by line print an ASCII image of an 8ball to the console with half a second between each line using the `.sleep()` time method. All input questions input by the user and the questions will be in the terminal when you run the code. 

## Main game function

The function `ask_the_ball()` is the central function of the app. It contains all the element needed to run the app successfully. Without any other function, this will answer the users questions, however, we use other functions later to cover more questions the user may want to ask as well as incorrect inputs. 

```python 
def ask_the_ball():
    #asks the user to input a name and questions. .upper() turns the string into all caps. 
    name = input("What is your name?")
    #capitalizes the name
    cap_name = name.upper()
    question = input("What would you like an answer to?")
    cap_question = question.upper()
    #This uses random to create a random integer between two numbers, in this case 0 and the length of the list minus 1 to account for 0 indexing. 
    get_the_i = random.randint(0, len(answers)-1)
    #this selectes the answer by using the random number as the index from the list
    answer = answers[get_the_i]
```

This function opens by defining a variable for the users name to personalize the game. This is then put in all caps using `.upper()` for aesthetic reasons. After that, we ask for more input to get a question to answer from the user, which we also capitalize. We then use `random.randint()` to create a random number. `randint()` takes two parameters: a starting number and an ending number, non inclusive. In order to not run into an error from receiving a number out of range of the list, we use the length of the answers list minus 1. This is a great opportunity to remind students of "off by one" errors. The number that `randint()` creates is saved in the variable `get_the_i` and that is used to pick the element from the list that will represent our `answer`. 

```python
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
```

We print the name and question the user asked as a reminder before the computer "Ponders the Orb" to think for a moment. We use `randomint()` again to determine how long the app will sleep before coming up with the answer. Finally, we print the answer taken from `answers[get_the_i]` This could be where theapp ends, but we wanted some replayability without having to completely restart the app. `ask_again` is the user input to the question "Would you like to play again? yes/no." We pass that into the function `play_again()`, which we'll discuss now. 

## play_again() and wrong_answer()

We have two more functions: `play_again()` to run the program once more with a new input and `wrong_answer()` to deal with an answer other than yes or no. Let's explore `play_again()` first. 

```python
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
```

Once again, we use `.upper()` to get a standard input, no matter what the user enters. This makes it easier to write the if statement here since we know that we'll only ever pass an upper case word into the function. Using an if statement, we check for `YES` or `NO` and either run the app again or exit the program. For anything that isn't `YES` or `NO`, we print a reminder of what explicitly we are trying to receive as an answer. This is taken as user input and set equal to the vraible `wrong` which is then passed into our other function, `wrong_answer()`. 

```python
def wrong_answer(user_answer2):
    play_again(user_answer2)
```
`wrong_answer()` just takes in one parameter and plugs it into `play_again()`. So when we run `wrong_answer()` during the else statement at the end of `play_again()`, we input the user answer to the reminder statement of "Please type yes or no". The very last line in the file runs checks if the file being run has a name of `"__name__"` and then runs `ask_the_ball()`, our main function that runs the game so that when we run the file, the program starts. 


<!-- testing --> 