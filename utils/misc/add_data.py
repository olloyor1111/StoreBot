
import psycopg2
from data import config

categories = [
    {
        "name": "💻 Noutbuklar"  #1
    },
    {
        "name": "💻 Macbooklasr" #2
    },
    {
        "name": "⌨️ Kampyuter aksessuarlari"  #3
    },
    {
        "name": "🖥 Monitorlar"  #4
    },
    {
        "name": "Lenova",  #5
        "parent_id": 1
    },
    {
        "name": "Asus",  #6
        "parent_id": 1
    },
    {
        "name": "Acer",   #7
        "parent_id": 1
    },
    {
        "name": "hp",   #8
        "parent_id": 1
    },
    {
        "name": "MacBook Pro 13 M1",  #9
        "parent_id": 2
    },
    {
        "name": "Apple MacBook Air 13 M2",  #10
        "parent_id": 2
    },
    {
        "name": "Klaviatura", #11
        "parent_id": 3
    },
    {
        "name": "Naushnik",  #12
        "parent_id": 3
    },
    {
        "name": "Sichqoncha",  #13
        "parent_id": 3
    },
    {
        "name": "Printerlar",  #14
        "parent_id": 3
    },
    {
        "name": "Artel PRO3000 27CD IPS 75Hz",  #15
        "parent_id": 4
    },
    {
        "name": " Dahua LCD DHI-LM27-A200",  #16
        "parent_id": 4
    },
    {
        "name": "Монитор Mi 23.8",  #17
        "parent_id": 4
    },
    {
        "name": "Lenovo IdeaPad 3 ",  # 18
        "parent_id": 5
    },
    {
        "name": "Lenovo V15 G2ITL",  # 19
        "parent_id": 5
    },
    {
        "name": "Lenovo ThinkBook 15",  # 20
        "parent_id": 5
    },
    {
        "name": "Lenovo IdeaPad Pro 14ACN6 ",  # 21
        "parent_id": 5
    },
    {
        "name": "ASUS VivoBook 90NB10J2-M00BT0/X1504VA-BQ286",  # 22
        "parent_id": 6
    },
    {
        "name": "ASUS VivoBook 90NB10R2-M006F0/M1605YA-MB161",  # 23
        "parent_id": 6
    },
    {
        "name": "Acer Aspire 7 A715",  # 24
        "parent_id": 7
    },
    {
        "name": "Acer E15 ",  # 25
        "parent_id": 7
    },
    {
        "name": "Acer Aspire 3",  # 26
        "parent_id": 7
    },
    {
        "name": "HP Langkawi 15s",  # 27
        "parent_id": 8
    },
    {
        "name": "Ноутбук HP 250 G8 ",  # 28
        "parent_id": 8
    },
    {
        "name": "Printer oq-qora",  # 29
        "parent_id": 14
    },
    {
        "name": "Printer rangli",  # 30
        "parent_id": 14
    },
]

def add_category(name, parent_id=None):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                    password=config.DB_PASS,
                                    host=config.DB_HOST,
                                    port="5432",
                                    database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Categories (name, parent_id) VALUES (%s,%s)"""
        record_to_insert = (name, parent_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Categories table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Categories table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def add_category_to_db():
    for category in categories:
        add_category(name=category.get("name"), parent_id=category.get("parent_id"))


products = [
    {
        "name": " Lenovo IdeaPad 3 15IAU7 82RK00KYR",
        "description": "Бренд - Lenovo\nЧастота обновления экрана - 60 Гц\nТип процессораi3-1215U\nДиагональ экрана - 15.6\nUHD Graphics ",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1014/101475/179610/cdef156d-336a-4a85-bcf6-44e043fa142a.jpg",
        "price": 6700000,
        "category_id": 18
    },
    {
        "name": "Ноутбук Lenovo V15 G2ITL 82KB00MMRU",
        "description": "Бренд - Lenovo\nЧастота обновления экрана - 60 Гц\nТип процессора - i3-1115G4\nДиагональ экрана - 15.6\nГрафический контроллер - Intel HD Graphics",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1012/101259/179024/79fe8927-3781-468b-920f-4e823384c4b2.jpg",
        "price": 7749000,
        "category_id": 19
    },
    {
        "name": "Lenovo ThinkBook 15 G2ITL 20VE00G4RU",
        "description": "Бренд - Lenovo\nРазрешение экрана - 1920x1080\nТип процессора - i3-1115G4\nДиагональ экрана - 15.6\nГрафический контроллер - Iris Xe Graphics",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1014/101475/179610/cdef156d-336a-4a85-bcf6-44e043fa142a.jpg",
        "price": 7749000,
        "category_id": 20
    },
    {
        "name": "Lenovo IdeaPad Pro 14ACN6 82L700NDRK",
        "description": "Бренд - Lenovo\nРазрешение экрана - 2880x1800\nТип процессора - Ryzen 5 5600U\nДиагональ экрана - 14\nГрафический контроллер - GeForce MX130",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1014/101475/179610/cdef156d-336a-4a85-bcf6-44e043fa142a.jpg",
        "price": 16999000,
        "category_id": 21
    },
    {
        "name": "Ноутбук ASUS VivoBook 90NB10J2-M00BT0/X1504VA-BQ286",
        "description": "Бренд - ASUS\nРазрешение экрана - 1920x1080 (HD)\nТип процессора - Intel Core i5\nДиагональ экрана - 15.6",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/3560/356061/191285/6937110e-59c5-47cb-9941-cbe6ec1dc9c8.webp",
        "price": 9172000,
        "category_id": 22
    },
    {
        "name": "Ноутбук ASUS VivoBook 90NB10J2-M00BT0/X1504VA-BQ286",
        "description": "Бренд - ASUS\nТип процессора - AMD Ryzen 5 5500U\nДиагональ экрана - 16\nГрафический контроллер - AMD Radeon Graphics\nЧастота обновления экрана - 60 Гц",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/3560/356061/191285/6937110e-59c5-47cb-9941-cbe6ec1dc9c8.webp",
        "price": 9820000,
        "category_id": 23
    },
    {
        "name": "Ноутбук Acer Aspire 7 A715",
        "description": "Бренд - Acer\nТип процессора - AMD Ryzen 7\nДиагональ экрана - 16\nГрафический контроллер - GeForce® GTX 1650\nЧастота обновления экрана - 60 Гц",
        "image_url": "https://images.uzum.uz/ck1dghcvutvccfo27ng0/original.jpg",
        "price": 9500000,
        "category_id": 24
    },
    {
        "name": "Ноутбук Acer E15 EX21522-R4GF ATHLON SILVER",
        "description": "Бренд - Acer\nТип процессора - AMD Ryzen 7\nДиагональ экрана - 15.6\nГрафический контроллер - GeForce®  3050\nЧастота обновления экрана - 60 Гц",
        "image_url": "https://images.uzum.uz/ck1dghcvutvccfo27ng0/original.jpg",
        "price": 3800000,
        "category_id": 25
    },
    {
        "name": "Ноутбук Acer Aspire 3",
        "description": "Бренд - Acer\nТип процессора - Core i3-N305\nДиагональ экрана - 15.6\nЧастота обновления экрана - DDR5-4GB",
        "image_url": "https://images.uzum.uz/ck2ii94jvf2qegt3oib0/original.jpg",
        "price": 5420000,
        "category_id": 26
    },
    {
        "name": "Ноутбук HP Langkawi 15s-fq3055ur 6F8T0EA",
        "description": "Бренд - HP\nТип процессора - Celeron N4500\nДиагональ экрана - 15.6\nГрафический контроллер - UHD Graphics\nЧастота обновления экрана - 60 Гц",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1073/107395/185459/54da9c47-5463-413e-98db-4d43b4afd26b.jpg",
        "price": 3220000,
        "category_id": 27
    },
    {
        "name": "Ноутбук HP Langkawi 15s-fq3055ur 6F8T0EA",
        "description": "Бренд - HP\nТип процессора - i3-1115G4\nДиагональ экрана - 15.6\nГрафический контроллер - Iris Xe Graphics\nЧастота обновления экрана - 60 Гц",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1073/107395/185459/54da9c47-5463-413e-98db-4d43b4afd26b.jpg",
        "price": 7160000,
        "category_id": 28
    },
    {
        "name": "Ноутбук Apple MacBook Air 13 M2 MLXW3RU/A",
        "description": "Бренд - Apple\nТип процессора - M2\nДиагональ экрана - 13.6\nГрафический контроллер - Neural Engine\nРазрешение экрана - 2560x1664",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/3547/354765/186259/a8b82a26-b51a-4c15-81d2-7e9a0d9be350.jpg",
        "price": 17560000,
        "category_id": 10
    },
    {
        "name": "Ноутбук Apple MacBook Pro 13 M1 MYD82RU/A",
        "description": "Бренд - Apple\nТип процессора - Apple M1\nДиагональ экрана - 13.3\nРабота от аккумулятора - 20 ч\nРазрешение экрана - 2560x1600",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/943/94383/171295/031088aa-bf59-4e23-890c-ceb66fbd3f4c.jpg",
        "price": 18570000,
        "category_id": 9
    },
    {
        "name": "Клавиатура 2E GAMING KG380, RGB, 68 key, Gateron, Brown Switch, BT / USB, Black",
        "description": "Доставка - 1 день, бесплатно",
        "image_url": "https://images.uzum.uz/cgv9pufg49devoaed5d0/original.jpg",
        "price": 690000,
        "category_id": 11
    },
    {
        "name": "Клавиатура 2E GAMING KG380, RGB, 68 key, Gateron, Brown Switch, BT / USB, Black",
        "description": "Доставка - 1 день, бесплатно",
        "image_url": "https://images.uzum.uz/cgp4oob57mg9720e8550/original.jpg",
        "price": 100000,
        "category_id": 13
    },
    {
        "name": "Беспроводные наушники JBL 881A, с шумоподавлением и слотом для карты Micro SD",
        "description": "Доставка - 1 день, бесплатно",
        "image_url": "https://images.uzum.uz/ci97i4r6edfostihdorg/original.jpg",
        "price": 200000,
        "category_id": 12
    },
    {
        "name": "Принтер HP 107w 4ZB78A B19",
        "description": "Тип печати - Черно-белая\nТехнология печати - Лазерная\nОбласть применения - Cвой собственный",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/1014/101482/179643/b13719f7-fb9a-4d29-846b-0cd5af8c151d.jpg",
        "price": 3018000,
        "category_id": 29
    },
    {
        "name": "Принтер Canon PIXMA G540",
        "description": "Тип печати -Цветная\nТехнология печати - Термическая струйная\nОбласть применения - Cвой собственный",
        "image_url": "https://mini-io-api.texnomart.uz/catalog/product/807/80754/155654/c7702ab2-9905-4988-8a4c-acd116033ec0.jpg",
        "price": 2400000,
        "category_id": 30
    },
    {
        "name": "Монитор Artel PRO3000 27CD IPS 75Hz, изогнутый",
        "description": "Доставка - 1 день, бесплатно",
        "image_url": "https://images.uzum.uz/ci5g6ur6edfostih16ug/original.jpg",
        "price": 2350000,
        "category_id": 15
    },
    {
        "name": "Монитор Dahua LCD DHI-LM27-A200, 27",
        "description": "Доставка - 1 день, бесплатно",
        "image_url": "https://images.uzum.uz/cheumjt6sfhndlbm25h0/original.jpg",
        "price": 2150000,
        "category_id": 16
    },
    {
        "name": "Монитор Mi 23.8'' Desktop Monitor 1C",
        "description": "Доставка - 1 день, бесплатно",
        "image_url": "https://images.uzum.uz/cjmredkjvf2ofbh8cfv0/original.jpg",
        "price": 2150000,
        "category_id": 17
    }
]


def add_product(name, description, image_url, price, category_id):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                    password=config.DB_PASS,
                                    host=config.DB_HOST,
                                    port="5432",
                                    database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Products (name, description, image_url, price, category_id) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (name, description, image_url, price, category_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Products table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Products table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def add_products_to_db():
    for product in products:
        add_product(name=product.get("name"), description=product.get("description"), image_url=product.get("image_url"), price=product.get("price"), category_id=product.get("category_id"))
