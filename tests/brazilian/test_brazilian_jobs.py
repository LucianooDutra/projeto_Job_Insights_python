from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"

    exemple_result = {"title", "salary", "type"}

    data = read_brazilian_file(path)
    result = data[0].keys()

    keys = set()

    for item in result:
        keys.add(item)

    assert keys == exemple_result
