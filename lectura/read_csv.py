import csv
with open("export_bookshop_2.csv", "w" ,encoding="utf8", newline="") as file:
    # data = json.load(file)

    csv_writer = csv.writer(file, delimiter=",", dialect="excel")
    csv_writer.writerow(["hola", "como"])
    csv_writer.writerow("5")
    csv_writer.writerow("7")
    csv_writer.writerow("9")
    