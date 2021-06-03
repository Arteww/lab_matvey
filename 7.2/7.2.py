# Возвращает информацию о рейсе
def get_flight_info(flight: list):
    info = f"-----------\n" \
           f"Номер рейса: {flight[0]}\n" \
           f"Пункт вылета: {flight[1]}\n" \
           f"Пункт прилета: {flight[2]}\n" \
           f"Время вылета: {flight[3]}\n" \
           f"Время прилета: {flight[4]}"

    return info


# Возвращает список рейсов из текстового файла
def get_flight_from_txt(file: str) -> list:
    # Получаем список строк txt файла с рейсами
    with open(file, "r", encoding="UTF-8") as file:
        flight_str_list = file.readlines()

    # Создаем список объектов класса Flight
    flights = list()
    for flight_str in flight_str_list:
        ls = list(flight_str.split(" "))
        flights.append([int(ls[0]), ls[1], ls[2], ls[3], ls[4]])

    return flights


def main():
    flights = get_flight_from_txt("infile.txt")  # Получаем список всех рейсов

    while True:  # Пока не введен символ конца ввода
        searchable = input("\nВведите номер рейса или пункт прилёта: ")

        if searchable == "-":
            return 0

        is_find = False
        if searchable.isdigit():  # Если введен номер рейса
            for flight in flights:
                if int(searchable) == flight[0]:
                    is_find = True
                    print(get_flight_info(flight))
        else:  # Иначе, если введен пунт прилёта
            for flight in flights:
                if searchable.lower() == flight[2].lower():
                    is_find = True
                    print(get_flight_info(flight))

        if not is_find:
            print("Рейс не найден!")


if __name__ == '__main__':
    main()
