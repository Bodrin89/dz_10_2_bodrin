import json
from candidates import Candidates


def load_candidates(file_name):
    """функция которая загрузит данные из файла"""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all(all_candidates):
    """Функция которая покажет всех кандидатов"""
    array = []
    for item in all_candidates:
        candidate = Candidates(item['pk'], item['name'], item['picture'], item['position'], item['gender'],
                               item['age'], item['skills'].lower())
        array.append(candidate)
    return array


def get_by_pk(pk, data):
    """Функция которая вернет кандидата по pk"""
    for item in data:
        if item.pk == pk:
            return item


def get_by_skill(skill_name, data):
    """Функция которая вернет кандидатов по навыку"""
    arr = []
    for item in data:
        if skill_name in (item.skills).split(','):
            arr.append(item)
    return arr
