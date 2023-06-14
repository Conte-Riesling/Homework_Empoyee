# Створити клас Candidate
# В init передавати first name, last name, email, tech_stack, main_skill, main_skill_grade
class Candidate:
    def __init__(
            self,
            first_name,
            last_name,
            email,
            tech_stek,
            main_skill,
            main_skill_grade
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stek = tech_stek
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    # Створити @property метод який повертає first name + ‘ ‘ + last name
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

candidate1 = Candidate('Jake', 'Jobson', 'dsa@mail.com', 'Phyton', 'Django', 'Django_grade')
print(candidate1.full_name)

# Створити @classmethod generate_candidates, який приймає в якості аргументу шлях до файлу
# Метод generate_candidates має повертати список об’єктів класу Candidate
# ** Розширити метод generate_candidates, щоб він міг отримувати в якості аргументу URL \n
# на файл та генерувати кандидатів з нього

@classmethod
def generate_candidates(cls, file_path):
    candidates = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            candidate_data = line.strip().split(',')
            first_name = candidate_data[0]

            last_name = candidate_data[1]
            email = candidate_data[2]
            tech_stack = candidate_data[3]
            main_skill = candidate_data[4]
            main_skill_grade = candidate_data[5]
            candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
            candidates.append(candidate)

        return candidates
