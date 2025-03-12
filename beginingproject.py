# HOSPITAL BILLING:

def calculate_total_bill():
    # User input for hospital stay
    room_charge_per_day = float(input("Enter the daily room charge : "))
    days_in_hospital = int(input("Enter the number of days the patient stayed in the hospital: "))
    
    # User input for doctor visits
    doctor_fee_per_visit = float(input("Enter the doctor fee per visit : "))
    doctor_visits = int(input("Enter the number of doctor visits: "))
    
    # User input for medication costs
    medication_cost = float(input("Enter the total medication cost: "))
    
    # User input for surgery charges (if applicable)
    surgery_needed = input("Did the patient undergo surgery? (yes/no): ").strip().lower()
    if surgery_needed == "yes":
        surgery_cost = float(input("Enter the surgery cost (in USD): "))
    else:
        surgery_cost = 0
    
    # Calculate the charges
    room_charge = room_charge_per_day * days_in_hospital
    doctor_charge = doctor_fee_per_visit * doctor_visits
    
    # Total bill calculation
    total_bill = room_charge + doctor_charge + medication_cost + surgery_cost
    
    # Display the breakdown of charges
    print("\nHospital Billing Summary:")
    print(f"Room Charge for {days_in_hospital} days: {room_charge:.2f}")
    print(f"Doctor Consultation Fee for {doctor_visits} visits: {doctor_charge:.2f}")
    print(f"Medication Cost: {medication_cost:.2f}")
    print(f"Surgery Cost: {surgery_cost:.2f}")
    print(f"\nTotal Bill: {total_bill:.2f}")

# Call the function to run the program
calculate_total_bill()
