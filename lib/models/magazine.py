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
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (magazine.name, magazine.category))
        magazine.id = cursor.lastrowid
        conn.commit()
        conn.close()
        print(f"Magazine '{magazine.name}' saved with ID {magazine.id}")

    @classmethod
    def create(cls, name, category):
        magazine = cls(name=name, category=category)
        cls.save(magazine)
        return magazine

    @classmethod
    def update(cls, magazine_id, name=None, category=None):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        updates = []
        params = []
        if name is not None:
            updates.append("name = ?")
            params.append(name)
        if category is not None:
            updates.append("category = ?")
            params.append(category)
        if updates:
            params.append(magazine_id)
            cursor.execute(f"UPDATE magazines SET {', '.join(updates)} WHERE id = ?", tuple(params))
            conn.commit()
            print(f"Magazine with ID {magazine_id} updated!")
        else:
            print("No updates provided.")
        conn.close()

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
        return cls(id=row['id'], name=row['name'], category=row['category']) if row else None

    @classmethod
    def get_by_name(cls, name):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(id=row['id'], name=row['name'], category=row['category']) if row else None

    @classmethod
    def all(cls):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], name=row['name'], category=row['category']) for row in rows] if rows else []

    def articles(self):
        from lib.models.article import Article
        return Article.articles_by_magazine(self.id)

    def contributors(self):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT authors.*
            FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []

    

    