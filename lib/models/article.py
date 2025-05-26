class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f"Article(id={self.id}, title='{self.title}', author_id={self.author_id}, magazine_id={self.magazine_id})"

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 1:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def author_id(self):
        return self._author_id
    @author_id.setter
    def author_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Author ID must be an integer")
        self._author_id = value

    @property
    def magazine_id(self):
        return self._magazine_id
    @magazine_id.setter
    def magazine_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Magazine ID must be an integer")
        self._magazine_id = value

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
        cursor.execute("DROP TABLE IF EXISTS articles")
        conn.commit()
        conn.close()
        print("Article table dropped successfully!")

    @classmethod
    def save(cls, article):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (article.title, article.author_id, article.magazine_id)
        )
        article.id = cursor.lastrowid
        conn.commit()
        conn.close()
        print(f"Article '{article.title}' saved with ID {article.id}")

    @classmethod
    def create(cls, title, author_id, magazine_id):
        article = cls(title=title, author_id=author_id, magazine_id=magazine_id)
        cls.save(article)
        return article

    @classmethod
    def get_by_id(cls, article_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'])
        return None

    @classmethod
    def get_by_title(cls, title):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'])
        return None

    @classmethod
    def articles_by_author(cls, author_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in rows]

    @classmethod
    def articles_by_magazine(cls, magazine_id):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in rows]

    @classmethod
    def all(cls):
        from lib.db.connection import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in rows]


