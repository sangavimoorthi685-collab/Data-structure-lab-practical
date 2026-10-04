def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]

    left = [x for x in bookings[1:]
            if x[1].lower() <= pivot[1].lower()]

    right = [x for x in bookings[1:]
             if x[1].lower() > pivot[1].lower()]

    return quick_sort(left) + [pivot] + quick_sort(right)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    ticket = int(input("Enter ticket ID: "))
    movie = input("Enter movie name: ")
    seat = input("Enter seat number: ")

    bookings.append((ticket, movie, seat))

result = quick_sort(bookings)

print("\nSorted Movie Bookings:")

for ticket, movie, seat in result:
    print(ticket, movie, seat)