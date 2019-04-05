import os
import sqlite3
from collections import namedtuple
from utils import Book


book_db = 'PDF.db'
book_info = namedtuple('info',  'path page flag')


def read_db():
    # 将路径更改为该文件所处路径
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists(book_db):
        conn = sqlite3.connect(book_db)
        conn.execute("CREATE TABLE book_info(path, page, flag)")
        conn.close()
    conn = sqlite3.connect(book_db)
    for row in conn.execute('SELECT * FROM book_info'):
        info = book_info(*row)
        book = Book(info.path)
        book.page = info.page
        book.flag = info.flag
        yield book
        
    conn.close()  
  
  
    

def remove_db():
    conn = sqlite3.connect(book_db)
    conn.execute('DELETE FROM book_info')
    conn.commit()
    conn.close()


def save2db(booklist):
    conn = sqlite3.connect(book_db)
    conn.executemany("INSERT INTO book_info Values (?,?,?)",
                ((book.fname, book.page, book.flag) for book in booklist))
    conn.commit()
    conn.close()
    
    
if __name__ == '__main__':
    pass
