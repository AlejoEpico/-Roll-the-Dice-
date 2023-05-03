import random

def roll_dice():
    dice_draws = {
        1: '''
            +-------+
            |       |
            |   1   |
            |       |
            +-------+
           ''',

        2: '''
            +-------+
            |       |
            | 2   2 |
            |       |
            +-------+
           ''',

        3: '''
            +-------+
            |     3 |
            |   3   |
            | 3     |
            +-------+
           ''',

        4: '''
            +-------+
            | 4   4 |
            |       |
            | 4   4 |
            +-------+
           ''',

        5: '''
            +-------+
            | 5   5 |
            |   5   |
            | 5   5 |
            +-------+
           ''',

        6: '''
            +-------+
            | 6   6 |
            | 6   6 |
            | 6   6 |
            +-------+
           ''',
    }

    roll = input("Roll the dice? (YES/NO): ")

    while roll.lower() == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('dice rolled: {} and {} '.format(dice1, dice2))
        roll = input("Roll again ?  (YES/NO): ")
        print(dice_draws[dice1])
        print(dice_draws[dice2])


roll_dice()
