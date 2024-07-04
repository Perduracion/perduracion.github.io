from app.database import get_db



class Product:
    # product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # product_name = db.Column(db.String(60), nullable=False)
    # product_desc = db.Column(db.String(155), nullable=False)
    # product_image_path = db.Column(db.String(15), nullable=True)
    # product_price = db.Column(db.Decimal(10, 2), nullable=True)
    # product_cat_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'))
    # category = db.relationship('Category', backref='products')

    def __init__(self,product_id = None, 
                 product_name = None, 
                 product_desc = None, 
                 product_image_path = None, 
                 product_price = None, 
                 product_cat_id = None, 
                 category = None
                 ):
    
        self.product_id=product_id
        self.product_name=product_name
        self.product_desc=product_desc
        self.product_image_path=product_image_path
        self.product_price=product_price
        self.product_cat_id=product_cat_id
        self.category=category

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM product order by product_cat_id desc")
        rows = cursor.fetchall()
        
        products = [Product(product_id=row[0], 
                            product_name=row[1], 
                            product_desc=row[2], 
                            product_image_path=row[3], 
                            product_price=row[4],
                            product_cat_id=row[5]) for row in rows]
        cursor.close()
        return products
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.product_id:
            
            cursor.execute(f"""
                UPDATE product SET product_name = "{self.product_name}", 
                    product_desc = "{self.product_desc}", 
                    product_image_path = "{self.product_image_path}", 
                    product_price = {self.product_price},
                    product_cat_id = {self.product_cat_id}
                WHERE product_id = {self.product_id}
            """)
        else:
            query=f"""                
                INSERT INTO product (product_name, 
                                    product_desc, 
                                    product_image_path, 
                                    product_price, 
                                    product_cat_id)
                VALUES (
                "{self.product_name}", 
                "{self.product_desc}",
                "{self.product_image_path}",
                {self.product_price}, 
                {self.product_cat_id}
                );

            """
            print(query)
            cursor.execute(query)
            self.id_movie = cursor.lastrowid
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
        query=f"SELECT * FROM product WHERE product_id = {product_id}"
        print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Product(product_id=row[0], 
                            product_name=row[1], 
                            product_desc=row[2], 
                            product_image_path=row[3], 
                            product_price=row[4],
                            product_cat_id=row[5]) 
        
        return None


    def delete_by_id(product_id):
         db = get_db()
         cursor = db.cursor()
         cursor.execute(f"DELETE FROM product WHERE PRODUCT_ID = {product_id}")
         db.commit()
         cursor.close()

