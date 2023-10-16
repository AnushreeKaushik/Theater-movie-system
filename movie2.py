print(".................Theater ticket booking syatem.............")
total_seats = 50
normal_seat_price = 100
recliner_seat_price = 150
combo_price = 50


seats_available = total_seats
total_cost = 0

# Main loop.........
while seats_available > 0:
    print(f"Seats available: {seats_available}")
    seat_type = input("Select seat type (Normal/Recliner): ").strip().lower()

    if seat_type == "normal":
        seat_price = normal_seat_price
    elif seat_type == "recliner":
        seat_price = recliner_seat_price
    else:
        print("Invalid seat type. Please choose Normal or Recliner.")
        continue


    num_tickets = int(input(f"Enter the number of {seat_type} tickets: "))
    if num_tickets > seats_available:
        print(f"Sorry, only {seats_available} {seat_type} seats available.")
        continue

    total_cost += seat_price * num_tickets
    seats_available -= num_tickets

    #.......Add combos.......
    add_combo = input("Do you want to add combos? (yes/no): ")
    if add_combo == "yes":
        num_combos = int(input("Enter the number of combos: "))
        total_cost += combo_price * num_combos

    print(f"Total cost for {num_tickets} {seat_type} ticket(s): ${total_cost}")
    print("Enjoy the show!")



    go_next = input("Go to the next person? (yes/no): ")
    if go_next == "no":
        break

print("Thank you for using the ticket booking system!")