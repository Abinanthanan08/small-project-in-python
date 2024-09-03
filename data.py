from datetime import datetime
def valid_date(date):

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False

print(valid_date("2024-03-03"))
print(valid_date("2024-02-31"))
print(valid_date("2024-03-23 10:30"))

