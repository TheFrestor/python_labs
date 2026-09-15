price = int(input())
discount = int(input())
vat = int(input())
#base = price * (1 - discount/100)
#vat_amount = base * (vat/100)
#total = base + vat_amount
print(f"База после скидки: {price * (1 - discount/100)}.00 ₽")
print(f"НДС: {(price * (1 - discount/100))* (vat/100)}.00 ₽")
print(f"Итого к оплате: {(price * (1 - discount/100))+(price * (1 - discount/100))* (vat/100)}.00 ₽")
