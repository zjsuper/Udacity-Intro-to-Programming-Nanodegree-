
test = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
'''Conventionally, a modern computer consists of at least one processing element, typically a ___1___ (CPU), and some form of ___2___. The processing element carries out arithmetic and logical operations, and a sequencing and control unit can change the order of operations in response to stored ___3___. ''',
'''Alan Mathison Turing was a pioneering English ___1___ scientist. He was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of ___2___ and computation with the ___3___ machine, which can be considered a model of a general purpose computer. Turing is widely considered to be the father of theoretical computer science and ___4___ intelligence.''']

blanks = ["___1___", "___2___", "___3___", "___4___"]
answer_sets = [["function","input","none","list"],
["central processing unit","memory","information"],
["computer","algorism","Turing","artificial"]]


#To start the game and select a level.
#Output:Return the quiz and according answer the user select.
def select_level(): 
    start = raw_input("Do you want a game? Yes or No: ")
    if start.lower() == "yes":
        print " "
        print "Let's start!"
        print " "
        print "We have 3 tests, which one do you want to take?"
        print " "
        choosetest = raw_input("1, 2 or 3: ")
        print " "
        test_index = int(choosetest) - 1
        current_quiz = test[test_index]
        current_answer = answer_sets[test_index]
        return current_quiz, current_answer
    else:
        return "See you next time!"," "

current_quiz, current_answer = select_level()
print current_quiz

#main body of the game
#Input: current quiz player have chosen.
#Output: Lead the user play the game and give according feedback.
def play_game(current_quiz):
    blankindex = 0
    count = 2
    while blankindex < len(current_answer):
        user_input = raw_input("What is the answer for blank " + str(blankindex + 1) + "?  ")
        if user_input == current_answer[blankindex]:
            print "correct!"
            current_quiz = current_quiz.replace(blanks[blankindex],user_input)
            print current_quiz
            blankindex += 1
            if blankindex == len(current_answer):
                print current_quiz
                print "Great! You've passed the test."
                exit()
            count = 2
        else:
            count -= 1
            if count == 0 :
                print "Game over!"
                quit()
            print "Wrong. Try agian and you only have last " + str(count) + " chance."               
            
#run the game    
if current_quiz != "See you next time!":
    play_game(current_quiz)      
    

