import json

from back_kurs_2.Config import NEW_VACANCIES_PATH
from src.class_hh import HeadHunter
from src.class_json import JSONSaver
from src.function import create_list_obj, sort_salary_from


def clear_file(file_path):
    """Функция удаляет содержимое файла перед записью новой информации."""
    try:
        with open(file_path, 'w+') as file:
            file.truncate(0)
        print(f"Файл {file_path} был успешно очищен.")
    except Exception as e:
        print(f"Произошла ошибка при очистке файла: {e}")


def user_interaction():
    """
    программа приветствует пользователя
    user_vacancy  помогает ему с поиском вакансии
    user_sorting_number сортирует вакансии для вывода
    user_top_number помогает вывести топ вакансий
    chose_another_vac предлагает выбрать другую вакансию
    или завершить программу
     """
    print("Здравствуйте! Я Ваш личный помошник в поиске интересующей Вас работы")
    user_vacancy = input("Введите интересующие Вас вакнсию: ").lower().strip()
    hh = HeadHunter()
    vacancy_from_hh = hh.get_vacansies(user_vacancy)
    saving_vac = JSONSaver(NEW_VACANCIES_PATH)
    saving_vac.write_data(vacancy_from_hh)
    user_sorting_number = int(input("Наберите номер для сортировки списка вакансий:\n"
                                    "1 - по возрастанию зарплаты\n"
                                    "2 - по убыванию зарплаты\n"
                                    "3 - без сортировки\n"))

    vacs_list = create_list_obj(vacancy_from_hh)

    sorted_vacs = sort_salary_from(vacs_list, user_sorting_number)

    user_top_number = int(input('Выберите топ-список вакансий для вывода на экран, для этого'
                                'введите соответсвующую цифру:\n'
                                '1 - топ 5 вакансий\n'
                                '2- топ 10 вакансий\n'
                                '3- топ 15 вакансий\n'
                                '4- показать все вакансии\n'))

    if user_top_number == 1:
        for vac in sorted_vacs[:5]:
            print(vac)
    elif user_top_number == 2:
        for vac in sorted_vacs[:10]:
            print(vac)
    elif user_top_number == 3:
        for vac in sorted_vacs[:15]:
            print(vac)
    elif user_top_number == 4:
        for vac in sorted_vacs[:20]:
            print(vac)

    chose_another_vac = input("Хотите выбрать другую вакансию?\n y/n: \n").lower().strip()
    if chose_another_vac in ['y', 'yes', 'да', 'д']:

        user_interaction()
    elif chose_another_vac in ['n', 'no', 'нет', 'н']:
        print('Программа завершена. \n Желаем удачи!')
        exit()


if __name__ == "__main__":
    user_interaction()
