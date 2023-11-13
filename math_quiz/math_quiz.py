import random


def RandomInteger(min, max):
    """
    Creates a random integer in a given intervall
    
    Parameters
    ----------
    min : int
        Lower limit of intervall
    max : int
        Upper limit of intervall
        
    Returns
    -------
    int
        Random integer in given intervall
        
    """

    return random.randint(min, max)


def ChooseOperation():
    """
    Chooses randomly a mathematical operation out of ('+', '-', '*')
    
    Parameters
    ----------
    None
        
    Returns
    -------
    
        Random mathematical operation out of ('+', '-', '*')
        
    """
    
    return random.choice(['+', '-', '*'])


def ExecuteCalculation(n1, n2, o):
    """
    Calculate the result of two numbers depending on a given operation
    
    Parameters
    ----------
    n1 : int
        First number for the calculation
    n2 : int
        Second number for the calculation
    o : 
        Mathematical operation for the calculation
        
    Returns
    -------
    int
        Result of two numbers depending on a given operation
        
    """
    
    p = f"{n1} {o} {n2}"
    
    if o == '-': 
        a = n1 - n2
        # When the given operation is '-', the numbers are subtracted
    elif o == '+': 
        a = n1 + n2
        # When the given operation is '+', the numbers are added
    else: 
        a = n1 * n2
        # When the given operation is '*', the numbers are multiplied
    return p, a

def math_quiz():
    s = 0
    t_q = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(t_q):
        n1 = RandomInteger(1, 10); n2 = RandomInteger(1, 5); o = ChooseOperation()

        PROBLEM, ANSWER = ExecuteCalculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
