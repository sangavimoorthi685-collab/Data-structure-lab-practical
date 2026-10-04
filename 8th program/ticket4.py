def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]

    left = [x for x in bookings[1:] if x[0] <= pivot[0]]
    right = [x for x in bookings[1:] if x[0] > pivot[0]]

    return quick_sort(left) + [pivot] + quick_sort(right)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    ticket = int(input("Enter ticket ID: "))
    name = input("Enter customer name: ")
    movie = input("Enter movie name: ")
    price = int(input("Enter ticket price: "))

    bookings.append((ticket, name, movie, price))

result = quick_sort(bookings)

print("\nMovie Ticket Booking Details:")

for ticket, name, movie, price in result:
    print("Ticket:", ticket)
    print("Customer:", name)
    print("Movie:", movie)
    print("Price:", price)
    print()