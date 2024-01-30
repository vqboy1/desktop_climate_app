import sqlite3
db = sqlite3.connect("WEATHER.db")
def get_logins():
    result = db.execute("""select * from "weather_login";""")
    a = []
    for i in result:
        a.append(i)
        print(i)
    return a
def reg(login,password):
    db.execute("""insert into weather_login (Login, Password) values(?,?);""", [login,password])
    db.commit()
def auth(login,password):
    log = get_logins()
    for i in log:
        if i == (login,password):
            return True
    return False
if __name__ == '__main__':
    reg("Вася","1234")
    get_logins()
