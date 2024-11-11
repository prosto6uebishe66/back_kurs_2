from src.class_vacansies import Vacansy

def create_list_obj(list_obj):
    """

    :param list_obj: данные для создания класс
    :return: list_vac: список объектов класса
    """
    list_vac = []
    for item in list_obj:
        list_vac.append(
            Vacansy(item.get('name'),
                    item.get('area', {}).get('name'),
                    item.get('salary').get('from') if item["salary"] is not None else 0,
                    item.get('salary').get('to') if item["salary"] is not None else 0,
                    item.get('snippet', {}).get('requirement'),
                    item.get('apply_alternate_url'),
                    )
                            )
    return list_vac

def sort_salary_from(vacs_list, user_sorting_number):


    if user_sorting_number == 1:

        print('Выбрано: сортировка по возрастанию зарплаты')

    if user_sorting_number == 2:

        print('Выюроано: сортировка по убыванию зарплаты')

    if user_sorting_number ==3:

        print('Выбрано: сортировка списка вакансий')

    return  vacs_list