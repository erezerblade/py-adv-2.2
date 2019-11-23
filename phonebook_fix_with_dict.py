from pprint import pprint
import csv
import codecs
import re

with codecs.open("phonebook_raw.csv", "r", "utf_8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

contacts_dict = {}
counter = 1
for name in contacts_list:
    id = counter
    full_name = f'{name[0]} {name[1]} {name[2]}'.strip(' ')
    organisation = name[3]
    position = name[4]
    phone = name[5]
    email = name[6]
    contacts_dict.update({id: {
        "fullname": full_name.split(),
        "organisation": organisation,
        "position": position,
        "phone": phone,
        "email": email
    }})
    counter += 1

# замена телефонов
for fullname in contacts_dict.values():
    old_phone = fullname.get('phone')
    if re.match(r"\+(\d)\s(\(\d{3}\))\s(\d{3}\-\d{2}\-\d{2})", old_phone):
        new_phone = re.sub(r"\+(\d)\s(\(\d{3}\))\s(\d{3}\-\d{2}\-\d{2})", r"+\1\2\3", old_phone)
        fullname.update({'phone': new_phone})
    elif re.match(r"\+7(\d{3})(\d{3})(\d{2})(\d{2})", old_phone):
        new_phone = re.sub(r"\+7(\d{3})(\d{3})(\d{2})(\d{2})", r"+7(\1)\2-\3-\4", old_phone)
        fullname.update({'phone': new_phone})
    elif re.match(r"8\s(\d{3})\-(\d{3})\-(\d{2})(\d{2})", old_phone):
        new_phone = re.sub(r"8\s(\d{3})\-(\d{3})\-(\d{2})(\d{2})", r"+7(\1)\2-\3-\4", old_phone)
        fullname.update({'phone': new_phone})
    elif re.match(r"8\((\d{3})\)(\d{3})\-(\d{2})\-(\d{2})", old_phone):
        new_phone = re.sub(r"8\((\d{3})\)(\d{3})\-(\d{2})\-(\d{2})", r"+7(\1)\2-\3-\4", old_phone)
        fullname.update({'phone': new_phone})
    elif re.match(r"(\+\d\(\d{3}\)\w+\-\w+\-\w+)\s\((\w+\.)\s(\d+)\)", old_phone):
        new_phone = re.sub(r"(\+\d\(\d{3}\)\w+\-\w+\-\w+)\s\((\w+\.)\s(\d+)\)", r"\1 \2\3", old_phone)
        fullname.update({'phone': new_phone})
    elif re.match(r"(\+\d\(\d{3}\)\w+\-\w+\-\w+)\s(\w+\.)\s(\d+)", old_phone):
        new_phone = re.sub(r"(\+\d\(\d{3}\)\w+\-\w+\-\w+)\s(\w+\.)\s(\d+)", r"\1 \2\3", old_phone)
        fullname.update({'phone': new_phone})


# удаление дублей
for people in contacts_dict.values():
    name = ' '.join(people.get('fullname'))
    if re.match(r'Мартиняхин', name):
        people.update({'position': 'cоветник отдела Интернет проектов Управления информационных технологий'})
    elif re.match(r'Лагунцов', name):
        people.update({'email': 'Ivan.Laguntcov@minfin.ru'})
contacts_dict.pop(5)
contacts_dict.pop(9)


# конвертация словаря в список строк
list_of_lists = []
for man in contacts_dict.values():
    list = [
        man.get('fullname')[0],
        man.get('fullname')[1],
        man.get('fullname')[2],
        man.get('organisation'),
        man.get('position'),
        man.get('phone'),
        man.get('email')
        ]
    list_of_lists.append(list)


# создание файла
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(list_of_lists)





