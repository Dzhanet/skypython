import json
import functions


def main():
    """запуск программы"""

    print("Введите номер студента:")
    number_input = int(input())
    student = functions.get_student_by_pk(number_input)

    if student is None:
        print("Студент не найден")
        return

    name_student = student["full_name"]
    student_skill = student["skills"]

    print(f"Студент - {name_student}")
    print(f"Знает - {student_skill}")

    print("Введите название профессии")
    profession_input = input()
    profession = functions.get_profession_by_title(profession_input)

    if profession is None:
        print("Профессия не найдена")
        return

    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    coincidence = functions.check_fitness(student_skills, profession_skills)

    has = coincidence["has"]
    lucks = coincidence["lucks"]
    percent_fit = coincidence["percent_fit"]

    print (f"Пригодность {percent_fit}%")
    print(f"Студент знает: {has}")
    print(f"Студент не знает: {lucks}")

main()
