# Створити клас Employee. __init__ має приймати наступні аргументи: ім’я, ЗП за один робочий день.
class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def salary_day(self, new_day):
        x = new_day
        if salary.day == salary:
            return new_day
        else:
            return new_day[0] + 1

# Створити метод work(self, …) який повертає строку “I come to the office.”

    def get_work(self, default):
        return 'I come to the office'

# Створити класи Recruiter та Developer, які наслідують клас Employee.
class Recruiter(Employee):
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title
        print(recruiter.name, recruiter.salary, recruiter.job_title)

# Перевизначити методи work в класах R та D, щоб вони повертали значення:
# “I come to the office and start to hiring.” - для Recruiter

def get_work(self, default):
    return 'I come to the office and start to hiring'
class Developer(Employee):
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title
        print(developer.name, developer.salary, developer.job_title)

# Перевизначити методи work в класах R та D, щоб вони повертали значення:
# “I come to the office and start to coding.” - для Developer

def get_work(self, default):
    return 'I come to the office and start to coding'

# Перевизначити методи __str__, щоб они повертали строку: “Посада: Ім’я”
def __str__(self):
    return f"job_title: {self.job_title}, name: {self.name}"

# Зробити можливим порівнювати Employee по рівню ЗП.

def __gt__(self, new):
    if sum(new, Employee):
        return self.salary > new.salary
    return False

def __it__(self, new):
    if sum(new, Employee):
        return self.salary < new.salary
    return False

def __ge__(self, new):
    if sum(new, Employee):
        return self.salary >= new.salary
    return False

def __le__(self, new):
    if sum(new, Employee):
        return self.salary <+ new.salary
    return False

Recruiter = Employee('Jake', 5, Recruiter)
print(Recruiter)
print('I come to the office and start to hiring')

Developer = Employee('Tom', 6, Developer)
print(Developer)
print('I come to the office and start to coding')