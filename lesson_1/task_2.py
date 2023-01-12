time_in_sec = int(input("Введите время в секундах: "))
sec = time_in_sec % (24 * 3600)
hour = sec // 3600
sec %= 3600
minute = sec // 60
sec %= 60

print(f"{hour}:{minute}:{sec}")