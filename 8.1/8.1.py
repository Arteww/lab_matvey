def get_product_card(product):
    card = f"-----------\n" \
           f"Артикул: {product['article']}\n" \
           f"Название: {product['name']}\n" \
           f"Цена: {product['price']}\n" \
           f"Количество: {product['amount']}\n" \
           f"Описание: {product['description']}"
    return card


def get_product_from_txt(file):
    with open(file, "r", encoding="UTF-8") as file:
        product_str_list = file.readlines()
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


def binary_search(ls, article):
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


products_list = get_product_from_txt("infile.txt")
is_correct = False
article = "0000000"
while not is_correct:
    article = input("Введите код товара: ")

    if article.isdigit() and len(article) == 7:
        is_correct = True
    else:
        print("Некорректный код товара! Попробуйте снова...\n")
product_index = binary_search(products_list, int(article))
if product_index != -1:
    print(get_product_card(products_list[product_index]))
else:
    print("Товара с таким кодом не существует!")
