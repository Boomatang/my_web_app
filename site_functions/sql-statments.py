import gc
import pymysql
from pymysql import escape_string as thwart

__author__ = 'boomatang'
__version__ = '1'

def connection():
    """
    Use to make a connection to the SQL database
    :return:
    """
    conn = pymysql.connect(host="localhost",
                           user="root",
                           db="shop_front")
    c = conn.cursor()
    return c, conn


def conn_close(c, conn):
    """
    Use to close and commit the trans action with the sql database
    Will do grabge colllection too
    :param c:
    :param conn:
    :return:
    """
    conn.commit()
    c.close()
    conn.close()
    gc.collect()


def check_new_user_email(email):

    c, conn = connection()

    sql = """SELECT email
    WHERE email = %s"""

    data = (email)

    info = c.execute(sql, data)

    if info == 0:
        return True
    else:
        return False
