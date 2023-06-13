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

# Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів

    def check_salary(self, days):
        workdays = self._get_workdays()
        salary = workdays * self.salary
        return salary

# ** Зробити можливим, щоб метод check_salary рахував ЗП з початку місяця до \n
# поточного дня, не враховуючи вихідні дні.
    def _get_workdays(self):
        import datetime

        today = datetime.date.today()
        start_of_month = datetime.date(today.year, today.month, 1)

        workdays = 0
        current_day = start_of_month
        while current_day <= today:
            if current_day.weekday() < 5:  # 5 робочіх днів
                workdays += 1
            current_day += datetime.timedelta(days=1)

        return workdays

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
    def __init__(self, name, salary, job_title, tech_stack):
        self.name = name
        self.salary = salary
        self.job_title = job_title
        self.tech_stack = tech_stack
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
# Для класу Developer зробити порівняння за кількістю технологій

def eq(self, other):
    return len(self.tech_stack) == len(other.tech_stack)

# Зробити можливим операцію додавання об’єктів класу Developer. \n
# Результатом має бути новий об’єкт, в якому name = name1 + ‘ ’ + name2, \n
# a tech_stack - список з технологій двох об’єктів (тільки унікальні значення), ЗП - більша з двох

def add(self, other):
    name = self.name + " " + other.name
    tech_stack = list(set(self.tech_stack + other.tech_stack))
    salary = max(self.salary, other.salary)
    return Developer(name, salary, tech_stack)


Recruiter = Employee('Jake', 5, Recruiter)
print(Recruiter)
print('I come to the office and start to hiring')

Developer = Employee('Tom', 6, Developer)
print(Developer)
print('I come to the office and start to coding')