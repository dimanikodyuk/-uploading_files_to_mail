import pymssql
from db.config import host_delta, user_delta, password_delta, database_delta

conn = pymssql.connect(host=host_delta, user=user_delta, password=password_delta, database=database_delta, as_dict=True)


def ins_file(p_file_name):
    fl = conn.cursor()
    fl.execute("INSERT INTO crm..finx_dog_send_mail(dt_ins, file_name, file_sended) VALUES(GETDATE(), %s, 0)",
               (p_file_name,))
    print(f"INSERT INTO crm..finx_dog_send_mail(dt_ins, file_name, file_sended) VALUES(GETDATE(), {p_file_name}, 0)")
    conn.commit()


def check_file(p_file_name):
    fl = conn.cursor()
    fl.execute("select * from crm..finx_dog_send_mail m where m.file_name = %s;", (p_file_name,))
    check = fl.fetchone()
    return check


def get_file_to_send():
    fl = conn.cursor()
    fl.execute("select * from crm..finx_dog_send_mail m where m.file_sended = 0")
    files = fl.fetchall()
    return files
