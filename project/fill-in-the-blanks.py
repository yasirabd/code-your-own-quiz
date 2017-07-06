# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

# A bunny story fill-in-the-blanks and its corresponding answers.
bunny_story = ["Once there was an ugly","___1___","named Kevin. He was","___2___","and nobody liked him. One day there was a Bhutan Marathon and the ugly bunny","___3___",". He got a","___4___","and then everybody liked him. He made lots of new","___5___","and lived happily ever after."]
bunny_answers = ["bunny", "ugly", "won", "medal", "friends"]

# Kites story fill-in-the-blanks and its corresponding answers
kites_story = ["There was once a boy called Sam. He was very","___1___",". He lived with his","___2___","named Sigrid. One day he found","___3___","gold coins and","___4___","silver coins. Then he went and bought some paper and crayons, made","___5___","kites and sold them. Then he took the money and bought a wardrobe, a car, a black dress for his mom and lots of gifts for his house and became very","___6___","."]
kites_answers = ["poor", "mother", "50", "25", "1000", "rich"]

# The Cat story fill-in-the-blanks and its corresponding answers
cat_story = ["Once upon a time there was a","___1___","named Susan. She","___2___","cats. She","___3___","had a cat before but one day she got a cat for her now and then. The cat's name was Harry. Susan loved Harry. She","___4___","with it and","___5___","it sooo much. Her","___6___",", named Robb, disliked the cat but her mom loved it. Susan","___7___","it and loved it so much. They all lived very ever after."]
cat_answers = ["girl", "loved", "never", "slept", "loved", "dad", "pet"]
