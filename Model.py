import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name_publisher = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        return f'publisher {self.id}: {self.name_publisher}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'book {self.id} : ({self.title}, {self.id_publisher})'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name_shop = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        return f'shop {self.id}: {self.name_shop}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)

    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')

    def __str__(self):
        return f'Stock {self.id}: ({self.count}, {self.id_book}, {self.id_shop})'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    data_sale = sq.Column(sq.String(length=50), nullable=False)
    price = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)

    stock = relationship(Stock, backref='sales')

    def __str__(self):
        return f'Sale {self.id}: ({self.count}, {self.data_sale}, {self.price}, {self.id_stock})'


def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
