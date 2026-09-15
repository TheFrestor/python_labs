price = int(input("price: "))
discount = int(input("discount: "))
vat = int(input("vat: "))
#base = price * (1 - discount/100)
#vat_amount = base * (vat/100)
#total = base + vat_amount
print(f"База после скидки: {price * (1 - discount/100)}0 ₽")
print(f"НДС: {(price * (1 - discount/100))* (vat/100)}0 ₽")
print(f"Итого к оплате: {(price * (1 - discount/100))+(price * (1 - discount/100))* (vat/100)}0 ₽")
