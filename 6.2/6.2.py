persons = ["actress", "colonel", "countess", "baronet", "drwatson", "maid",
           "minister", "mp", "moriarty", "narrator", "sheepdog", "stranger"]

with open('infile.txt', 'r', encoding='utf-8') as infile:
    results = infile.readlines()
    killed = results[1].replace('\n', '')
    wishes_death = results[4].replace('\n', '').split(', ')
    place = results[7].replace('\n', '')
    access = results[10].replace('\n', '').split(', ')
    alibi = results[13].replace('\n', '').split(', ')

    print(f"Убит: {killed}\n"
          f"Желали смерти: {', '.join(wishes_death)}\n"
          f"Место убийства: {place}\n"
          f"Имели доступ: {', '.join(access)}\n"
          f"Имеется алиби: {', '.join(alibi)}\n")

    for person in alibi:
        persons.remove(person)
    i = 0
    while i < len(persons):
        if persons[i] not in wishes_death:
            persons.remove(persons[i])
        elif persons[i] not in access:
            persons.remove(persons[i])
        else:
            i += 1

    if len(persons) == 0:
        print("Похоже, что мне дали неверные данные, преступником быть не может никто")
    elif len(persons) == 1:
        print(f"Преступник обнаружен! Это {persons[0]}")
    else:
        print(f"Ищите злодея среди {', '.join(persons)}")