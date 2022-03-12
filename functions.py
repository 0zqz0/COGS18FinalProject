def start_quiz():
    print("\n Hi! Welcome to the Meteorology Quiz!\n"
          "\n Today we will explore the weather in San Diego.\n")
    
    location()
    
def location():
    home = str(input("Do you currently live or have you lived in San Diego?"))
    ans = home.lower()
    
    if 'yes' in ans:
        statement = ("\n That's wonderful! Let's see how you know this place.\n")
    elif 'no' in ans:
        statement = ("\n No worries! Today you would learn a new place without even physically be there.\n")
    else:
        statement = ("\n Let's GO!\n")
    
    print(statement)
    quiz_choice()
    
def quiz_choice():
    
    """
    This function would generate a 3-question quiz from the question bank. Correctness is recorded.
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """
    
    import numpy
    
    score = 0
    quiz_content = numpy.random.choice([1, 2, 3, 4, 5, 6], size = 3, replace = False)
    
    for index in quiz_content:
        if index == 1:
            Q1 = str(input("Which is the windiest month in San Diego?"))
    
            if 'dec' in Q1.lower() or '12' in Q1:
                score += 1
                print("\n You got it!\n")
            else:
                print("\n Sorry, the correct answer would be December.\n")
        elif index == 2:
            Q2 = str(input("Which is the sunniest month in San Diego?"))
    
            if 'jun' in Q2.lower() or '6' in Q2:
                score += 1
                print("\n You got it!\n")
            else:
                print("\n Sorry, the correct answer would be June.\n")
        elif index == 3:
            Q3 = str(input("Which is the wettest month in San Diego?"))
    
            if 'nov' in Q3.lower() or '11' in Q3:
                score += 1
                print("\n You got it!\n")
            else:
                print("\n Sorry, the correct answer would be November.\n")
        elif index == 4:
            Q4 = str(input("Which is the warmest month in San Diego?"))
    
            if 'aug' in Q4.lower() or '8' in Q4:
                score += 1
                print("\n You got it!\n")
            else:
                print("\n Sorry, the correct answer would be Auguest.\n")
        elif index == 5:
            Q5 = str(input("Which is the coldest month in San Diego?"))
    
            if 'dec' in Q5.lower() or '12' in Q5:
                score += 1
                print("\n You got it!\n")
            else:
                print("\n Sorry, the correct answer would be December.\n")
        elif index == 6:
            Q6 = str(input("What is the driest month?"))
    
            if 'aug' in Q6.lower() or '8' in Q6:
                score += 1
                print("\n You got it!\n")
            else:
                print("\n Sorry, the correct answer would be Auguest.\n")

    ending(score)
    rate(score)
    
def ending(score):
    
    """
    This function would provide the participant with the final score.
    
    PARAMETERS
    ----------
    score : int
        Final score of the quiz.
    
    RETURNS
    -------
    score_statment : str
        Statement on final score of the quiz.
    """
    
    score_statment = ("\n Your score for this small quiz is {}. Thanks for your participation.\n".format(score))
    
    print(score_statment)
    return score_statment

def rate(score):
    
    """
    This function would let participant rate the quiz. A try/expect algothrim is used for detecting valid/invalid input.
    If the input is valid, different response would call for different rating score. 
    If the input invalid, it would recall the function with a warning.
    
    PARAMETERS
    ----------
    score : int
        Final score of the quiz.
    
    RETURNS
    -------
    none
    """
    
    rate_score = input("\n Please rate this quiz based on your experience in any aspect. Rating scale from 1 to 5, with 5 as the highest level.\n")
    
    try:
        rate_score = int(rate_score)
        
        if rate_score <= 2:
            print("\n Okay. Restart the quiz for you right now.\n"
                  "\n Welcome back.\n")
            quiz_choice()
        elif rate_score == 3:
            if score >= 2:
                print("\n Thanks for the feedback.\n")
            else:
                print("\n Your score is just so-so as well.\n")
            end_quiz()
        elif rate_score >= 4:
            print("\n Appreaciate your honesty.\n")
            end_quiz()
    except:
        print("\n Please enter the valid value.\n")
        rate(score)

def end_quiz():
    print("\n Goodbye!\n")