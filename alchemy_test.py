from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return self.title

engine = create_engine('sqlite://', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# authors = session.query(Author)
# session.add_all([
#     Author('Lewis Carroll'),
#     Author('Mark Twain'),
#     Author('Steven King')
# ])
lc = Author(name='Lewis Carroll')
lc.books = [
    Book(title='Alice in a wonderland')
]
mt = Author(name='Mark Twain')
mt.books = [
    Book(title='Tom Soyer')
]
sk = Author(name='Steven King')
sk.books = [
    Book(title='Thing'),
    Book(title='Birds')
]

session.add(lc)
session.add(mt)
session.add(sk)
session.commit()

for item in session.query(Author):
    print item.id, item.name

for item in session.query(Book):
    print item.title, item.author_id

# tw = session.query(Author).filter(Author.name == 'Mark Twain').one()
# session.delete(tw)
# session.commit()

# for book, author in session.query(Book, Author).filter(Book.author_id == Author.id):
#     print book.title + ' - ' + author.name

for author in session.query(Author):
    print '{} - {}'.format(author.name, [x for x in author.books])

for book in session.query(Book):
    print '{} - {}'.format(book.title, book.author.name)
