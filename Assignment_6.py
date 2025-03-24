from datetime import datetime


data = [
    {"name": "Nugraha", "birthdate": "1989-09-13"},
    {"name": "John", "birthdate": "1990-01-01"},
    {"name": "Jane", "birthdate": "1992-02-02"},
    {"name": "Doe", "birthdate": "1994-03-03"}
]


def calculate_age(birthdate):
    birth_year = int(birthdate.split("-")[0])
    current_year = datetime.now().year
    return current_year - birth_year


print(f"{'Number':<8}{'Name':<10}{'Age':<5}")
print("=" * 25)

for index, person in enumerate(data, start=1):
    age = calculate_age(person["birthdate"])
    print(f"{index:<8}{person['name']:<10}{age:<5}")
