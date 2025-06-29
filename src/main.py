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

    print_count = 0

    total_credit_points = 0
    total_credit_hours = 0

    """
    print(f" what's considered n A in one class might be different from a A in another class")
    print(f" the creator of this programmer didn't advocate for that in his design.")
    print(f' if you would like to advocate for that in the program. Email him and he will do so ')
    print()
    """

    for dictionary in spring_2025__master_var__lectures:
        print(print_count)
        print_count += 1

        print(f"\tdictionary :")
        print(f"\t\t{dictionary}")
        print()
        print(f"\tdictionary[\"informal name\"] = {dictionary["informal name"]}")
        print(f"\tdictionary[\"final grade\"] = {dictionary["final grade"]}")
        print(f"\t\ti'm gonna get your letter grade so i can calculate your GPA.")
        #print(f"\t\t i don't strictly have to do this but it seems easier :-/ ")
        final_grade_as_numerical_grade = get_numerical_grade(dictionary["final grade"], '\t\t\t')
        print(f"\t\tfinal_grade_as_numerical_grade = {final_grade_as_numerical_grade}")
        print(f"\tdictionary[\"credits\"] = {dictionary["credits"]}")
        print()
        print(f"\tgrade point calculation time!")
        print(f"\t\t(numerical grade) * (credit hours) = (grade points)")
        print(f"\t\t{final_grade_as_numerical_grade} * {dictionary['credits']} = (grade points)")
        print(f"grade points = {final_grade_as_numerical_grade * dictionary['credits']}")
        print()

if __name__ == "__main__":
    main()


