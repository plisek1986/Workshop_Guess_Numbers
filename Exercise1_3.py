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

def user_choice():
    """
    Returns: The list of numbers selected by the user
    """
    available_numbers = list(range(1, 50))
    result_user = []
    while len(result_user) < 6:
        number = get_number()
        if number in available_numbers and number not in result_user:
            result_user.append(number)
        result_user.sort()
    print(result_user)
    return result_user