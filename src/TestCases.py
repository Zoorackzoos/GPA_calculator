import inspect
import unittest

from src.main import GPA_calculator


class MasterTesterGPACalculator(unittest.TestCase):
    """
    this is a test case class.
    """

    """
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
    math_class = \
        {
            "course": "math",
            "class number": 1,
            "days": "MTWRF",
            "time": "8:00AM -> 9:00AM",
            "location": "100",
            "credits": 4,
            "instructor": "FuckFace",
            "grading basis": "GRD",
            "final grade": 100.0,
            "informal name": "math class"
        }

    art_class = \
        {
            "course": "art",
            "class number": 2,
            "days": "MTWRF",
            "time": "9:15AM -> 10:00AM",
            "location": "101",
            "credits": 4,
            "instructor": "BitchTits",
            "grading basis": "GRD",
            "final grade": 100.0,
            "informal name": "art class"
        }

    science_class = \
        {
            "course": "science",
            "class number": 3,
            "days": "MTWRF",
            "time": "10:15AM -> 11:00AM",
            "location": "102",
            "credits": 4,
            "instructor": "CarpetMuncher",
            "grading basis": "GRD",
            "final grade": 100.0,
            "informal name": "science class"
        }

    master_var = \
        [
            math_class,
            art_class,
            science_class,
        ]

    def test_all_As__good_student(self):

        """
        self.math_class["final grade"] = 100.0
        self.art_class["final grade"] = 100.0
        self.science_class["final grade"] = 100.0
        """

        #this line just prints the test case's name
        print("Test = " + inspect.currentframe().f_code.co_name)
        computer_result = GPA_calculator(self.master_var,"\t")
        correct_result = 4.0
        print(f"computer_result = correct_result")
        print(f"{computer_result} = {correct_result}")
        print(computer_result == correct_result)
        self.assertEqual(computer_result,correct_result)

    def test_all_As__over_achiever(self):

        self.math_class["final grade"] = 200.0
        self.art_class["final grade"] = 200.0
        self.science_class["final grade"] = 200.0

        #this line just prints the test case's name
        print("Test = " + inspect.currentframe().f_code.co_name)
        computer_result = GPA_calculator(self.master_var,"\t")
        correct_result = 4.0
        print(f"computer_result = correct_result")
        print(f"{computer_result} = {correct_result}")
        print(computer_result == correct_result)
        self.assertEqual(computer_result,correct_result)

    def test_all_Fs__Absentee(self):


        self.math_class["final grade"] = 0.0
        self.art_class["final grade"] = 0.0
        self.science_class["final grade"] = 0.0


        #this line just prints the test case's name
        print("Test = " + inspect.currentframe().f_code.co_name)
        computer_result = GPA_calculator(self.master_var,"\t")
        correct_result = 0.0
        print(f"computer_result = correct_result")
        print(f"{computer_result} = {correct_result}")
        print(computer_result == correct_result)
        self.assertEqual(computer_result,correct_result)

    def test_all_Fs__shit_student(self):


        self.math_class["final grade"] = 50.0
        self.art_class["final grade"] = 50.0
        self.science_class["final grade"] = 50.0


        #this line just prints the test case's name
        print("Test = " + inspect.currentframe().f_code.co_name)
        computer_result = GPA_calculator(self.master_var,"\t")
        correct_result = 0.0
        print(f"computer_result = correct_result")
        print(f"{computer_result} = {correct_result}")
        print(computer_result == correct_result)
        self.assertEqual(computer_result,correct_result)

    def test_all_Cs(self):


        self.math_class["final grade"] = 70.0
        self.art_class["final grade"] = 70.0
        self.science_class["final grade"] = 70.0


        #this line just prints the test case's name
        print("Test = " + inspect.currentframe().f_code.co_name)
        computer_result = GPA_calculator(self.master_var,"\t")
        correct_result = 1.7
        print(f"computer_result = correct_result")
        print(f"{computer_result} = {correct_result}")
        print(computer_result == correct_result)
        self.assertEqual(computer_result,correct_result)