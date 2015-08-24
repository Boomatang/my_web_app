import gc
import random
import pymysql
from pymysql import escape_string as thwart
from passlib.hash import sha256_crypt

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
    FROM user_tbl
    WHERE email = %s"""

    data = email

    info = c.execute(sql, data)

    if info == 0:
        output = True
    else:
        output = False

    conn_close(c, conn)
    return output


def create_user_account(values):
    c, conn = connection()

    sql = """
        INSERT INTO user_tbl (firstName, surName, email, paswrd,
        userLevel, joinDate)
        VALUES  (%s, %s, %s, %s, %s, %s)
    """

    data = (values['first_name'],
            values['surname'],
            values['email'],
            values['password'],
            values['account_type'],
            values['join_date'])

    c.execute(sql, data)

    conn_close(c, conn)


def get_user_id(email):

    c, conn = connection()

    sql = """
        SELECT iduser, firstName
        FROM user_tbl
        where email = %s
        """

    data = (email,)

    info = c.execute(sql, data)
    output = False
    if info == 1:
        output = c.fetchone()
    else:
        pass

    conn_close(c, conn)

    return output


def comfirm_password(userid, email, password):
    c, conn = connection()

    sql = """
        SELECT paswrd
        FROM user_tbl
        WHERE email = %s
        AND iduser = %s;
        """

    data = (email, userid)

    info = c.execute(sql, data)

    if info == 1:
        pas_hash = c.fetchone()
        output = sha256_crypt.verify(password, pas_hash[0])

        pas_hash = random.random()
        password = random.random()

    else:
        output = False

    conn_close(c, conn)

    return output
