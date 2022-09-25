# Student data
st1 = {"name": "Ryan",
       "assignment": [80, 50, 40, 20, 60],
       "theory_test": [75, 75],
       "lab_test": [78.20, 77.20],
       "mini_project": 70,
       }

st2 = {"name": "Alex",
       "assignment": [70, 50, 80, 20, 60],
       "theory_test": [75, 85],
       "lab_test": [78.20, 35.20],
       "mini_project": 80,
       }

st3 = {"name": "Lucy",
       "assignment": [80, 50, 40, 20, 60],
       "theory_test": [75, 75],
       "lab_test": [78.20, 77.20],
       "mini_project": 90,
       }

st4 = {"name": "Sam",
       "assignment": [90, 90, 40, 20, 60],
       "theory_test": [75, 85],
       "lab_test": [88.20, 77.20],
       "mini_project": 60,
       }

st5 = {"name": "Ben",
       "assignment": [80, 50, 40, 20, 60],
       "theory_test": [73, 85],
       "lab_test": [78.20, 77.20],
       "mini_project": 70,
       }

# Returns corresponding Grade


def gradingPattern(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "c"
    elif score >= 50:
        return "D"
    elif score >= 35:
        return "E"
    elif score < 35:
        return "F"

# Calculates the total score by taking student dictionaries as input


def calcScore(student):
    total_score = 0
    avg = findAverage(student["lab_test"])
    student["lab_test"] = avg*(0.3)
    total_score += avg*(0.3)
    avg = findAverage(student["assignment"])
    student["assignment"] = avg*(0.1)
    total_score += avg*(0.1)
    avg = findAverage(student["theory_test"])
    student["theory_test"] = avg*(0.5)
    total_score += avg*(0.5)
    # avg = findAverage(student["mini_project"])
    student["mini_project"] = avg*(0.1)
    total_score += avg*(0.1)
    return total_score

# Returns Average


def findAverage(marks_list):
    sum = 0
    for x in marks_list:
        sum += x
    avg = sum/len(marks_list)
    return avg


# Main code
sum_students = calcScore(st1) + calcScore(st2) + \
    calcScore(st3) + calcScore(st4) + calcScore(st5)
avg_students = sum_students/5
avg_grade = gradingPattern(avg_students)
print(f"The Average score of the class is {avg_students}")
print(f"And the Average grade is {avg_grade}")
