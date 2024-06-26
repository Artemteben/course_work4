from src.get_api_hh import GetApiHH

from src.saver import SaveToFormatFile


def user_interface():
    """
    Функция предоставляет интерфейс для взаимодействия
    пользователя с программой поиска и сохранения вакансий.

    Пользователю предлагается ввести поисковой запрос,
    после чего программа получает вакансии с сайта hh.
    Далее пользователь выбирает количество вакансий, которое он хочет увидеть,
    после чего программа их выводит.
    Пользователю также предлагается сохранить полученные вакансии
    в файл, очистить или открыть его для просмотра.

    :return: Нет возвращаемых значений.
    """
    user_input = input('Введите поисковой запрос: ')
    get_json = GetApiHH(user_input).get_vacancy()
    sort_list = sorted(get_json, reverse=True)
    user_input_vacancy = int(input('Введите количество вакансий: '))
    if isinstance(user_input_vacancy, int):
        for i in range(user_input_vacancy):
            print(f"{sort_list[i]}")
    else:
        user_input_vacancy = 5
        for i in range(user_input_vacancy):
            print(f"{sort_list[i]}")

    input_save = input('Хотите сохранить файл? Введите "да" или "нет"!: ')
    match input_save:
        case 'да':
            SaveToFormatFile().saver(sort_list)
            print('Файл сохранён')
        case 'нет':
            print('Файл не будет сохранён')
        case _:
            print("неверный ввод для сохранения")

    input_del = input('Хотите очистить файл? Введите "да" или "нет"!: ')
    match input_del:
        case 'да':
            SaveToFormatFile().delf()
            print('Файл чист')
        case 'нет':
            print('Файл не будет очищен')
        case _:
            print("Неверный ввод для удаления")
    input_read = input('Хотите открыть файл? Введите "да" или "нет"!: ')
    match input_read:
        case 'да':
            print('Файл открыт')
            user_input_vacancy = int(input('Введите количество вакансий: '))
            if isinstance(user_input_vacancy, int):
                for i in range(user_input_vacancy):
                    print(f"{SaveToFormatFile(sort_list).reader()[i]}")
            else:
                user_input_vacancy = 5
                for i in range(user_input_vacancy):
                    print(f"{sort_list[i]}")
        case 'нет':
            print('ок')
        case _:
            print("Досвидания!")


user_interface()
