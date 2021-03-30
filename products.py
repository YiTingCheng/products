import os # operating system

# 讀取檔案
def read_file(filename):
	products =[]
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續
			name, price = line.strip().split(',') # 先把換行符號去掉, 再用逗點作為切割依據
			# 切割完的結果是清單
			products.append([name, price])
	return products # 回傳清單

# 讓使用者輸入
def user_input(products):
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
	return products
	# print(products[0][0])

#印出所有購買記錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

	# 'abc' + '123' = 'abc123'
	# 'abc' * 3 = 'abcabcabc'

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: # 寫入模式, 沒有這個檔案就會產生這個檔案
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p [1]) + '\n')
	# 離開with自動關閉檔案

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在
		print('Yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()