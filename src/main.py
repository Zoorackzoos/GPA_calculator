from src.grade_percent_towards_grade_number_converter import get_numerical_grade
#non-project libraries

#project libraries
from src.spring_2025_class_vars import *


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
    """
    my_dictionary =
    {
        "key1": "value1",
        "key2": 2,
        "key3": [1, 2, 3]
    }
    :return:
    """

    total_credit_points = 0
    total_credit_hours = 0

    """
    print(f" what's considered n A in one class might be different from a A in another class")
    print(f" the creator of this programmer didn't advocate for that in his design.")
    print(f' if you would like to advocate for that in the program. Email him and he will do so ')
    print()
    """

    for dictionary in spring_2025__master_var__lectures:
        print(f"\t{dictionary}")
        final_grade = dictionary["final grade"]
        print(f"\t\tfinal grade = {final_grade}")
        numerical_grade = get_numerical_grade(grade_percent=final_grade,tab_amount='\t\t\t')
        print(f"\t\tnumerical grade = {numerical_grade}")
        print(f"\t\tcredit hours = {dictionary['credits']}")
        print(f"\t\tgrade \t* \tcredits\t = total grade points")
        print(f"\t\t{numerical_grade} \t*\t {dictionary['credits']}\t = {numerical_grade * dictionary['credits']}")
    print()

if __name__ == "__main__":
    main()


