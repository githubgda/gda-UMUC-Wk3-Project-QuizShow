# =================================
# Print game title using ASCII Art
# =================================
# "Quiz Time! You Game ?" is represented in what is known as ASCII Art, which gets 
# its name from the characters available in an "ASCII" chart (technical speak
# for how text is represented in memory).

#You can find "ASCII Art Generators" sites on the internet, by search for it.

# The Python feature "r-strings" is display each of the ASCII characters without any processing.
# For our purposes, we use them with triple quotation marks, and simply copy/paste our ASCII art 
# into the middle, like so:



print(r"""
  ______             __                  ________  __                          __             
 /      \           |  \                |        \|  \                        |  \            
|  $$$$$$\ __    __  \$$ ________        \$$$$$$$$ \$$ ______ ____    ______  | $$            
| $$  | $$|  \  |  \|  \|        \         | $$   |  \|      \    \  /      \ | $$            
| $$  | $$| $$  | $$| $$ \$$$$$$$$         | $$   | $$| $$$$$$\$$$$\|  $$$$$$\| $$            
| $$ _| $$| $$  | $$| $$  /    $$          | $$   | $$| $$ | $$ | $$| $$    $$ \$$            
| $$/ \ $$| $$__/ $$| $$ /  $$$$_          | $$   | $$| $$ | $$ | $$| $$$$$$$$ __             
 \$$ $$ $$ \$$    $$| $$|  $$    \         | $$   | $$| $$ | $$ | $$ \$$     \|  \            
  \$$$$$$\  \$$$$$$  \$$ \$$$$$$$$          \$$    \$$ \$$  \$$  \$$  \$$$$$$$ \$$            
      \$$$                                                                                    
                                                                                              
                                                                                              
 __      __                           ______                                            ____  
|  \    /  \                         /      \                                          /    \ 
 \$$\  /  $$______   __    __       |  $$$$$$\  ______   ______ ____    ______        |  $$$$\
  \$$\/  $$/      \ |  \  |  \      | $$ __\$$ |      \ |      \    \  /      \        \$$| $$
   \$$  $$|  $$$$$$\| $$  | $$      | $$|    \  \$$$$$$\| $$$$$$\$$$$\|  $$$$$$\         /  $$
    \$$$$ | $$  | $$| $$  | $$      | $$ \$$$$ /      $$| $$ | $$ | $$| $$    $$        |  $$ 
    | $$  | $$__/ $$| $$__/ $$      | $$__| $$|  $$$$$$$| $$ | $$ | $$| $$$$$$$$         \$$  
    | $$   \$$    $$ \$$    $$       \$$    $$ \$$    $$| $$ | $$ | $$ \$$     \        |  \  
     \$$    \$$$$$$   \$$$$$$         \$$$$$$   \$$$$$$$ \$$  \$$  \$$  \$$$$$$$         \$$  
                                                                                              
                                                                                              
                                                                                              
""")

#Print game introduction and instruction
print("Welcome to Quiz Time! You will answer a few True or False questions. Please only enter the letter 'T' (for True) or 'F' (for False) when it's your turn to answer. Have fun!")

# Add a blank line to seperate previous text displayed from next print out
print()

# Setup series of True and False Questions and Answers
questions = ('Q1. A square has only three equal sides','Q2. Integers are whole numbers','Q3. Booleans can store decimal values','Q4. The sum of the all the angels inside a triangle is equal to 180 degrees','Q5. An interger divided by zero is a valid math operation','Q6. Python is a compiler programming language','Q7. The Python keyword "int" means interrupt','Q8. Floating Points are use to keep boats afloat','Q9. The "*" is use to perform division in the Python Programming Language','Q10. For and While Loops allow one to perform redundant tasks multiple time')
answers = ('F', 'T', 'F', 'T', 'F', 'F', 'F', 'F', 'F', 'T')

# Calculate the number of questions
numberOfQuestions = len(questions)

# Initialize variables used in program
answerResponse = ""
numberCorrect = 0

#Ask the question and ask player to answer True or Falser
# Loop once for each question and ask question again if a capital 'T' or 'F' is not entered

for index in range(numberOfQuestions):
  print(f"Prompt: {questions[index]}")
  answerResponse = input("Please only enter the letter #'T' (for True) or 'F' (for False): ")
  while (answerResponse != "T") and (answerResponse != "F"):
    answerResponse = input("Please only enter the letter 'T' (for True) or 'F' (for False): ")
    
  # Add a blank line to seperate previous text displayed from next print out
  print()

# Calcule the number of correct answers
  if answerResponse == answers[index]:
    numberCorrect = numberCorrect + 1

#Print the number of questions that were answered correctly
print(f"You got {numberCorrect} out of {numberOfQuestions} questions correct! Thanks for playing!")
  
# The End