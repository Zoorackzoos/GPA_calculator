from src.grade_percent_towards_grade_number_converter import get_numerical_grade
from src.course_vars.spring_2025_vars import *
from src.course_vars.fall_2025_vars import *


"""
total grade points = grade (in 4.0 numeric) * credit hours 

GPA =   total grade points
        /
        total credit hours
"""

"""
master_var  ->  class_dictionary1   ->  course : durgadurga
                                        class_number : durgadurgadurga 
                class_dictionary2
"""


def main():
    #GPA_calculator(spring_2025__master_var__lectures,"")
    GPA_calculator(fall_2025__master,"")


def GPA_calculator(class_dictionary,tab_amount):
    """
    This calculates the GPA. you can see the output via the terminal.
    if you don't want to see the process of what getting the GPA
    was. then you can look at the end and see the decimal

    here is an example dictionary for class_dictionary:
    anthro_lecture = \
    {
        "course": "ANTH 242L 005",
        "class number": 4463,
        "days": "R",
        "time": "11:00AM -> 12:15PM",
        "location": "HAH-112 CITY",
        "credits": 3,
        "instructor": "Sefczek",
        "grading basis": "GRD",
        "final grade": 83.78,
        "informal name": "anthro lecture"
    }
    """
    total_grade_points = 0
    total_credit_hours = 0
    """
    print(f" what's considered n A in one class might be different from a A in another class")
    print(f" the creator of this programmer didn't advocate for that in his design.")
    print(f' if you would like to advocate for that in the program. Email him and he will do so ')
    print()
    """
    print(f"{tab_amount}inside GPA_calculator")
    for dictionary in class_dictionary:
        #getting the final grade. which is a number.
        print(f"{tab_amount}\t{dictionary}")
        final_grade = dictionary["final grade"]
        print(f"{tab_amount}\t\tfinal grade = {final_grade}")

        #turning that number into a letter. this depends on the class, so this isn't 100% accurate.
        numerical_grade = get_numerical_grade(grade_percent=final_grade, tab_amount='\t\t\t')
        print(f"{tab_amount}\t\tnumerical grade = {numerical_grade}")

        #getting the credit hours. you need this for GPA calculation
        print(f"{tab_amount}\t\tcredit hours = {dictionary['credits']}")

        #calculate incoming_grade_points, we calculate incoming_grade_points for each class
        incoming_grade_points = numerical_grade * dictionary['credits']
        print(f"{tab_amount}\t\tgrade \t* \tcredits\t = total grade points")
        print(f"{tab_amount}\t\t{numerical_grade} \t*\t {dictionary['credits']}\t = {incoming_grade_points} \n")

        total_grade_points += incoming_grade_points
        total_credit_hours += dictionary['credits']

    print(f"{tab_amount}total_grade_points / total_credit_hours = GPA")
    GPA = total_grade_points / total_credit_hours
    print(f"{tab_amount}{total_grade_points} / {total_credit_hours} = {GPA}")
    return GPA

if __name__ == "__main__":
    main()


