from collections import defaultdict, Counter

# Sample borrowing record: member_id -> list of book_ids borrowed
borrowing_records = {
    'M001': ['B1', 'B2'],
    'M002': ['B2', 'B3', 'B1'],
    'M003': [],
    'M004': ['B2'],
    'M005': ['B3'],
    'M006': [],
    'M007': ['B1', 'B3', 'B2', 'B2'],
}

def compute_average_books(records):
    total_books = sum(len(books) for books in records.values())
    num_members = len(records)
    average = total_books / num_members
    return average

def book_borrowing_stats(records):
    book_counter = Counter()
    for books in records.values():
        book_counter.update(books)

    most_borrowed = book_counter.most_common(1)[0]
    least_borrowed = min(book_counter.items(), key=lambda x: x[1])

    return most_borrowed, least_borrowed, dict(book_counter)

def count_inactive_members(records):
    return sum(1 for books in records.values() if len(books) == 0)

def display_results():
    print("Library Borrowing Records Analysis\n")

    # 1. Average books borrowed
    avg = compute_average_books(borrowing_records)
    print(f"1. Average number of books borrowed per member: {avg:.2f}")

    # 2. Highest and Lowest borrowed books
    most, least, full_stats = book_borrowing_stats(borrowing_records)
    print(f"2. Most borrowed book: {most[0]} (Borrowed {most[1]} times)")
    print(f"   Least borrowed book: {least[0]} (Borrowed {least[1]} times)")

    # 3. Inactive members
    inactive_count = count_inactive_members(borrowing_records)
    print(f"3. Number of members who did not borrow any books: {inactive_count}")

    # 4. Frequency of each book
    print("4. Frequency of all borrowed books:")
    for book, count in full_stats.items():
        print(f"   {book}: {count} times")

if __name__ == "__main__":
    display_results()