import csv

output_rows = []

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

for file in files:
    with open(file, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["product"].strip().lower() == "pink morsel":
                price = float(row["price"].replace("$", ""))
                quantity = int(row["quantity"])

                sales = price * quantity

                output_rows.append([
                    sales,
                    row["date"],
                    row["region"]
                ])

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sales", "Date", "Region"])
    writer.writerows(output_rows)

print("Done! output.csv created")