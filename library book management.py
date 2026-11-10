# Application 3: Library Book Management
books = {
    "Python Programming": "Available",
    "Data Structures": "Issued",
    "Database Systems": "Available",
    "Computer Networks": "Available"
}
print("--- LIBRARY BOOK CATALOGUE ---")
for title, status in books.items():
    print(title, ":", status)
search_title = input("\nEnter book title to search: ")
if search_title in books:
    print("Book Status:", books[search_title])
else:
    print("Book not found.")
update_title = input("\nEnter book title to update: ")

if update_title in books:
    new_status = input("Enter status (Available/Issued): ")
    if new_status.lower() in ("available", "issued"):
        books[update_title] = new_status.capitalize()
        print("Book status updated successfully.")
    else:
        print("Invalid status. Enter Available or Issued.")
else:
    print("Book not found.")
print("\n--- UPDATED LIBRARY CATALOGUE ---")
for title, status in books.items():
    print(title, ":", status)
