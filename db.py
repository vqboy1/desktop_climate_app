import sqlite3
db = sqlite3.connect("WEATHER.db")
def get_logins():
    result = db.execute("""select * from "weather_login";""")
    a = []
    for i in result:
        a.append(i)
        print(i)
    return a

def get_users():
    result = db.execute("""select Login from "weather_login";""")
    a = []
    for i in result:
        a.append(i[0])
        print(a)
    return a


def reg(login,password):
    db.execute("""insert into weather_login (Login, Password) values(?,?);""", [login,password])
    db.commit()


def auth(login,password):
    log = get_logins()
    if (login, password) in log:
        return True
    return False


if __name__ == '__main__':
    get_logins()
    get_users()