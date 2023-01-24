from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    list_data = read(path)
    result = []

    for item in list_data:
        if item["max_salary"] != "" and not item["max_salary"].isalpha():
            result.append(int(item["max_salary"]))

    return max(result)


def get_min_salary(path: str) -> int:
    list_data = read(path)
    result = []

    for item in list_data:
        if item["min_salary"] != "" and not item["min_salary"].isalpha():
            result.append(int(item["min_salary"]))

    return min(result)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("valor mínimo ou máximo não existe")

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if (
        (not str(min_salary).isnumeric())
        or (not str(max_salary).isnumeric())
        or (type(salary) is not int and type(salary) is not str)
    ):
        raise ValueError("Os valores não são do type int")
    elif int(min_salary) > int(max_salary):
        raise ValueError("O valor mínimo é maior do que o valor máximo")
    else:
        return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    lista_de_trabalhos = []

    for job in jobs:
        try:
            values = matches_salary_range(job, salary)
            if values:
                lista_de_trabalhos.append(job)
        except ValueError:
            pass
            # raise ValueError("deu ruim")

    return lista_de_trabalhos
