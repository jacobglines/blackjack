"""
A ton of useful functions
"""

def is_number(number):
    """Returns True if number is a number else it returns False."""
    isInteger = True
    #
    # Remove leading and trailing whites space and
    # check for 4 special cases of non-integers. Then
    # remove any leading positive or negative signs.
    #
    number = str(number).strip()
    if number in  ['', '.', '+', '-']:
        isInteger = False
    if isInteger and number[0] in '+-':
        number = number[1:]
    #
    # Loop through the string checking to make sure
    # the characters are all legal number characters.
    #
    position = 0        
    legalValues = '0123456789.'
    while isInteger and position <= len(number)-1:
        if number[position] not in legalValues:
            isInteger = False
        if number[position] == '.':
            legalValues = '0123456789'
        position += 1       
    return isInteger

def is_integer(number):
    """Returns True is number is an interger else it returns False."""
    isInteger = True
    #
    # Remove leading and trailing whites space and
    # check for 4 special cases of non-integers. Then
    # remove any leading positive or negative signs.
    #
    number = str(number).strip()
    if number in  ['', '.', '+', '-']:
        isInteger = False
    if isInteger and number[0] in '+-':
        number = number[1:]                
    #
    # Loop through the string checking to make sure
    # the characters are all legal integer characters.
    #
    position = 0        
    legalValues = '0123456789.'
    while isInteger and position <= len(number)-1:
        if number[position] not in legalValues:
            isInteger = False
        if number[position] == '.':
            legalValues = '0'
        position += 1
        
    return isInteger
        
def get_yes_no(prompt):
    """Asks the user a yes or no question and returns 'yes' or 'no'. Will
       ask the user for clarification if it can't figure out what they
       mean."""
    answer = input(prompt)
    answer = str(answer)
    answer = str.lower(answer)
    #
    # Makes sure the user enters either yes or no
    #
    answerResponses = ["yes","Yes","YES","no","No","NO"]
    while answer not in answerResponses:
        print("Please enter either 'yes' or 'no'")
        answer = input("Yes or No? ")
    answer = answer.lower()
    return answer

def line_by_line(phrase, lineCount, waitTime):
    """Prints the given phrase and also allows for extra lines and a period of sleep
    to occur after the phrase is printed."""
    print(phrase)
    loopEnd = 0
    while loopEnd != lineCount:
        print()
        loopEnd += 1
    time.sleep(waitTime)

def money_formating(money):
    """Takes a number and converts it into a string that looks like money."""
    #
    # This section rounds the number to the length of money and then converts it into a string
    #
    money = round(money, 2)
    moneyString = str(money)
    #
    # This section checks the length of a string and applies the decimal and 0s
    # to the appropriate locations.
    #
    if len(moneyString) == 1:
        string = moneyString + ".00"
    elif len(moneyString) == 2:
        if moneyString[-1] == ".":
            string = moneyString + "00"
        elif moneyString[-2] == ".":
            string = moneyString + "0"
        else:
            string = moneyString + ".00"
    elif len(moneyString) >= 3:
        if moneyString[-1] == ".":
            string = moneyString + "00"
        elif moneyString[-2] == ".":
            string = moneyString + "0"
        elif moneyString[-3] == ".":
            string = moneyString
        else:
            string = moneyString + ".00"
    #
    # Adds a dollar sign so it looks like money.
    #
    string = "$" + string
    return string

def play_sound(soundFile):
    """Plays a .wav file"""
    if os.name == 'nt':
        winsound.playSound(soundFile,winsound.SND_ASYNC)
    else:
        sound = pyglet.media.load(soundFile, streaming=False)
        sound.play()

def get_positive_number(prompt):
    isPositive = False
    isNumber = False
    while isPositive == False:
        userInput = input(prompt)
        isNumber = is_number(userInput)
        if isNumber == True:
            userInput = int(userInput)
            if userInput > 0:
                isPositive = True
            else:
                pass
    userInput = int(userInput)
    return userInput

def get_integer(prompt):
    isInteger = False
    while isInteger == False:
        userAnswer = input(prompt)
        isInteger = is_integer(userAnswer)
    userAnswer = int(userAnswer)
    return userAnswer

def get_integer_between(prompt, lowestValue, highestValue, nonAnswer):
    userAnswer = nonAnswer
    while userAnswer > highestValue or userAnswer <lowestValue:
        userAnswer = get_integer(prompt)
    return userAnswer

def is_binary(number):
    """Returns True if number is binary else it returns False."""
    isBinary = True
    number = str(number).strip()
    if number in  ['', '.', '+', '-']:
        isBinary = False
    if isBinary and number[0] in '+-':
        isBinary = True
    position = 0        
    legalValues = '01+-'
    while isBinary and position <= len(number)-1:
        if number[position] not in legalValues:
            isBinary = False
        if number[position] == '.':
            legalValues = '01'
        position += 1
    return isBinary

def get_binary(prompt):
    isBinary = False
    while isBinary == False:
        userAnswer = input(prompt)
        isBinary = is_binary(userAnswer)
    userAnswer = int(userAnswer)
    return userAnswer

def ask_to_run(prompt):
    runProgram = get_yes_no(prompt)
    if runProgram == 'yes':
        runProgram = True
    else:
        runProgram = False
    return runProgram

def split(string,splitAt):
    counter = 0
    print('1')
    for character in string:
        print('2')
        if character == splitAt:
            place = counter
        counter +=1
    before = string[0]

def get_answer_list(question, itemList):
    print()
    counter = 0
    for item in itemList:
        counter += 1
        print(f"{counter}. {item}")
    answer = input(question)
    run = True
    while run == True and answer not in range(len(itemList) + 1):
        try:
            answer = int(answer)
            while answer not in range(len(itemList) + 1):
                print("That's not one of the options")
                prompt = question + f"(1 - {counter}): "
                answer = input(prompt)
                answer = int(answer)
            run = False
        except:
            print("That's not one of the options")
            prompt = question + f"(1 - {counter}): "
            answer = input(prompt)
    return itemList[answer - 1]

def split_string(string):
    """Returns a list of the words in a string."""
    wordList = []
    word = ''
    for character in string:
        if character != ' ':
            word = word + character
        else:
            wordList = wordList + [word]
            word = ''
    wordList = wordList + [word]
    return wordList
