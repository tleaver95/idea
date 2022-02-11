# imports

# variables

currentQuestion = ""
questionMarks = 0
questionMarksLoop = False


# user creates questions and answers which are added to a csv file
def makingQuestions():
    questionMarksLoop = False
    global a_file
    #  validating inputs so they are int
    while questionMarksLoop == False:
        questionMarks = input("how many marks is this question?")
        if questionMarks.isdigit():
            questionMarksLoop = True
            #  allows user to determine number of marks a question is
            for i in range(int(questionMarks) + 1):
                currentQuestion = input("Give the question followed by an appropriate amount of answers")
                a_file = open("Questions.txt", "a")
                a_file.write(currentQuestion + ",")
                print("Added to data base")
            # starts a new line outside of loop
            a_file.write("\n")
        else:
            print("you must enter a valid number")


makingQuestions()


#  need to remove the last comma when adding information to csv.
#  need to figure out how to add the spaced repetition to the csv after the question has been created.
#  maybe use different text files to store different subjects ect
#  once achieved above need to make the section that asks the questions