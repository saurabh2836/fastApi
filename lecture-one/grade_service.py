

def calculate_homework(homework_assignemnts_arg):
    sum_of_grades =0
    for homework in homework_assignemnts_arg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(homework_assignemnts_arg),2)

    print(final_grade)
    print("hi")
