import datetime
from librarysystem.py import calculate_due_date, calculate_late_fee, display_book_catalog

def test_calculate_due_date():
    today = datetime.date.today()
    due_date = calculate_due_date()
    assert due_date == today + datetime.timedelta(days=14)

def test_calculate_late_fee():
    assert calculate_late_fee(0) == 0
    assert calculate_late_fee(5) == 5
    assert calculate_late_fee(0, rate=2) == 0
    assert calculate_late_fee(5, rate=2) == 10

def test_display_book_catalog(capsys):
    books = {
        1: {"title": "Book 1", "author": "Author 1", "availability": 5},
        2: {"title": "Book 2", "author": "Author 2", "availability": 3},
    }
    display_book_catalog(books)
    captured = capsys.readouterr()
    assert "Catálogo de la biblioteca:" in captured.out
    assert "Book 1 by Author 1 - Disponibles: 5" in captured.out
    assert "Book 2 by Author 2 - Disponibles: 3" in captured.out