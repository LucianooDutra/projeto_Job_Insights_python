from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        group_by_department = []
        for row in reader:
            group_by_department.append(row)
        return group_by_department


def get_unique_job_types(path: str) -> List[str]:
    list_data = read(path)
    result = set()
    for item in list_data:
        if item["job_type"] != "":
            result.add(item["job_type"])
    return result


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    result = []

    for job in jobs:
        if job["job_type"] != "" and job["job_type"] == job_type:
            result.append(job)

    return result
