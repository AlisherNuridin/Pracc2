import re

text = open("raw.txt").read()

prices = re.findall(r"\d+\.\d{2}", text)
date = re.search(r"\d{2}/\d{2}/\d{4}", text)
time = re.search(r"\d{2}:\d{2}", text)
payment = re.search(r"Cash|Card", text)

print("Prices:", prices)
print("Total:", sum(float(p) for p in prices))
print("Date:", date.group() if date else "")
print("Time:", time.group() if time else "")
print("Payment:", payment.group() if payment else "")