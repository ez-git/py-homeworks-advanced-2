from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from graphs import get_graph


def get_time():
    print(datetime.now())


if __name__ == '__main__':
    calculate_salary()
    get_employees()

get_time()
get_graph()
