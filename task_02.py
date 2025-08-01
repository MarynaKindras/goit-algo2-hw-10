from colorama import Fore, Style, init

# Initialize colorama for colored console output
init(autoreset=True)

class Teacher:
    """
    A class to represent a teacher with their personal details and subjects they can teach.

    Attributes:
        first_name (str): The first name of the teacher.
        last_name (str): The last name of the teacher.
        age (int): The age of the teacher.
        email (str): The email address of the teacher.
        can_teach_subjects (set): A set of subjects the teacher can teach.
        assigned_subjects (set): A set of subjects assigned to the teacher.
    """

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        """
        Initializes a Teacher instance.

        Args:
            first_name (str): The first name of the teacher.
            last_name (str): The last name of the teacher.
            age (int): The age of the teacher.
            email (str): The email address of the teacher.
            can_teach_subjects (set): A set of subjects the teacher can teach.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        """
        Returns a string representation of the Teacher instance.

        Returns:
            str: A string representation of the teacher.
        """
        return f"{self.first_name} {self.last_name}"

def create_schedule(subjects, teachers):
    """
    Creates a schedule by assigning teachers to subjects using a greedy algorithm.

    Args:
        subjects (set): A set of subjects to be covered.
        teachers (list): A list of Teacher instances.

    Returns:
        list: A list of Teacher instances with assigned subjects, or None if not all subjects can be covered.
    """
    covered_subjects = set()
    schedule = []

    while subjects - covered_subjects:
        # Find the teacher who can cover the most uncovered subjects
        best_teacher = None
        max_covered = 0

        for teacher in teachers:
            if teacher not in schedule:
                # Calculate the number of uncovered subjects this teacher can cover
                can_cover = teacher.can_teach_subjects & (subjects - covered_subjects)
                if len(can_cover) > max_covered or (len(can_cover) == max_covered and teacher.age < best_teacher.age):
                    best_teacher = teacher
                    max_covered = len(can_cover)

        if not best_teacher:
            # No teacher can cover the remaining subjects
            return None

        # Assign the subjects to the best teacher
        best_teacher.assigned_subjects = best_teacher.can_teach_subjects & (subjects - covered_subjects)
        covered_subjects.update(best_teacher.assigned_subjects)
        schedule.append(best_teacher)

    return schedule

if __name__ == '__main__':
    # Set of subjects
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # List of teachers
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    # Create the schedule
    schedule = create_schedule(subjects, teachers)

    # Print the schedule
    if schedule:
        print(f"{Fore.GREEN}Розклад занять:")
        for teacher in schedule:
            print(f"{Fore.BLUE}{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"{Fore.YELLOW} Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print(f"{Fore.RED}Неможливо покрити всі предмети наявними викладачами.")