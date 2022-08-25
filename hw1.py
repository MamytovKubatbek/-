
import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    database = 'shoping',
    user = 'postgres',
    password = 'postgres',
)

con = connection.cursor()

try:
    query = 'CREATE TABLE Products ( ID SERIAL PRIMARY KEY, ProductName VARCHAR(30) NOT NULL, Company VARCHAR(20) NOT NULL, ProductCount INTEGER DEFAULT 0, Price NUMERIC NOT NULL );'
    con.execute(query)
    query = "CREATE TABLE archiv (Id SERIAL, FirstName VARCHAR(30) NOT NULL, email VARCHAR(255), PASSWORD VARCHAR(15));"   
    con.execute(query)
    print("Успешто отпровлен запрос")
except:
    print("Существует такой таблица")
connection.commit()

# con.execute("INSERT INTO Products(ProductName, Company, ProductCount, Price) \
# VALUES ('iPhone X', 'Apple', 2, 66000), \
# ('iPhone 8', 'Apple', 2, 51000),\
# ('iPhone 7', 'Apple', 5, 42000),\
# ('Galaxy S9', 'Samsung', 2, 56000),\
# ('Galaxy S8 Plus', 'Samsung', 1, 46000),\
# ('Nokia 9', 'HDM Global', 2, 26000),\
# ('Desire 12', 'HTC', 6, 38000)")
# connection.commit()

# con.execute("INSERT INTO archiv(FirstName, email, password) VALUES \
# ('Kubatbek Mamytov', 'mamytovkubat157@gmail.com', 'Kubat.140800k');")
# connection.commit()
def adminPanel():
    print("Вы админ панеле")
    while True:
        print(" 1) Добавить товар        2) Удалить клиент  \
               \n3) Изменить цену       4) Изменить количество товар \
               \n5) Exit") 
        a = int(input("Вберите один изних: "))
        if a == 1:
            print("Добавить товар")
            con.execute("SELECT * FROM PRODUCTS")
            for i in con.fetchall():
                print(*i)
            i = True
            while i:
                ProductName = input("ProductName: ")
                con.execute("SELECT ProductName FROM PRODUCTS")
                a = []
                for i in data:
                    l = [*i]
                    for j in l:
                        a.append(j)  
                if len(ProductName) > 0:
                    if ProductName not in a:
                        Company = input("Company: ")
                        ProductCount = input("ProductCount: ")
                        Price = input("Price: ")
                        con.execute(f"INSERT INTO Products(ProductName, Company, ProductCount, Price) \
                        VALUES ('{ProductName}', '{Company}', '{ProductCount}', '{Price}')")
                        connection.commit()
                        print("Успешно Добавлён")
                    else:
                        print(f"{ProductName} Этот товар существует")
                else:
                    i = False
        elif a == 2:
            print("Удалить клиент")
            con.execute("SELECT * FROM ARCHIV")
            for i in con.fetchall():
                print(*i)
            i = True
            while i:
                ids = input("Удалить по ID: ")
                if len(ids) >= 1:
                   con.execute(f"DELETE FROM ARCHIV WHERE ID = {int(ids)}")
                   connection.commit()
                else:
                    i = False
        elif a == 3:
            print("Изменить цену")
            con.execute("SELECT * FROM PRODUCTS")
            for i in con.fetchall():
                print(*i)
            i = True
            while i:
                ProductName = input("Названия товары: ")
                con.execute(f"SELECT PRICE FROM PRODUCTS WHERE ProductName = '{ProductName}'")
                name_price = 0
                for i in con.fetchall():
                    name_price = int(*i)
                print(name_price)
                if len(ProductName) >= 1 and name_price > 0:
                    Price_product = int(input("Price: "))
                    con.execute(f"SELECT ID FROM PRODUCTS WHERE ProductName = '{ProductName}'")
                    id_price = 0
                    for i in con.fetchall():
                         id_price = int(*i)
                    con.execute(f"UPDATE products SET PRICE = {Price_product} WHERE ID = {id_price}")
                    connection.commit()
                    print("Цену товар изменон")
                elif ProductName == '':
                    i = False
                elif name_price == 0:
                    print("Такое товары нет списке")

        elif a == 4:
            print("Изменить количество товар")
            con.execute("SELECT * FROM PRODUCTS")
            for i in con.fetchall():
                print(*i)
            i = True
            while i:
                ProductName = input("Названия товары: ")
                con.execute(f"SELECT ProductCount FROM PRODUCTS WHERE ProductName = '{ProductName}'")
                name_price = 0
                for i in con.fetchall():
                    name_price = int(*i)
                print(name_price)
                if len(ProductName) >= 1 and name_price > 0:
                    ProductCount = int(input('Добавить Количество: '))
                    con.execute(f"SELECT ID FROM PRODUCTS WHERE ProductName = '{ProductName}'")
                    id_price = 0
                    for i in con.fetchall():
                         id_price = int(*i)
                    con.execute(f"UPDATE products SET ProductCount = {name_price + ProductCount} WHERE ID = {id_price}")
                    connection.commit()
                    print("Количество товар изменон")
                elif ProductName == '':
                    i = False
                elif name_price == 0:
                    print("Такое товары нет списке")
        elif a == 5:
            break


def product():
    print('Добро пожаловать в магазин Мир технологий')
    print('Список наших товаров:')
    con.execute('SELECT ProductName, Company, Price FROM products')
    data = con.fetchall()
    for i in data:
        print(*i)
    connection.commit()
    while True:
        a = input('Что вы хотите купить?: ')
        if len(a)>0:
            con.execute(f"SELECT ProductName From products WHERE ProductName iLIKE '{a}%'")
            connection.commit()
            productName = con.fetchall()
            name_pro = []
            for i in productName:
                name_pro.append(*i)
            if len(name_pro) >= 2:
                print(name_pro)
            elif len(name_pro) == 1:
                print(name_pro)
                con.execute(f"SELECT ProductCount FROM products WHERE ProductName = '{a}'")
                f = con.fetchall()
                g = 0
                for y in f:
                    g = int(*y)
                connection.commit()

                while True:
                    b = int(input('Количество: '))
                    if int(g) >= b:
                        con.execute(f"UPDATE products SET ProductCount = {g - b} WHERE ProductCount = {g}")
                        connection.commit()
                        con.execute(f"SELECT Price FROM products WHERE ProductName = '{a}'")
                        connection.commit()
                        w = con.fetchall()
                        c = 0
                        for r in w:
                            c = int(*r)
                        con.execute(f"SELECT FirstName, email FROM ARCHIV WHERE EMAIL = '{new_email}'")
                        connection.commit
                        print(f"""Товар {a} \nКолисечтво {b} \nЦена {c} \nОбщая сумма {b * c} 
                        """)
                        break
                    else:
                        if g == 0:
                            break
                        else:
                            print(f'У нас в складе имеется только {g} штук')
            else:
                print(f'У нас нету такой телефон {a}')
        else:
            break


br = True
while br:
    print("1) Мне ест акаунт     2) Регистратция")

    ab = int(input("... "))
    if ab == 1:
        i = True
        while i:
            new_email = input('Email: ')
            password = input("Password: ")
            con.execute(f"SELECT * FROM ARCHIV WHERE EMAIL = '{new_email}'")
            connection.commit
            data = con.fetchall()
            a = []
            for i in data:
                l = [*i]
                for j in l:
                    a.append(j)   
            if "@" in new_email and new_email.count(".", new_email.index("@")):        
                if new_email== 'mamytovkubat157@gmail.com' and password== 'Kubat.140800k':
                    adminPanel()
                    i = False
                    br = False
                    
                elif new_email in a and password in a:
                    product()
                    i = False
                    br = False
                elif new_email in a and password not in a:
                    print(f"Существует такой {new_email} почту \nВведите провилно <<<Пароль>>>") 
                           
                else:
                    print("нет такой почту Региструвийте")
                    i = False
            else:
                print("Ошибочная почта")

    elif ab == 2:
        i = True
        while i:
            fullName = input("ФИО:")
            new_email = input('Email or NEW_Email: ')
            password = input("Password: ")
            if "@" in new_email and new_email.count(".", new_email.index("@")):
                con.execute(f"SELECT * FROM ARCHIV WHERE EMAIL = '{new_email}'")
                connection.commit
                data = con.fetchall()
                a = []
                for i in data:
                    l = [*i]
                    for j in l:
                       a.append(j)
                if new_email in a and password not in a:
                    print(f"Существует такой {new_email} почту") 

                elif new_email not in a and password not in a:
                    con.execute(f"INSERT INTO archiv(FirstName, email, password) VALUES ('{fullName}', '{new_email}', '{password}');")
                    connection.commit()
                    product()
                    br = False
            else:
                print("Ошибочная почта")

con.close() 
connection.close()

print("project")