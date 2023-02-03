months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_name = input("Введите название месяца (Англ): ").capitalize()

if month_name in months:
    index = months.index(month_name)
    days = month_days[index]
    if month_name == "February":
        print(f"Кол-во дней: {days}/{days + 1}")
    else:
        print(f"Кол-во дней: {days}")
else:
    print("Невeрное название месяца")
