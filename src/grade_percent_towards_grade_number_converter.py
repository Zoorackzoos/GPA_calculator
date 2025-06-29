



def get_numerical_grade(grade_percent, tab_amount):
    print(f"{tab_amount}i'm inside ! get_numerical_grade !  now.")
    if grade_percent >= 94:
        print(f'{tab_amount}you got a \t A')
        print(f'{tab_amount}\tgood job !')
        print(f"{tab_amount}A -> 4.0")
        return 4.0
    elif grade_percent >= 90:
        print(f'{tab_amount}you got a \t A-')
        print(f'{tab_amount}\tgood job !')
        print(f"{tab_amount}A- -> 3.7")
        return 3.7
    elif grade_percent >= 87:
        print(f'{tab_amount}you got a \t B+')
        print(f'{tab_amount}\tgood job !')
        print(f"{tab_amount}B -> 3.3")
        return 3.3
    elif grade_percent >= 84:
        print(f'{tab_amount}you got a \t B')
        print(f'{tab_amount}\tgood job !')
        print(f"{tab_amount}B -> 3.0")
        return 3.0
    elif grade_percent >= 80:
        print(f'{tab_amount}you got a \t B-')
        print(f"{tab_amount}B- -> 2.7")
        return 2.7
    elif grade_percent >= 77:
        print(f'{tab_amount}you got a \t C+')
        print(f"{tab_amount}C+ -> 2.3")
        return 2.3
    elif grade_percent >= 74:
        print(f'{tab_amount}you got a \t C')
        print(f"{tab_amount}C- -> 2.0")
        return 2.0
    elif grade_percent >= 70:
        print(f'{tab_amount}you got a \t C-')
        print(f"{tab_amount}C- -> 1.7")
        return 1.7
    elif grade_percent >= 67:
        print(f'{tab_amount}you got a \t D+')
        print(f"{tab_amount}D+ -> 1.3")
        return 1.3
    elif grade_percent >= 64:
        print(f'{tab_amount}you got a \t D')
        print(f"{tab_amount}D- -> 1.0")
        return 1.0
    elif grade_percent >= 60:
        print(f'{tab_amount}you got a \t D-')
        print(f"{tab_amount}D- -> 0.7")
        return 0.7
    else:
        print(f'{tab_amount}you got a \t F')
        print(f"{tab_amount}F -> 0.0")
        return 0.0