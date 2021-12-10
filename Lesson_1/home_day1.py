time_sec = int(input("Введите в секундах:"))
one_min = 60
one_hour = 3600
one_day = 86400
# до минуты
if time_sec <= one_min:
    print(time_sec, "сек")
# до часа
elif one_min <= time_sec < one_hour:
    my_min = time_sec // one_min
    my_sec = time_sec % one_min
    print(my_min, "мин", my_sec, "сек")
# до суток
elif one_hour <= time_sec < one_day:
    my_hour = time_sec // one_hour
    time_sec = time_sec % one_hour
    my_min = time_sec // one_min
    my_sec = time_sec % one_min
    print(my_hour, "час", my_min, "мин", my_sec, "сек")
# больше суток
elif one_day <= time_sec:
    my_day = time_sec // one_day
    time_sec = time_sec % one_day
    my_hour = time_sec // one_hour
    time_sec = time_sec % one_hour
    my_min = time_sec // one_min
    my_sec = time_sec % one_min
    print(my_day, "дн", my_hour, "час", my_min, "мин", my_sec, "сек")
