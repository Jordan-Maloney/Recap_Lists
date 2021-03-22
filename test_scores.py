##
# test_scores.py
# Jordan Maloney
# 23/3/21

# Lists
class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 36, 49, 24, 26, 36]

# Variables
highest = 0
lowest = 50
both_classes_sum = 0


# Calculate the highest and lowest scores
for score in (class_a + class_b):
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

# Calculate the mean
for number in class_a:
    both_classes_sum += number
for number in class_b:
    both_classes_sum += number
mean = both_classes_sum / (len(class_a) + len(class_b))

# Test scores
print("The highest score was {}. The lowest score was {}. The average score was {:.0f}.".format(highest, lowest, mean))
for number in class_a:
    if number in class_b:
        print("Both classes have a score of {}.".format(number))
