def get_flight_info(flight: list):
    info = f"Номер рейса: {flight[0]}\n" \
           f"Пункт вылета: {flight[1]}\n" \
           f"Пункт прилета: {flight[2]}\n" \
           f"Время вылета: {flight[3]}\n" \
           f"Время прилета: {flight[4]}"
    return info


def get_flight_from_txt(file):
    with open(file, "r", encoding="UTF-8") as file:
        flight_str_list = file.readlines()
    flights = list()
    for flight_str in flight_str_list:
        ls = list(flight_str.split(" "))
        flights.append([int(ls[0]), ls[1], ls[2], ls[3], ls[4]])
    return flights


flights = get_flight_from_txt("infile.txt")

while True:
    searchable = input("\nВведите номер рейса или пункт прилёта: ")

    if searchable == "-":
        break

    is_find = False
    if searchable.isdigit():
        for flight in flights:
            if int(searchable) == flight[0]:
                is_find = True
                print(get_flight_info(flight))
    else:
        for flight in flights:
            if searchable.lower() == flight[2].lower():
                is_find = True
                print(get_flight_info(flight))

    if not is_find:
        print("Рейс не найден!")
