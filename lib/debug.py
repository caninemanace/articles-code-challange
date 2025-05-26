from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

if __name__ == "__main__":
    # Create authors
    author1 = Author.create("Eddie")
    author2 = Author.create("Faith")

    # Create magazines
    mag1 = Magazine.create("Tech Weekly", "Technology")
    mag2 = Magazine.create("Science Digest", "Science")

    # Create articles
    article1 = Article.create("Understanding Python", author_id=author1.id, magazine_id=mag1.id)
    article2 = Article.create("AI in 2025", author_id=author1.id, magazine_id=mag1.id)
    article3 = Article.create("Quantum Basics", author_id=author2.id, magazine_id=mag2.id)

    print(" Created Articles:")
    print(article1)
    print(article2)
    print(article3)

    # Get by ID
    print(" Get article by ID:")
    found = Article.get_by_id(article1.id)
    print(found)

    # Get by title
    print(" Get article by title:")
    found_by_title = Article.get_by_title("AI in 2025")
    print(found_by_title)

    # Get all articles
    print(" All articles:")
    all_articles = Article.all()
    for art in all_articles:
        print(art)

    # Get articles by author
    print(" Articles by author Eddie:")
    eddie_articles = Article.articles_by_author(author1.id)
    for art in eddie_articles:
        print(art)

    # Get articles by magazine
    print("Articles in Tech Weekly:")
    tech_weekly_articles = Article.articles_by_magazine(mag1.id)
    for art in tech_weekly_articles:
        print(art)

    # Update article
    print(" Updating article title:")
    Article.update(article1.id, title="Understanding Advanced Python")
    updated = Article.get_by_id(article1.id)
    print("Updated:", updated)

    # Delete an article
    print(" Deleting an article:")
    Article.delete(article2.id)
    print(f"Deleted article with ID {article2.id}")

    # Show remaining articles
    print(" Remaining articles:")
    for art in Article.all():
        print(art)


