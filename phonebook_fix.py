from pprint import pprint
import csv
import codecs
import re

with codecs.open("phonebook_raw.csv", "r", "utf_8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
fio1 = re.sub(r"\'(\b[A-Я]\w+\b)\s(\b[A-Я]\w+\b)\s(\b[A-Я]\w+\b)\'\,\ \'\'\,\ \'\'\,", r"'\1', '\2', '\3',",
       str(contacts_list))
fio2 = re.sub(r"\'(\b[A-Я]\w+\b)\'\,\s\'(\b[A-Я]\w+\b)\s(\b[A-Я]\w+\b)\'\,\ \'\'\,", r"'\1', '\2', '\3',", fio1)
phone1 = re.sub(r"\+(\d)\s(\(\d{3}\))\s(\d{3}\-\d{2}\-\d{2})", r"+\1\2\3", fio2)
phone2 = re.sub(r"\+7(\d{3})(\d{3})(\d{2})(\d{2})", r"+7(\1)\2-\3-\4", phone1)
phone3 = re.sub(r"8\s(\d{3})\-(\d{3})\-(\d{2})(\d{2})", r"+7(\1)\2-\3-\4", phone2)
phone4 = re.sub(r"8\((\d{3})\)(\d{3})\-(\d{2})\-(\d{2})", r"+7(\1)\2-\3-\4", phone3)
phone5 = re.sub(r"(\+\d\(\d{3}\)\w+\-\w+\-\w+)\s\((\w+\.)\s(\d+)\)", r"\1 \2\3", phone4)
phone6 = re.sub(r"(\+\d\(\d{3}\)\w+\-\w+\-\w+)\s(\w+\.)\s(\d+)", r"\1 \2\3", phone5)
replace1 = re.sub(r"(\[\'Мартиняхин\'.{35})\'\'",
                  r"\1'cоветник отдела Интернет проектов Управления информационных технологий'", phone6)
delete1 = re.sub(r"\[\'Мартиняхин\'.{119}\]\,\s", '', replace1)
replace2 = re.sub(r"(\[\'Лагунцов.{68})\'\'", r"\1'Ivan.Laguntcov@minfin.ru'", delete1)
delete2 = re.sub(r"\,\s\[\'Лагунцов.{54}\]", r"", replace2)
refactor1 = re.sub(r"\[|\]|\'", r"", delete2).split(", ")

cleaned_list = []
counter = 0
listing = []
for i in refactor1:
    listing.append(i)
    counter +=1
    if counter % 7 == 0:
        cleaned_list.append(listing)
        listing = []
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(cleaned_list)