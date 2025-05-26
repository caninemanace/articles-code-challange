from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

author1 = Author.create("Eddie")
author2 = Author.create("Faith")

mag1 = Magazine.create("Tech Weekly", "Technology")
mag2 = Magazine.create("Science Digest", "Science")

article1 = Article.create("Understanding Python", author_id=author1.id, magazine_id=mag1.id)
article2 = Article.create("AI in 2025", author_id=author1.id, magazine_id=mag1.id)
article3 = Article.create("Quantum Basics", author_id=author2.id, magazine_id=mag2.id)