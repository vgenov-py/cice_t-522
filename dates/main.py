import datetime
import os

CWD = os.path.dirname(__file__)
print(CWD)
today = datetime.date(2021, 7, 20)
# ten_days = datetime.timedelta(days = 20,)
# print(today + ten_days)

# today = datetime.datetime.today()

# tarjeta_vip = "contraseña"
# tarjeta_vip_expired_date = today + datetime.timedelta(days = 30)
# print(tarjeta_vip_expired_date)

# if today < tarjeta_vip_expired_date:
#     print("Puede acceder a la nueva estación de Gran Vía")

# bday = datetime.date(2022, 5, 12)
# print(today + 10)
# print(type(bday))
# result = bday + today
# print(result)


# 10/10/2020



# user_date = input("YYYY-MM-DD: ")
# dec_user_date = [int(value) for value in user_date.split("-")] 
# date_1 = datetime.date(dec_user_date[0], dec_user_date[1], dec_user_date[2])
# print(date_1)

with open(f"{CWD}/historico.log", "a", encoding="utf8") as file:
    "datetime | status_code | msg | if err "
    file.write(f"{datetime.datetime.today()} | 200 | user post |\n")