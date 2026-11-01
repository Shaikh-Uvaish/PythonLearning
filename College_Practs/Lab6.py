class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_student = Student(roll, name, marks)
        if self.head is None:
            self.head = new_student
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_student
        print(f"\n Student record added successfully for Roll No: {roll}")

    def display_students(self):
        if self.head is None:
            print("\n No records found.")
            return
        print("\n--- Student Records ---")
        temp = self.head
        while temp:
            print(f"Roll No: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"\n Student Found -> Roll No: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return temp
            temp = temp.next
        print("\n Student not found.")
        return None

    def delete_student(self, roll):
        if self.head is None:
            print("\n No records to delete.")
            return

        if self.head.roll == roll:
            self.head = self.head.next
            print(f"\n Record with Roll No: {roll} deleted successfully.")
            return

        prev = None
        temp = self.head
        while temp and temp.roll != roll:
            prev = temp
            temp = temp.next

        if temp is None:
            print("\n Record not found.")
        else:
            prev.next = temp.next
            print(f"\n Record with Roll No: {roll} deleted successfully.")

    def update_student(self, roll, new_name, new_marks):
        temp = self.search_student(roll)
        if temp:
            temp.name = new_name
            temp.marks = new_marks
            print("\n Record updated successfully!")

    def sort_students(self, key="roll", order="asc"):
        if self.head is None or self.head.next is None:
            print("\n Not enough records to sort.")
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                first = getattr(temp, key)
                second = getattr(temp.next, key)
                condition = first > second if order == "asc" else first < second

                if condition:
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        print(f"\n Records sorted by {key} in {order.upper()} order successfully!")



def main():
    system = StudentLinkedList()

    while True:
        print("\n========= Student Record Management System =========")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student Record")
        print("4. Delete Student Record")
        print("5. Update Student Record")
        print("6. Sort Records")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            roll = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            system.add_student(roll, name, marks)

        elif choice == '2':
            system.display_students()

        elif choice == '3':
            roll = int(input("Enter Roll Number to search: "))
            system.search_student(roll)

        elif choice == '4':
            roll = int(input("Enter Roll Number to delete: "))
            system.delete_student(roll)

        elif choice == '5':
            roll = int(input("Enter Roll Number to update: "))
            name = input("Enter new Name: ")
            marks = float(input("Enter new Marks: "))
            system.update_student(roll, name, marks)

        elif choice == '6':
            print("\nSort by: 1. Roll Number  2. Marks")
            opt = input("Enter choice (1/2): ")
            key = "roll" if opt == '1' else "marks"
            order = input("Order (asc/desc): ").lower()
            system.sort_students(key, order)

        elif choice == '7':
            print("\n Exiting... Thank you for using the system!")
            break

        else:
            print("\n Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
