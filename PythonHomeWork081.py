# Задача 38
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import csv


with open("contact.csv", newline = '', encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['иванов'])

# with open("contact.csv", 'w', newline = '', encoding = 'utf-8') as csvfile:
#     writer = csv.writer(csvfile, delimiter = ',')
#     writer.writerow(["иванов", "row 1 el 2", "row 1 el 3"])
#     writer.writerow(["row 2 el 1", "row 2 el 2", "row 2 el 3"])
#     writer.writerow(["row 3 el 1", "row 3 el 2", "row 3 el 3"])

# Ввод данных
# def ask_user():
#     last_name = input('Введите фамилию: ')
#     first_name = input('Введите имя: ')
#     phone_number = int(input('Введите номер телефона: '))
#     return last_name, first_name, phone_number


# def text_save():
#     with open('Contact.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerows(writer)


# def read_file():
#     with open('Contact.csv', 'w', newline='') as csvfile:
#         fieldnames = ['фамилия', 'имя', 'телефон']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()


# if __name__ == '__main__':
#     data = ask_user()
#     print(data)
#     contact_user = 'Contact.csv'
#     text_save(data, contact_user)    
#     print(contact_user)