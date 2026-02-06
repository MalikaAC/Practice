grade = 4
match grade:
    case 5:
        print("Excellent")
    case 4:
        print("Good")
    case 3:
        print("Satisfactory")
    case 2:
        print("Fail")


mood = 1
match mood:
    case 1:
        print("Happy")
    case 2:
        print("Sad")
    case _:
        print("Neutral")


hour = 14
match hour:
    case 6 | 7 | 8 | 9 | 10 | 11:
        print("Morning")
    case 12 | 13 | 14 | 15 | 16 | 17:
        print("Afternoon")
    case _:
        print("Evening or night")


score = 4
exam = "math"
match score:
    case 4 | 5 if exam == "math":
        print("Good result in math")
    case 4 | 5 if exam == "english":
        print("Good result in english")
    case _:
        print("Result not considered")

level = 3
mode = "hard"
match level:
    case 1 | 2 | 3 if mode == "easy":
        print("Easy mode")
    case 1 | 2 | 3 if mode == "hard":
        print("Hard mode")
    case _:
        print("Other mode")
