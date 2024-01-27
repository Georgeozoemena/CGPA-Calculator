import asyncio

# Menu List of Architecture Year2 courses, if chosen by the user
def Year2():
    print(
    """
    ##Courses##
    1. ARC245(History of Architecture)
    2. ARC212(Architectural Design II)
    """
)

# Menu List of Departments in the faculty of Environmental Sciences
async def departments():
    print('Loading...')

    # Displays list of departments in the faculty of Environmental Sciences, After 3seconds
    await asyncio.tasks.sleep(3)
    print("""
    ***Environmental Sciences***

    1. Architecture
    2. Building
    3. Estate management
    4. Environmental management
    5. Fine and Applied Art
    6. Geomet
    7. Quantity Surveying
    8. Surveying
    """)

# Conditional statement of User's Grade and score
def Students_Score():  
    if stud_score >= 0 and stud_score <= 39:
        return 'F'
    elif stud_score >= 40 and stud_score <= 44:
        return 'E'
    elif stud_score >= 45 and stud_score <= 49:
        return 'D'
    elif stud_score >= 50 and stud_score <= 59:
        return 'C'
    elif stud_score >= 60 and stud_score <= 69:
        return 'B'
    elif stud_score >= 70 and stud_score <= 100:
        return 'A'
    else:
        print("Grades can't exceed 100")

# Calculate the Quality Point(QP) of the user
def selectedCourse():
    return creditload * stud_score


# Requiring Bio from user
# - Greet the user, after a 3seconds of the users input(using an Asynchronous function)
async def Greet():
    import time

    get_username = str(input("Can I know your name please? "))
    await asyncio.sleep(1)
    print("Hi there! {}.".format(get_username.title()))

    time = time.localtime().tm_hour
    if time >= 0 and time <= 11:
        print("Good morning")
    elif time >= 12 and time <= 15:
        print("Good Afternoon")
    else:
        print('Good evening')


asyncio.run(Greet())
# Calling the departments function(That hosting the departments menu)
asyncio.run(departments())

# - Request user's Department
stud_dept = int(input("Department? "))
if stud_dept == 1:
    print('***Architecture***')

    # Requires user's level
    stud_level = int(input("Level: "))
    
    # For students currently in 200lvl
    if stud_level == 200:

        # Display List of 200lvl courses
        Year2()

        stud_course = int(input("Course? "))
        if stud_course == 1:

            # Architectural Courses(Year2)
            # 1. ARC245
            course = 'ARC245'
            creditload = 4

            stud_score = float(input("Your Score? "))
            print(f'***{course}***\nCredit Unit: {creditload}')

            # Script to calculate Quality Point
            GPA = selectedCourse()
            print(f'\nYour scores is: {stud_score}\nYour Grade: {Students_Score()}\nYour GPA is: {GPA}\n')

else:
    print('Error___________End.')