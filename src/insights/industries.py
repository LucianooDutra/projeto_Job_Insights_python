from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_data = read(path)
    result = set()

    for item in list_data:
        if item["industry"] != "" and item["industry"] not in result:
            result.add(item["industry"])

    return result


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = []

    for job in jobs:
        if job["industry"] != "" and job["industry"] == industry:
            result.append(job)

    return result
