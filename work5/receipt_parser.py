import re
#1.Extract all prices from the receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

prices = re.findall(r"\d[\d ]*,\d{2}", text)

print(prices)



#2. Find all product names
products = re.findall(r"\d+\.\n(.+)", text)

for p in products:
    print(p)


#3. Calculate total amount
numbers = []
for p in prices:
    p = p.replace(" ", "")     
    p = p.replace(",", ".")    
    numbers.append(float(p))    

total = sum(numbers)

print(total)


#4. Extract date and time information
datetime = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)

print(datetime.group())

#5. Find payment method
payment = re.search(r"([А-Яа-яA-Za-z\s]+):\n\d[\d ]*,\d{2}", text)

if payment:
    print(payment.group(1))


#6. Create a structured output (JSON or formatted text)
import json

data = {
    "date": date,
    "time": time,
    "total": total,
    "payment_method": payment_method,
    "products": products
}

print(json.dumps(data, indent=4, ensure_ascii=False))