class Author:

    def __init__(self, name,id=None):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}')"
    
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
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer or None")
        self._id = value\
        
    @classmethod
    def drop_table(cls):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS authors")
        conn.commit()
        conn.close()
        print("Author table dropped successfully!")
    @classmethod
    def save(cls, author):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (author.name,))
        author.id = cursor.lastrowid
        conn.commit()
        conn.close()
        print(f"Author {author.name} saved with ID {author.id}")
    @classmethod
    def create(cls, name):
        author = cls(name=name)
        author.save(author)
        return author
    @classmethod
    def get_by_id(cls, author_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], name=row['name'])
        return None
    @classmethod
    def get_by_name(cls, name):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(id=row['id'], name=row['name']) if row else None
    @classmethod
    def articles_by_author(cls, author_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    @classmethod
    def magazines_by_author(cls, author_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.*
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (author_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []



