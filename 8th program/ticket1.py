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
    bookings.append((ticket, name))

result = quick_sort(bookings)

print("\nSorted Booking Details:")
for ticket, name in result:
    print(ticket, name)