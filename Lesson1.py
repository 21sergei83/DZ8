# Создаем пустой словарь для хранения данных
phonebook = {}

# Функция для добавления новой записи в справочник
def add_contact(name, phone):
    phonebook[name] = phone
    print(f"Контакт {name} успешно добавлен в справочник")

# Функция для изменения данных контакта
def edit_contact(name):
    if name in phonebook:
        new_phone = input("Введите новый номер телефона: ")
        phonebook[name] = new_phone
        print(f"Данные контакта {name} успешно изменены")
    else:
        print(f"Контакт {name} не найден в справочнике")

# Функция для удаления контакта из справочника
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} успешно удален из справочника")
    else:
        print(f"Контакт {name} не найден в справочнике")

# Добавляем несколько контактов в справочник
add_contact("Иванов", "123-45-67")
add_contact("Петров", "987-65-43")
add_contact("Сидоров", "555-55-55")

# Изменяем данные контакта
edit_contact("Иванов")

# Удаляем контакт из справочника
delete_contact("Петров")

# Выводим содержимое справочника
print(phonebook)