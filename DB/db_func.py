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


def db_add_new_user(username: str, chat_id: str):
    with conn.cursor() as cur:
        insert_query = "INSERT INTO myurist_usertg (username1, chat_id) VALUES ('{}', '{}')".format(username, chat_id)
        cur.execute(insert_query)
        conn.commit()


def db_member(chat_id):
    with conn.cursor() as cur:
        select_cuery = "SELECT id FROM myurist_usertg WHERE chat_id = '{}'".format(chat_id)
        cur.execute(select_cuery)
        res = cur.fetchone()
        return res


def db_new_chat(chat_id:int, username:str, topic_id):
    with conn.cursor() as cur:
        insert_query = ("insert into myurist_chatusers (chat_id, user_name, topic_id) VALUES"
                        " ({}, '{}', {}) ON CONFLICT DO NOTHING").format(chat_id, username, topic_id)
        cur.execute(insert_query)
        conn.commit()

def db_list_id():
    with conn.cursor() as cur:
        select_query = "select chat_id from myurist_chatusers"
        cur.execute(select_query)
        ret = cur.fetchall()
        ret_list = []
        for tup in ret:
            for row in tup:
                ret_list.append(row)
        return ret_list

# print(db_list_id())

def db_user_topic(chat_id):
    with conn.cursor() as cur:
        select_query = "select topic_id from myurist_chatusers where chat_id = {}".format(chat_id)
        cur.execute(select_query)
        ret = cur.fetchone()
        return ret[0]

def db_user_id(topic):
    with conn.cursor() as cur:
        select_query = "select chat_id from myurist_chatusers where topic_id = {}".format(int(topic))
        cur.execute(select_query)
        ret = cur.fetchone()
        return ret[0]


def db_delete_chat(chat_id):
    with conn.cursor() as cur:
        delete_query = "DELETE FROM myurist_chatusers where chat_id = {}".format(chat_id)
        cur.execute(delete_query)
        conn.commit()