import csv
import cv2
import qrcode
from pyzbar.pyzbar import decode
from datetime import datetime

# ==================== Initial Setup ====================
# Define 5 employees
employees = {
    "E001": {"name": "Alice"},
    "E002": {"name": "Bob"},
    "E003": {"name": "Charlie"},
    "E004": {"name": "David"},
    "E005": {"name": "Eva"}
}

log_file = "attendance_log.csv"

# Create CSV file if it doesn't exist
def initialize_log():
    try:
        with open(log_file, "x", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Year", "Employee ID", "Name", "Status"])
    except FileExistsError:
        pass

# ==================== QR Code Generation ====================
def generate_qr_codes():
    for emp_id in employees:
        img = qrcode.make(emp_id)
        img.save(f"{emp_id}.png")
    print("✅ QR Codes generated for all employees.")

# ==================== QR Scan & Attendance ====================
def scan_qr_and_mark_attendance():
    print("📷 Starting QR Scanner... Press 'q' to stop.\n")
    cap = cv2.VideoCapture(0)
    today = datetime.now().strftime("%Y-%m-%d")
    year = datetime.now().year
    marked = set()

    while True:
        success, frame = cap.read()
        for barcode in decode(frame):
            emp_id = barcode.data.decode("utf-8")
            if emp_id in employees and emp_id not in marked:
                name = employees[emp_id]["name"]
                print(f"✅ {name} ({emp_id}) marked present.")
                with open(log_file, "a", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([today, year, emp_id, name, "Present"])
                marked.add(emp_id)

        cv2.imshow("QR Scanner - Press 'q' to exit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("📴 QR Scanning Ended.\n")

# ==================== Attendance Search ====================
def search_attendance():
    emp_id = input("Enter Employee ID (e.g., E001): ")
    year = input("Enter Year (e.g., 2025): ")
    date = input("Enter Date (YYYY-MM-DD): ")
    found = False

    with open(log_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Employee ID"] == emp_id and row["Date"] == date and row["Year"] == year:
                print(f"📌 {row['Name']} was {row['Status']} on {row['Date']}")
                found = True
                break
    if not found:
        print("❌ No attendance record found.\n")

# ==================== Utility Functions ====================
def view_all_employees():
    print("\n📋 Employee List:")
    for emp_id, info in employees.items():
        print(f"ID: {emp_id}, Name: {info['name']}")
    print()

def view_full_log():
    print("\n🗂 Attendance Log:")
    with open(log_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
    print()

# ==================== Main Menu ====================
initialize_log()

while True:
    print("\n====== QR Attendance System ======")
    print("1. Generate QR Codes")
    print("2. Mark Attendance (QR Scan)")
    print("3. View All Employees")
    print("4. Search Attendance (By Date & Year)")
    print("5. View Full Attendance Log")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        generate_qr_codes()
    elif choice == "2":
        scan_qr_and_mark_attendance()
    elif choice == "3":
        view_all_employees()
    elif choice == "4":
        search_attendance()
    elif choice == "5":
        view_full_log()
    elif choice == "6":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("⚠ Invalid choice! Please enter 1 to 6.\n")