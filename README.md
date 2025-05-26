# articles-code-challange

A simple Python project to manage authors, magazines, and articles using SQLite. This project demonstrates basic CRUD operations, relationships, and querying with a focus on OOP and database integration.

## Features

- Create, read, update, and delete authors, magazines, and articles
- Query articles by author or magazine
- List contributors and topic areas
- SQLite database with schema and seed scripts

- Working code that correctly uses raw SQL queries within Python classes
- Proper database schema design with correct relationships
- SQL queries that are efficient and correct
- Transaction management and error handling
- Code organization and adherence to OOP principles
- Protection against SQL injection
- Test coverage of all SQL operations

## Project Structure
├── lib/ # Main code directory
│ ├── models/ # Model classes
│ │ ├── __init__.py # Makes models a package
│ │ ├── author.py # Author class with SQL methods
│ │ ├── article.py # Article class with SQL methods
│ │ └── magazine.py # Magazine class with SQL methods
│ ├── db/ # Database components
│ │ ├── __init__.py # Makes db a package
│ │ ├── connection.py # Database connection setup
│ │ ├── seed.py # Seed data for testing
│ │ └── schema.sql # SQL schema definitions
│ ├── controllers/ # Optional: Business logic
│ │ └── __init__.py # Makes controllers a package
│ ├── debug.py # Interactive debugging
│ └── __init__.py # Makes lib a package
├── tests/ # Test directory
│ ├── __init__.py # Makes tests a package
│ ├── test_author.py # Tests for Author class
│ ├── test_article.py # Tests for Article class
│ └── test_magazine.py # Tests for Magazine class
├── scripts/ # Helper scripts
│ ├── setup_db.py # Script to set up the database
│ └── run_queries.py # Script to run example queries
└── README.md # Project documentation


## Setup

1. **Install dependencies**  
   (No external packages required; uses Python 3.8+ and SQLite.)

2. **Initialize the database**
   ```sh
   python scripts/setup_db.py

Collecting workspace informationHere’s a README template for your project, based on your code and structure:

```md
# Articles Code Challenge

A simple Python project to manage authors, magazines, and articles using SQLite. This project demonstrates basic CRUD operations, relationships, and querying with a focus on OOP and database integration.

## Features

- Create, read, update, and delete authors, magazines, and articles
- Query articles by author or magazine
- List contributors and topic areas
- SQLite database with schema and seed scripts

## Project Structure

```
articles.db
lib/
  debug.py
  controllers/
  db/
    connection.py
    schema.sql
    seed.py
  models/
    article.py
    author.py
    magazine.py
scripts/
  run_queries.py
  setup_db.py
tests/
  test_article.py
  test_author.py
  test_magazine.py
```

## Setup

1. **Install dependencies**  
   (No external packages required; uses Python 3.8+ and SQLite.)

2. **Initialize the database**
   ```sh
   python scripts/setup_db.py
   ```

3. **Run the debug/demo script**
   ```sh
   python lib/debug.py
   ```

## Usage

- Use the models in `lib/models/` to interact with the database.
- See [`lib/debug.py`](lib/debug.py) for example usage and queries.

## Testing

- Add tests in the `tests/` directory.
- Run with your preferred test runner (e.g., `pytest`).

