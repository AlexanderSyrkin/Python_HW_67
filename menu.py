import function

def start_menu():
    print("1 - Все контакты.")
    print("2 - Найти контакт.")
    print("3 - Добавить контакт.")
    print("4 - Импорт контактов.")
    print("5 - Экспорт контактов.")
    choice = int(input("Выберете действие: "))
    print("---------------------------------------")


    if choice == 1:
        function.read()

    elif choice == 2:
        data_request = str(input("Введите данные: ")).title()
        function.find_contact(data_request)

    elif choice == 3:
        family = input("Введите фамилию: ")
        name = input("Введите имя: ")
        number = input("Введите номер: ")
        description = input("Введите описание: ")
        function.create_contact(family, name, number, description)

    elif choice == 4:
        filename = input("Введите название файла csv: ")
        function.import_contacts(filename)

    elif choice == 5:
        expt = input("Введите названия файла для экспорта данных: ")
        function.export_contact(expt)