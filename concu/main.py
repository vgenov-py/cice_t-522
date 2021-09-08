import threading
import time
import concurrent.futures
import requests as req

res = req.get("https://restcountries.eu/rest/v2/all").json()

flags = (country["flag"] for country in res)


# flags = ["https://images.unsplash.com/photo-1563615728293-670199b973ad?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80","https://images.unsplash.com/photo-1630257956817-0734ff3846dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80", "https://images.unsplash.com/photo-1574619151033-a9e1f81cae52?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80", "https://images.unsplash.com/photo-1590514845251-47d80b094702?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80", "https://images.unsplash.com/photo-1631002165161-27b558475f58?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80", "https://images.unsplash.com/photo-1630951633284-f35d46350ac3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80", "https://images.unsplash.com/photo-1630968636109-a60480bd85af?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80", "https://images.unsplash.com/photo-1631006695356-e4fa367afe5e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"]


def get_flag(flag_url):
    flag = req.get(flag_url).content
    with open(f"./concu/flags/{flag_url[-7:]}", "wb") as file:
        file.write(flag)


# start_f = time.perf_counter()
# for flag in flags:
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.submit(get_flag, flag)

# finish_f = time.perf_counter()

# print("Concurrent: ", (finish_f - start_f))

# start_t = time.perf_counter()
# for flag in flags:
#     t = threading.Thread(target=get_flag, args=[flag])
#     t.start()
# finish_t = time.perf_counter()
# print("Threading: ", finish_t-start_t)


start_f = time.perf_counter()


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_flag, flags)

finish_f = time.perf_counter()
print("Concurrent: ", (finish_f - start_f))













# start_t = time.perf_counter()
# for flag in flags:
#     t = threading.Thread(target=get_flag, args=[flag])
#     t.start()
# finish_t = time.perf_counter()
# print("Threading: ", finish_t-start_t)


# start_n = time.perf_counter()
# count = 0
# for flag in flags:
#     get_flag(flag)
#     count += 1
# finish_n = time.perf_counter()
# print("Without concurrent: ", (finish_n - start_n), count)

# start = time.perf_counter()

# def a_dormir(secs):
#     time.sleep(secs)
#     return secs

# t_1 = threading.Thread(target=a_dormir, args=[4])
# # t_2 = threading.Thread(target=a_dormir)

# t_1.start() # 1º
# print("t_1 se ha ejecutado")
# t_2.start() 
# print("t_2 se ha ejecutado")
# t_1.join()
# t_2.join()



# # a_dormir()
# # a_dormir()
