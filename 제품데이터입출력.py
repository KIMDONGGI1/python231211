import sqlite3

class ProductManager:
    def __init__(self, db_path='products.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # 제품 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, quantity, price):
        # 제품 추가
        self.cursor.execute('''
            INSERT INTO products (product_name, quantity, price) VALUES (?, ?, ?)
        ''', (product_name, quantity, price))
        self.conn.commit()

    def update_product(self, product_id, product_name, quantity, price):
        # 제품 업데이트
        self.cursor.execute('''
            UPDATE products SET product_name=?, quantity=?, price=? WHERE product_id=?
        ''', (product_name, quantity, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        # 제품 삭제
        self.cursor.execute('DELETE FROM products WHERE product_id=?', (product_id,))
        self.conn.commit()

    def select_all_products(self):
        # 모든 제품 조회
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

# 샘플 데이터 10개 준비
sample_data = [
    ('Laptop', 5, 1200.0),
    ('Smartphone', 10, 800.0),
    ('Headphones', 20, 50.0),
    ('Tablet', 8, 300.0),
    ('Camera', 15, 700.0),
    ('Printer', 3, 150.0),
    ('Smartwatch', 12, 200.0),
    ('External HDD', 7, 100.0),
    ('Bluetooth Speaker', 25, 30.0),
    ('Gaming Mouse', 18, 60.0)
]

# ProductManager 인스턴스 생성
product_manager = ProductManager()

# 샘플 데이터 추가
for data in sample_data:
    product_manager.insert_product(*data)

# 모든 제품 조회
all_products = product_manager.select_all_products()
print("=== All Products ===")
for product in all_products:
    print(product)

# 제품 업데이트
product_manager.update_product(1, 'Updated Laptop', 7, 1500.0)

# 모든 제품 재조회
updated_products = product_manager.select_all_products()
print("\n=== Updated Products ===")
for product in updated_products:
    print(product)

# 제품 삭제
product_manager.delete_product(3)

# 모든 제품 재조회
remaining_products = product_manager.select_all_products()
print("\n=== Remaining Products ===")
for product in remaining_products:
    print(product)

# 연결 종료
product_manager.conn.close()
