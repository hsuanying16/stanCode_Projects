"""
File: class_reviews.py
Name: Sharon
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1       # The number the user inputs to stop


def main():
    """
    input class name (SC001 or SC101)
    input score
    print the maximum, minimum, and average
    """
    classes = str(input('Which class? '))
    classes = classes.upper()  # case-insensitive
    count001 = 0
    count101 = 0
    total001 = 0
    total101 = 0
    max001 = 0
    min001 = 0
    max101 = 0
    min101 = 0
    if classes == str(EXIT):
        print('No class scores were entered')
    else:
        while True:
            if classes == 'SC001':
                score = int(input('Score: '))
                if min001 == 0:
                    min001 = score
                count001 += 1  # Update count001
                total001 += score  # Update total001
                if score > max001:  # Update max001 when the input SC001 score is higher than the original value
                    max001 = score
                if score < min001:  # Update min001 when the input SC001 score is lower than the original value
                    min001 = score
            elif classes == str('SC101'):
                score = int(input('Score: '))
                if min101 == 0:
                    min101 = score
                count101 += 1  # Update count101
                total101 += score
                if score > max101:  # Update max101 when the input SC101 score is higher than the original value
                    max101 = score
                if score < min101:  # Update main01 when the input SC101 score is lower than the original value
                    min101 = score
            elif classes == str(EXIT):
                print('=============SC001=============')
                if max001 == 0:
                    print('No score for SC001')
                else:
                    print('Max (001): ' + str(max001))
                    print('Min (001): ' + str(min001))
                    print('Avg (001): ' + str(total001 / count001))
                print('=============SC101=============')
                if max101 == 0:
                    print('No score for SC101')
                else:
                    print('Max (101): ' + str(max101))
                    print('Min (101): ' + str(min101))
                    print('Avg (101): ' + str(total101 / count101))
                break
            classes = str(input('Which class? '))
            classes = classes.upper()

    # classes = str(input('Which class? '))
    # classes = classes.upper()       # case-insensitive
    # if classes == str(EXIT):
    #     print('No class scores were entered')
    # elif classes == str('SC001'):
    #     # First input class is SC001
    #     score = int(input('Score: '))
    #     max001 = score
    #     min001 = score
    #     count001 = 1       # Count how many scores there are and will be used to calculate the SC001 average score
    #     total001 = score
    #     while True:
    #         classes = str(input('Which class? '))
    #         classes = classes.upper()
    #         if classes == str(EXIT):
    #             print('=============SC001=============')
    #             print('Max (001): ' + str(max001))
    #             print('Min (001): ' + str(min001))
    #             print('Avg (001): ' + str(total001 / count001))
    #             print('=============SC101=============')
    #             print('No score for SC101')
    #             break
    #         elif classes == str('SC001'):
    #             score = int(input('Score: '))
    #             count001 += 1           # Update count001
    #             total001 += score       # Update total001
    #             if score > max001:      # Update max001 when the input SC001 score is higher than the original value
    #                 max001 = score
    #             if score < min001:      # Update min001 when the input SC001 score is lower than the original value
    #                 min001 = score
    #         elif classes == str('SC101'):
    #             score = int(input('Score: '))
    #             max101 = score
    #             min101 = score
    #             count101 = 1
    #             total101 = score
    #             while True:
    #                 # if input any SC101 score
    #                 classes = str(input('Which class? '))
    #                 classes = classes.upper()
    #                 if classes == str(EXIT):
    #                     break
    #                 elif classes == str('SC001'):
    #                     score = int(input('Score: '))
    #                     count001 += 1
    #                     total001 += score
    #                     if score > max001:
    #                         max001 = score
    #                     if score < min001:
    #                         min001 = score
    #                 elif classes == str('SC101'):
    #                     score = int(input('Score: '))
    #                     count101 += 1       # Update count101
    #                     total101 += score   # Update total101
    #                     if score > max101:  # Update max101 when the input SC101 score is higher than the original value
    #                         max101 = score
    #                     if score < min101:  # Update min101 when the input SC101 score is lower than the original value
    #                         min101 = score
    #             print('=============SC001=============')
    #             print('Max (001): ' + str(max001))
    #             print('Min (001): ' + str(min001))
    #             print('Avg (001): ' + str(total001 / count001))
    #             print('=============SC101=============')
    #             print('Max (101): ' + str(max101))
    #             print('Min (101): ' + str(min101))
    #             print('Avg (101): ' + str(total101 / count101))
    #             break
    # elif classes == str('SC101'):
    #     # First input class is SC101
    #     score = int(input('Score: '))
    #     max101 = score
    #     min101 = score
    #     count101 = 1        # Count how many scores there are and will be used to calculate the SC101 average score
    #     total101 = score
    #     while True:
    #         classes = str(input('Which class? '))
    #         classes = classes.upper()
    #         if classes == str(EXIT):
    #             print('=============SC001=============')
    #             print('No score for SC001')
    #             print('=============SC101=============')
    #             print('Max (101): ' + str(max101))
    #             print('Min (101): ' + str(min101))
    #             print('Avg (101): ' + str(total101 / count101))
    #             break
    #         elif classes == str('SC101'):
    #             score = int(input('Score: '))
    #             count101 += 1           # Update count101
    #             total101 += score
    #             if score > max101:      # Update max101 when the input SC101 score is higher than the original value
    #                 max101 = score
    #             if score < min101:      # Update main01 when the input SC101 score is lower than the original value
    #                 min101 = score
    #         elif classes == str('SC001'):
    #             score = int(input('Score: '))
    #             max001 = score
    #             min001 = score
    #             count001 = 1
    #             total001 = score
    #             while True:
    #                 # if input any SC001 score
    #                 classes = str(input('Which class? '))
    #                 classes = classes.upper()
    #                 if classes == str(EXIT):
    #                     break
    #                 elif classes == str('SC001'):
    #                     score = int(input('Score: '))
    #                     count001 += 1
    #                     total001 += score
    #                     if score > max001:
    #                         max001 = score
    #                     if score < min001:
    #                         min001 = score
    #                 elif classes == str('SC101'):
    #                     score = int(input('Score: '))
    #                     count101 += 1
    #                     total101 += score
    #                     if score > max101:
    #                         max101 = score
    #                     if score < min101:
    #                         min101 = score
    #             print('=============SC001=============')
    #             print('Max (001): ' + str(max001))
    #             print('Min (001): ' + str(min001))
    #             print('Avg (001): ' + str(total001 / count001))
    #             print('=============SC101=============')
    #             print('Max (101): ' + str(max101))
    #             print('Min (101): ' + str(min101))
    #             print('Avg (101): ' + str(total101 / count101))
    #             break



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
