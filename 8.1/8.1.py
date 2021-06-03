# Возвращает всю информация о товаре
def get_product_card(product: dict):
    card = f"-----------\n" \
           f"Артикул: {product['article']}\n" \
           f"Название: {product['name']}\n" \
           f"Цена: {product['price']}\n" \
           f"Количество: {product['amount']}\n" \
           f"Описание: {product['description']}"

    return card


# Возвращает список товаров из текстового файла
def get_product_from_txt(file: str) -> list:
    # Получаем список строк txt файла с товарами
    with open(file, "r", encoding="UTF-8") as file:
        product_str_list = file.readlines()

    # Создаем список объектов класса Product
    products = list()
    for product_str in product_str_list:
        ls = list(product_str.split(" "))
        products.append({
            "article": ls[0],
            "name": ls[1].replace("_", " "),
            "price": ls[2],
            "amount": ls[3],
            "description": ls[4].replace("_", " ")
        })

    return products


# Бинарный поиск: возвращает индекс искомого элемента
def binary_search(ls: list, article: int) -> int:
    first = 0
    last = len(ls) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last) // 2
        if int(ls[mid]['article']) == article:
            index = mid
        else:
            if article < int(ls[mid]['article']):
                last = mid - 1
            else:
                first = mid + 1
    return index


def main():
    products_list = get_product_from_txt("infile.txt")   # Получаем список товаров

    is_correct = False
    article = "0000000"
    while not is_correct:  # Пока код товара не введен в верном формате
        article = input("Введите код товара: ")

        if article.isdigit() and len(article) == 7:
            is_correct = True
        else:
            print("Некорректный код товара! Попробуйте снова...\n")

    product_index = binary_search(products_list, int(article))  # Получаем индекс товара в списке

    if product_index != -1:
        print(get_product_card(products_list[product_index]))
    else:
        print("Товара с таким кодом не существует!")


if __name__ == '__main__':
    main()
