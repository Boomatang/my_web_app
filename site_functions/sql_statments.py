import gc
import random

import pymysql
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


def product_full_list():
    c, conn = connection()

    sql = """
        SELECT p.IDproduct, p.product_title, p.product_description, p.product_cost, pi.file_name, pi.ALT_text
        FROM product_tbl p, product_image_tbl pi
        WHERE p.IDproduct = pi.IDproduct
        AND pi.is_default = True
        """

    data = c.execute(sql)

    if data > 0:
        output = c.fetchall()
    else:
        output = None

    conn_close(c, conn)

    return output


def product_details(IDproduct):
    c, conn = connection()

    sql = """
        SELECT p.IDproduct, p.product_title, p.product_description, p.product_cost, concat(u.firstName, ' ', u.surName)
        FROM product_tbl p, user_tbl u
        WHERE p.IDcreator = u.iduser
        AND IDproduct = %s
        AND u.userLevel = 14;
        """
    values = (IDproduct,)

    data = c.execute(sql, values)

    if data == 1:
        output = c.fetchone()
    else:
        output = None

    conn_close(c, conn)

    return output


def product_images(IDprocdut):
    c, conn = connection()

    sql = """
    SELECT pi.file_name, pi.ALT_text, pi.is_default
    FROM product_image_tbl pi
    WHERE pi.IDproduct = %s
    """

    values = (IDprocdut,)

    data = c.execute(sql, values)

    if data > 0:
        output = c.fetchall()
    else:
        output = None

    conn_close(c, conn)

    return output
