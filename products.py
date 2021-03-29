products =[]
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]
    products.append([name, price])
print(products)
# print(products[0][0])

for p in products:
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f: # 寫入模式, 沒有這個檔案就會產生這個檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p [1]) + '\n')
# 離開with自動關閉檔案