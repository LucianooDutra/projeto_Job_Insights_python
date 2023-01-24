from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def list_jobs():
    return [
        {"min_salary": 300, "max_salary": 2000, "date_posted": "2022-01-01"},
        {"min_salary": 550, "max_salary": 3500, "date_posted": "2022-02-02"},
        {"min_salary": 250, "max_salary": 2500, "date_posted": "2022-03-03"},
        {"min_salary": 150, "max_salary": 1900, "date_posted": "2022-04-04"},
        {"min_salary": 900, "max_salary": 3600, "date_posted": "2022-05-05"},
        {"min_salary": 1500, "max_salary": 5000, "date_posted": "2022-06-06"},
    ]


@pytest.fixture
def min_salary():
    return [
        {"min_salary": 150, "max_salary": 1900, "date_posted": "2022-04-04"},
        {"min_salary": 250, "max_salary": 2500, "date_posted": "2022-03-03"},
        {"min_salary": 300, "max_salary": 2000, "date_posted": "2022-01-01"},
        {"min_salary": 550, "max_salary": 3500, "date_posted": "2022-02-02"},
        {"min_salary": 900, "max_salary": 3600, "date_posted": "2022-05-05"},
        {"min_salary": 1500, "max_salary": 5000, "date_posted": "2022-06-06"},
    ]


@pytest.fixture
def max_salary():
    return [
        {"min_salary": 1500, "max_salary": 5000, "date_posted": "2022-06-06"},
        {"min_salary": 900, "max_salary": 3600, "date_posted": "2022-05-05"},
        {"min_salary": 550, "max_salary": 3500, "date_posted": "2022-02-02"},
        {"min_salary": 250, "max_salary": 2500, "date_posted": "2022-03-03"},
        {"min_salary": 300, "max_salary": 2000, "date_posted": "2022-01-01"},
        {"min_salary": 150, "max_salary": 1900, "date_posted": "2022-04-04"},
    ]


@pytest.fixture
def data():
    return [
        {"min_salary": 1500, "max_salary": 5000, "date_posted": "2022-06-06"},
        {"min_salary": 900, "max_salary": 3600, "date_posted": "2022-05-05"},
        {"min_salary": 150, "max_salary": 1900, "date_posted": "2022-04-04"},
        {"min_salary": 250, "max_salary": 2500, "date_posted": "2022-03-03"},
        {"min_salary": 550, "max_salary": 3500, "date_posted": "2022-02-02"},
        {"min_salary": 300, "max_salary": 2000, "date_posted": "2022-01-01"},
    ]


def test_sort_by_criteria(list_jobs, min_salary, max_salary, data):

    sort_by(list_jobs, "min_salary")

    assert list_jobs == min_salary

    sort_by(list_jobs, "max_salary")

    assert list_jobs == max_salary

    sort_by(list_jobs, "date_posted")

    assert list_jobs == data
