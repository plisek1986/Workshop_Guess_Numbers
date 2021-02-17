from random import randint


def get_number():
    """
    Returns: User input
    """
    # while loop to evaluate its correctness
    while True:
        try:
            user_input = int(input('Please provide number: '))
            break
        except ValueError:
            print('Provided value is not a number, please try again!')
    return user_input