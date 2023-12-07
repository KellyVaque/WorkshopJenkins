import datetime

books = {
    1: {"title": "Book 1", "author": "Author 1", "availability": 5},
    2: {"title": "Book 2", "author": "Author 2", "availability": 3},
    3: {"title": "Book 3", "author": "Author 3", "availability": 7},
    4: {"title": "Book 4", "author": "Author 4", "availability": 2},
    # Añade más libros según sea necesario
}

checked_out_books = {}
late_fee_rate = 1  # $1 de tarifa por día de retraso

def display_catalog():
    print("Catálogo de la biblioteca:")
    for book_id, details in books.items():
        print(f"{book_id}. {details['title']} by {details['author']} - Disponibles: {details['availability']}")

def checkout_books():
    total_books = 0
    while True:
        try:
            book_id = int(input("Ingrese el ID del libro para el préstamo (0 para finalizar): "))
            if book_id == 0:
                break

            if book_id not in books:
                print("ID de libro no válido. Por favor, seleccione un ID de libro válido.")
                continue

            quantity = int(input("Ingrese la cantidad: "))
            if quantity <= 0 or quantity > 10:
                print("Cantidad no válida. Por favor, ingrese un número positivo entre 1 y 10.")
                continue

            if books[book_id]["availability"] >= quantity:
                if total_books + quantity <= 10:
                    checked_out_books[book_id] = {"quantity": quantity}
                    books[book_id]["availability"] -= quantity
                    total_books += quantity
                else:
                    print("No se pueden prestar más de 10 libros en una transacción. Por favor, seleccione menos libros.")
            else:
                print("Cantidad no disponible. Por favor, seleccione una cantidad menor o igual a la disponible.")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

    if total_books == 0:
        return -1

    confirm_checkout()

def confirm_checkout():
    print("\nLibros seleccionados para el préstamo:")
    total_due_date = datetime.date.today() + datetime.timedelta(days=14)
    total_late_fee = 0

    for book_id, details in checked_out_books.items():
        due_date = total_due_date.strftime("%Y-%m-%d")
        late_fee = 0
        checked_out_books[book_id]["due_date"] = due_date

        print(f"Libro: {books[book_id]['title']}, Cantidad: {details['quantity']}, Fecha de devolución: {due_date}")

        # Calcular tarifa por retraso
        days_late = (datetime.date.today() - total_due_date).days
        if days_late > 0:
            late_fee = days_late * late_fee_rate
            total_late_fee += late_fee
            print(f"Tarifa por retraso: ${late_fee}")

    print("\nTarifa total por retraso: ${}".format(total_late_fee))
    confirmation = input("¿Desea confirmar el préstamo? (sí/no): ").lower()

    if confirmation == "si":
        print("¡Préstamo exitoso!")
    else:
        # Deshacer cambios
        for book_id, details in checked_out_books.items():
            books[book_id]["availability"] += details["quantity"]
        print("Préstamo cancelado.")

def return_books():
    total_late_fee = 0
    while True:
        try:
            book_id = int(input("Ingrese el ID del libro para la devolución (0 para finalizar): "))
            if book_id == 0:
                break

            if book_id in checked_out_books:
                days_late = (datetime.date.today() - datetime.datetime.strptime(
                    checked_out_books[book_id]["due_date"], "%Y-%m-%d").date()).days
                late_fee = max(0, days_late * late_fee_rate)
                total_late_fee += late_fee
                books[book_id]["availability"] += checked_out_books[book_id]["quantity"]
                del checked_out_books[book_id]
                print(f"Libro devuelto con éxito. Tarifa por retraso: ${late_fee}")

            else:
                print("Libro no encontrado en los libros prestados.")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

    print("\nTarifa total por libros devueltos con retraso: ${}".format(total_late_fee))

def run_library_system():
    while True:
        print("\nSistema de préstamo de libros de la biblioteca")
        print("1. Mostrar catálogo")
        print("2. Prestar libros")
        print("3. Devolver libros")
        print("0. Salir")
        choice = input("Ingrese su elección: ")

        if choice == "1":
            display_catalog()
        elif choice == "2":
            checkout_books()
        elif choice == "3":
            return_books()
        elif choice == "0":
            print("Saliendo del sistema de la biblioteca. ¡Adiós!")
            break
        else:
            print("Elección no válida. Por favor, ingrese una opción válida.")

# Ejecutar el sistema
run_library_system()
