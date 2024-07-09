from app.database import get_db

class Product:
    def __init__(self, product_id=None, product_name=None, product_desc=None, product_image_path=None,
                 product_price=None, product_cat_id=None, category=None):
        self.product_id = product_id
        self.product_name = product_name
        self.product_desc = product_desc
        self.product_image_path = product_image_path
        self.product_price = product_price
        self.product_cat_id = product_cat_id
        self.category = category

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        cursor.close()
        
        return [Product(*row) for row in rows]

    def save(self):
        db = get_db()
        cursor = db.cursor()

        if self.product_id:
            cursor.execute("""
                UPDATE product SET 
                    product_name = %s, 
                    product_desc = %s, 
                    product_image_path = %s, 
                    product_price = %s,
                    product_cat_id = %s
                WHERE product_id = %s
            """, (self.product_name, self.product_desc, self.product_image_path,
                  self.product_price, self.product_cat_id, self.product_id))
        else:
            cursor.execute("""
                INSERT INTO product (product_name, product_desc, product_image_path, product_price, product_cat_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (self.product_name, self.product_desc, self.product_image_path,
                  self.product_price, self.product_cat_id))
            self.product_id = cursor.lastrowid

        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_desc': self.product_desc,
            'product_image_path': self.product_image_path,
            'product_price': self.product_price,
            'product_cat_id': self.product_cat_id,
        }

    @staticmethod
    def get_by_id(product_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return Product(*row)
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM product WHERE product_id = %s", (self.product_id,))
        db.commit()
        cursor.close()
