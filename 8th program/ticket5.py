def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]
    left = [x for x in bookings[1:] if x[2] <= pivot[2]]
    right = [x for x in bookings[1:] if x[2] > pivot[2]]

    return quick_sort(left) + [pivot] + quick_sort(right)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    ticket = int(input("Enter ticket ID: "))
    name = input("Enter customer name: ")
    price = int(input("Enter ticket price: "))
    bookings.append((ticket, name, price))

result = quick_sort(bookings)

print("\nBookings Sorted by Price:")
for ticket, name, price in result:
    print(ticket, name, price)