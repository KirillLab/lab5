# -*- coding: utf-8 -*-
import csv
import os.path

def list_from_file(path_directory):
    """
    Получение данных csv-файла по заданному пути и создание словаря по данным.
    :param path_directory:string
    :return: {}
    """
    b = []
    with open(path_directory + '/data.csv') as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            b.append(row)
    return b


def output_in_file(data, path_directory):
    """
    Вывод в файл CSV.
    :param path_directory:string
    :param data:{}
    """
    with open(path_directory + "/data.csv", 'w') as f:
        writer = csv.DictWriter(f, delimiter=';', lineterminator='\n', fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def print_data(data):
    """
    Форматированный вывод данных.
    :param data:{}
    """
    print()
    for i in data[0].keys():
        print("{:15s}".format(i), end=" ")
    print()
    for row in data:
        for x in row.values():
            print("{:15s}".format(x), end=" ")
        print()
    print()


def count_files(path_directory):
    """
    Вывод количества файлов в папке по заданному пути.
    :param path_directory:string
    """
    num_files = len([f for f in os.listdir(path_directory) if os.path.isfile(os.path.join(path_directory, f))])
    print("Количество файлов в директории", path_directory, ":", num_files)


def sort_key(dictionary, name):
    """
    Сортировка по ключу.
    :param dictionary:{}
    :param name:string
    """
    if name == "date" or name == "p":
        dictionary.sort(key=lambda f: f[name])
    else:
        dictionary.sort(key=lambda f: int(f[name]))
    print_data(dictionary)


def number_sort(dictionary):
    """
    Выводит выборку данных, где number < 500.
    :param dictionary:[]
    :return:
    """
    print("Данные, где number < 200:")
    for j in dictionary[0].keys():
        print("{:15s}".format(j), end=" ")
    print()
    for i in dictionary:
        if int(i['id']) < 200:
            for x in i.values():
                print("{:15s}".format(x), end=" ")
            print()


def input_data(dictionary):
    """
    Ввод новых данных. Добавляет одну новую строку.
    :param dictionary:[]
    :return: []
    """
    print("Введите новые данные через ;, всего 4 данных: №, марка машины, "
          "номер машины, дата (в формате ДД.ММ.ГГ) и ""время (в формате ЧЧ:ММ)")
    input_string = input()
    input_string.replace(' ', '')
    input_string = input_string.split(";")
    dictionary_2 = {"id": input_string[0],
                    "date": input_string[1],
                    "pr": input_string[2],
                    "p": input_string[3]}

    dictionary.append(dictionary_2)
    return dictionary


path = "C:\\Users\kkiir\Desktop/3lab"
count_files(path)
dictionary = list_from_file(path)

print("Исходные данные:")
print_data(dictionary)

print("Сортировка данных по ключу. Введите ключ:")
sort_key(dictionary, input())
number_sort(dictionary)
dictionary = input_data(dictionary)
output_in_file(dictionary, path)
