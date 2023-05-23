import sqlalchemy
from Model import create_table, Publisher, Stock, Shop, Sale, Book
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:x26n06dimon26@localhost:5432/base_orm'
engine = sqlalchemy.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

n_p1 = Publisher(name_publisher='Пушкин')
n_p2 = Publisher(name_publisher='Гоголь')
n_p3 = Publisher(name_publisher='Толстой')

session.add_all([n_p1, n_p2, n_p3])
session.commit()

book1 = Book(title='Пиковая дама', publisher=n_p1)
book2 = Book(title='Капитанская дочка', publisher=n_p1)
book3 = Book(title='Вий', publisher=n_p2)
book4 = Book(title='Мертвые души', publisher=n_p2)
book5 = Book(title='Война и мир', publisher=n_p3)
book6 = Book(title='Воскрешение', publisher=n_p3)


session.add_all([book1, book2, book3, book4, book5, book6])
session.commit()

shop1 = Shop(name_shop='Мир книг')
shop2 = Shop(name_shop='бумага с')
session.add_all([shop1, shop2])
session.commit()

stock1 = Stock(count=1, id_book=1, id_shop=1)
stock2 = Stock(count=2, id_book=2, id_shop=1)
stock3 = Stock(count=3, id_book=3, id_shop=1)
stock4 = Stock(count=4, id_book=4, id_shop=2)
stock5 = Stock(count=5, id_book=5, id_shop=2)
stock6 = Stock(count=6, id_book=6, id_shop=2)

session.add_all([stock1,stock2,stock3,stock4,stock4,stock5,stock6])
session.commit()

sale1 = Sale(count=1, data_sale='22-03-2021', price=540, id_stock=1)
sale2 = Sale(count=2, data_sale='16-05-2022', price=780, id_stock=2)
sale3 = Sale(count=3, data_sale='26-07-2023', price=600, id_stock=3)
sale4 = Sale(count=4, data_sale='12-12-2023', price=456, id_stock=4)
sale5 = Sale(count=5, data_sale='05-01-2022', price=654, id_stock=5)
sale6 = Sale(count=6, data_sale='19-06-2021', price=945, id_stock=6)

session.add_all([sale1,sale2,sale3,sale4,sale5,sale6])
session.commit()


publisher = input('Введите идентификатор издателя: ')
for name_book in session.query(Book).join(Book.publisher).filter(Publisher.id == publisher).all():
    title_book = session.query(Book.id).join(Book.publisher).filter(Publisher.id == publisher).subquery()
    stock_id = session.query(Stock.id).join(title_book, Stock.id_book == title_book.c.id).subquery()
    shop_id = session.query(Stock.id_shop).join(title_book, Stock.id_book == title_book.c.id).subquery()
    for name_shop in session.query(Shop).join(shop_id, Shop.id == shop_id.c.id_shop).all():
        name_shop2 = name_shop
    for sale_info in session.query(Sale).join(stock_id, Sale.id_stock == stock_id.c.id).all():
        sale_info2 = sale_info
    print(f' {name_book} | {name_shop2} | {sale_info2}')
session.commit()

session.close()