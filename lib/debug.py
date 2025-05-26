from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def debug_authors():
    print("--- Author Debug ---")
    # Create authors
    author1 = Author.create("Eddie")
    author2 = Author.create("Faith")
    print(f"Created authors: {author1}, {author2}")

    # Get author by ID
    print("Get author by ID:")
    print(Author.get_by_id(author1.id))

    # Update author
    print("Update author name:")
    Author.update(author1.id, name="Edward")
    print(Author.get_by_id(author1.id))

    # Delete author
    print("Delete one author:")
    Author.delete(author2.id)
    print("Remaining authors:")
    for a in Author.all():
        print(a)

def debug_magazines():
    print("--- Magazine Debug ---")
    # Create magazines
    mag1 = Magazine.create("Tech Weekly", "Technology")
    mag2 = Magazine.create("Science Digest", "Science")
    print(f"Created magazines: {mag1}, {mag2}")

    # Get magazine by ID
    print("Get magazine by ID:")
    print(Magazine.get_by_id(mag1.id))

    # List all magazines
    print("All magazines:")
    for m in Magazine.all():
        print(m)

    # Update magazine
    print("Update magazine:")
    Magazine.update(mag1.id, name="Tech Monthly", category="Tech News")
    print(Magazine.get_by_id(mag1.id))

    # Delete magazine
    print("Delete one magazine:")
    Magazine.delete(mag2.id)
    print("Remaining magazines:")
    for m in Magazine.all():
        print(m)

def debug_articles():
    print("--- Article Debug ---")
    # Create authors and magazines for articles
    author1 = Author.create("Eddie")
    author2 = Author.create("Faith")
    mag1 = Magazine.create("Tech Weekly", "Technology")
    mag2 = Magazine.create("Science Digest", "Science")

    # Create articles
    article1 = Article.create("Understanding Python", author_id=author1.id, magazine_id=mag1.id)
    article2 = Article.create("AI in 2025", author_id=author1.id, magazine_id=mag1.id)
    article3 = Article.create("Quantum Basics", author_id=author2.id, magazine_id=mag2.id)
    print("Created Articles:")
    print(article1)
    print(article2)
    print(article3)

    # Get article by ID
    print("Get article by ID:")
    print(Article.get_by_id(article1.id))

    # Get article by title
    print("Get article by title:")
    print(Article.get_by_title("AI in 2025"))

    # List all articles
    print("All articles:")
    for art in Article.all():
        print(art)

    # Articles by author
    print("Articles by author Eddie:")
    for art in Article.articles_by_author(author1.id):
        print(art)

    # Articles by magazine
    print("Articles in Tech Weekly:")
    for art in Article.articles_by_magazine(mag1.id):
        print(art)

    # Update article
    print("Updating article title:")
    Article.update(article1.id, title="Understanding Advanced Python")
    print(Article.get_by_id(article1.id))

    # Delete article
    print("Deleting an article:")
    Article.delete(article2.id)
    print(f"Deleted article with ID {article2.id}")

    print("Remaining articles:")
    for art in Article.all():
        print(art)

if __name__ == "__main__":
    debug_authors()
    debug_magazines()
    debug_articles()





