from pprint import pprint

import pandas as pd
import psycopg2.extras
# from psycopg2.errors import UniqueViolation

from DB.DB import conn


def db_cats_list():
    """Выводит все существующие категории"""
    with conn.cursor() as cur:
        select_query = '''SELECT category FROM myurist_affairs;'''
        cur.execute(select_query)
        list_cats = []
        for one in cur.fetchall():
            for one_tuple in one:
                if one_tuple in list_cats:
                    pass
                else:
                    list_cats.append(one_tuple)
        return list_cats


def db_sub_cats_list(cat):
    """Выводит все существующие подкатегории"""
    with conn.cursor() as cur:
        select_query = "SELECT sub_category FROM myurist_affairs WHERE category = '{}'".format(cat)
        cur.execute(select_query)
        list_cats = []
        for one in cur.fetchall():
            for one_tuple in one:
                if one_tuple in list_cats:
                    pass
                else:
                    list_cats.append(one_tuple)
        return list_cats


def search_delo(sub_cats):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        select = """SELECT "date", plaintiff, defendant, court, dispute, summ_plaintiff, result_client, result_court,
        image_result, purist, urls, "role" FROM myurist_affairs WHERE sub_category  = '{}'""".format(sub_cats)
        cur.execute(select)
        res = cur.fetchall()
        res_list = []
        for row in res:
            res_list.append(dict(row))
        return res_list


def db_records(name, number, about, username):
    with conn.cursor() as cur:
        insert_query = "INSERT INTO myurist_record (name, numbers_phone, dispute, username) VALUES ('{}', '{}', '{}', '{}')".format(name, number, about, username)
        cur.execute(insert_query)
        conn.commit()
