class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f"Magazine(id={self.id}, name='{self.name}', category='{self.category}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) < 1:
            raise ValueError("Category cannot be empty")
        self._category = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer or None")
        self._id = value

    @classmethod
    def drop_table(cls):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS magazines")
        conn.commit()
        conn.close()
        print("Magazine table dropped successfully!")

    @classmethod
    def save(cls, magazine):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO magazines (name, category) VALUES (?, ?)",
            (magazine.name, magazine.category)
        )
        magazine.id = cursor.lastrowid
        conn.commit()
        conn.close()
        print(f"Magazine '{magazine.name}' saved with ID {magazine.id}")

    @classmethod
    def create(cls, name, category):
        magazine = cls(name=name, category=category)
        magazine.save(magazine)
        return magazine
    
    @classmethod
    def update(cls, magazine_id, name=None, category=None):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        if name is not None:
            cursor.execute("UPDATE magazines SET name = ? WHERE id = ?", (name, magazine_id))
        if category is not None:
            cursor.execute("UPDATE magazines SET category = ? WHERE id = ?", (category, magazine_id))
        conn.commit()
        conn.close()
        print(f"Magazine with ID {magazine_id} updated")
        if name:
            print(f"Name updated to {name}")
        if category:
            print(f"Category updated to {category}")
    @classmethod
    def delete(cls, magazine_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (magazine_id,))
        conn.commit()
        conn.close()
        print(f"Magazine with ID {magazine_id} deleted")

    @classmethod
    def get_by_id(cls, magazine_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], name=row['name'], category=row['category'])
        return None

    @classmethod
    def get_by_name(cls, name):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], name=row['name'], category=row['category'])
        return None

    @classmethod
    def get_by_category(cls, category):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], name=row['name'], category=row['category']) for row in rows] if rows else []

    def articles(self):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    