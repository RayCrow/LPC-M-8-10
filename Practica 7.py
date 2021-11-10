from ftplib import FTP
from typing import List
import re


# host = "ftp.perftech.com"
host = "b.foobar.fi"
save_path = "D:\Users\RayCrow\Documents\GitHub\LPC-M-8-10\7txt"

user = ""
passw = ""
actpath = ""
lista = []
listatxt = []

def save_file(con: FTP, remote_file_path: str, local_file_path: str):
    with open(local_file_path, "wb") as local_file:
        con.retrbinary(f"RETR {remote_file_path}", local_file.write)


def list_folder(con: FTP, directory: str):
    print(directory)
    listado: List[str] = []
    con.retrlines(f"LIST {directory}", listado.append)
    return listado


def get_file_dir(con: FTP, directory: str):
    listado = list_folder(con, directory)
    return [file_info for file_info in listado if file_info.startswith("-")], [
        file_info for file_info in listado if not file_info.startswith("-")
    ]


def get_file_name(file_info: str) -> str:
    return "".join(file_info.split()[8:])

try:
    connection = FTP()
    connection.connect(host=host, timeout=3)
    connection.login(user, passw)
    l_file, l_dir = get_file_dir(connection, "")
    files_info = "\n".join(l_file)
    dirs_info = "\n".join(l_dir)

    for x in l_dir:
        l_subdir = list_folder(connection, get_file_name(x))
        for i in l_subdir:
            file_name = get_file_name(i)
            lista.append(file_name)
    # print(lista)
    for i in lista:
        exp = re.compile(r".*\.txt")
        co = exp.search(i)
        if co != None:
            listatxt.append(co.group())
    print(listatxt)
    for i in listatxt:
        try:
            save_file(connection, f"{actpath}/{i}", f"{save_path}/{i}")
        except Exception:
            pass
except Exception as e:
    print("La conexion fallo " + str(e))