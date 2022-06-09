import datetime
import time
import people
import salary


CreatData = datetime.datetime.today().strftime("%d-%m-%y")
CreatTime = time.strftime("%H.%M.%S")

print(f'Local Date: {CreatData}*{CreatTime} ')



if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()