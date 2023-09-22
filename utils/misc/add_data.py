import psycopg2
from data import config

categories = [
    {
        "name": "📲 Telefonlar"
    },
    {
        "name": "💻 Noutbuklar"
    },
    {
        "name": "💡 Maishiy texnikalar"
    },
    {
        "name": "🎙 Aksessuarlar"
    },
    {
        "name": "iPhone",
        "parent_id": 1
    },
    {
        "name": "SAMSUNG",
        "parent_id": 1
    },
    {
        "name": "Xiaomi",
        "parent_id": 1
    },
    {
        "name": "Vivo",
        "parent_id": 1
    },
    {
        "name": "Macbook",
        "parent_id": 2
    },
    {
        "name": "DELL",
        "parent_id": 2
    },
    {
        "name": "Asus",
        "parent_id": 2
    },
    {
        "name": "Acer",
        "parent_id": 2
    },
    {
        "name": "Kir yuvish mashinasi",
        "parent_id": 3
    },
    {
        "name": "Konditsioner",
        "parent_id": 3
    },
    {
        "name": "Muzlatgich",
        "parent_id": 3
    },
    {
        "name": "Gaz plitasi",
        "parent_id": 3
    }
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
        "name": "iPhone 14 Pro 256GB Silver",
        "description": "Phone bilan ishlashning yangi sehrli usuli.\nHayotni saqlab qolish uchun yaratilgan innovatsion xavfsizlik xususiyatlari.\nAjoyib tafsilotlar uchun innovatsion 48 megapikselli kamera.\nUlarning barchasi smartfonlar uchun eng yangi chip bilan jihozlangan.\nHar qanday smartfon oynasidan ko'ra bardoshli keramik ekran bilan. Suvga chidamli. Jarrohlik sinfidagi zanglamaydigan po'lat.",
        "image_url": "https://images.uzum.uz/cdq98a2vtie1lhbe1arg/original.jpg",
        "price": 15612999,
        "category_id": 5
    },
    {
        "name": "iPhone 13 128GB",
        "description": "Phone bilan ishlashning yangi sehrli usuli.\nHayotni saqlab qolish uchun yaratilgan innovatsion xavfsizlik xususiyatlari.\nAjoyib tafsilotlar uchun innovatsion 48 megapikselli kamera.\nUlarning barchasi smartfonlar uchun eng yangi chip bilan jihozlangan.\nHar qanday smartfon oynasidan ko'ra bardoshli keramik ekran bilan. Suvga chidamli. Jarrohlik sinfidagi zanglamaydigan po'lat.",
        "image_url": "https://images.uzum.uz/cifat5r6edfostii340g/original.jpg",
        "price": 11999999,
        "category_id": 5
    },
    {
        "name": "Galaxy A54 5G 8/256 GB",
        "description": "OT: Android 13\nDispley: 6,4 dyuymli Super AMOLED - 1080 x 2340\nChip: Samsung Exynos 1380\nKamera: 3 (50 MP + 12 MP + 5 MP)\nBatareya: 5000 mA / soat\nOg'irligi: 202 gr.",
        "image_url": "https://images.uzum.uz/ck1guakjvf2qegt3ku30/original.jpg",
        "price": 5439999,
        "category_id": 6
    },
    {
        "name": "Galaxy S23 Ultra",
        "description": "Mahsulot haqida qisqacha:\nProtsessor - Qualcomm Snapdragon 8 Gen2\nOperatsion tizim - Android 13\nHimoya darajasi - IP68\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKameralar - orqa tomondan 4 (200 MP + 10 MP + 12 MP + 10 MP), old kamera 12 MP\n5000 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cjhm2akvutv1klhdlm00/original.jpg",
        "price": 16999000,
        "category_id": 6
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
