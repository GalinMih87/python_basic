total_tickets_counter = 0
student_tickets_counter = 0
standard_tickets_counter = 0
kids_tickets_counter = 0
command = input()

while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places = free_places
    while free_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standard_tickets_counter += 1
        elif ticket_type == "kid":
            kids_tickets_counter += 1
        free_places -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    precent_full_hall = sold_tickets / total_places * 100
    print(f"{movie_name} - {precent_full_hall:.2f}% full.")

    command = input()
student_precent = student_tickets_counter / total_tickets_counter * 100
standard_precent = standard_tickets_counter / total_tickets_counter * 100
kids_precent = kids_tickets_counter / total_tickets_counter * 100
print(f"Total tickets: {total_tickets_counter}")
print(f"{student_precent:.2f}% student tickets.")
print(f"{standard_precent:.2f}% standard tickets.")
print(f"{kids_precent:.2f}% kids tickets.")