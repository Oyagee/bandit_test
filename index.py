from django.db import connection


def find_user(login):
    '''Поиск пользователя в базе данных'''
    with connection.cursor() as cursor_db:
        cursor_db.execute(f"""select login from USERS where name = '{login}'""")
        result = cursor_db.fetchone()
    return result