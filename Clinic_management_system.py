"""
Clinic Management System

"""

from math import isfinite

CONSULTATION_FEE = 50.00


class PatientRecord:
    """Represents one anonymous clinic billing record."""

    consultation_fee = CONSULTATION_FEE
    records_created = 0

    def __init__(self, age, treatment_cost):
        self.validate_details(age, treatment_cost)
        PatientRecord.records_created += 1
        self.patient_id = f"P{PatientRecord.records_created:03d}"
        self.age = age
        self.treatment_cost = treatment_cost
        self.total_bill = self.calculate_total_bill()
        self.status = self.get_case_status()

    def calculate_total_bill(self):
        """Instance method: calculate consultation fee plus treatment."""
        return self.consultation_fee + self.treatment_cost

    def get_case_status(self):
        """Classify billing amounts, not medical severity."""
        if self.total_bill > 2400:
            return "Above Le2,400 billing threshold"
        return "At or below Le2,400 billing threshold"

    def display_record(self):
        """Display this record without exposing a patient's name."""
        print(f"Patient reference: {self.patient_id}")
        print(f"Patient age: {self.age}")
        print(f"Consultation fee: Le{self.consultation_fee:.2f}")
        print(f"Treatment cost: Le{self.treatment_cost:.2f}")
        print(f"Total bill: Le{self.total_bill:.2f}")
        print(f"Billing threshold status: {self.status}")

    @staticmethod
    def validate_details(age, treatment_cost):
        """Static method: validate fictional demo values without an object."""
        if isinstance(age, bool) or not isinstance(age, int) or not 0 <= age <= 120:
            raise ValueError("Age must be a whole number between 0 and 120.")
        if (isinstance(treatment_cost, bool)
                or not isinstance(treatment_cost, (int, float))
                or not isfinite(treatment_cost)
                or treatment_cost < 0
                or not isfinite(CONSULTATION_FEE + treatment_cost)):
            raise ValueError("Treatment cost must be a finite, non-negative number.")

    @classmethod
    def create_record(cls, age, treatment_cost):
        """Class method: create a record through the class."""
        return cls(age, treatment_cost)


class Clinic:
    """Manages clinic records using one list of PatientRecord objects."""

    def __init__(self, clinic_name):
        self.clinic_name = clinic_name
        self.patient_records = []

    def add_record(self, patient_record):
        """Store a PatientRecord object in the clinic's list."""
        if not isinstance(patient_record, PatientRecord):
            raise TypeError("Only PatientRecord objects can be added.")
        if patient_record in self.patient_records:
            raise ValueError("This record has already been added.")
        self.patient_records.append(patient_record)

    def display_records(self):
        """Display all records currently stored in this session."""
        print(f"\n--- {self.clinic_name}: Patient Billing Records ---")

        if not self.patient_records:
            print("No records have been entered yet.")
            return

        for record in self.patient_records:
            print()
            record.display_record()

    def record_count(self):
        """Return the number of records in this session."""
        return len(self.patient_records)


def add_patient_record(clinic):
    """Collect input, validate it, create a record, and store it."""
    

    while True:
        try:
            age = int(input("Enter the patient's age in years: "))

            if age < 0 or age > 120:
                print("Please enter an age between 0 and 120.")
                continue

            treatment_cost = float(
                input("Enter the treatment cost (le): ")
            )

            PatientRecord.validate_details(age, treatment_cost)

            break

        except ValueError as error:
            print(f"Invalid input: {error}")

    record = PatientRecord.create_record(age, treatment_cost)
    clinic.add_record(record)

    print("\nRecord added successfully.")
    record.display_record()


def display_patient_records(clinic):
    """Display all stored patient billing records."""
    clinic.display_records()


def main():
    clinic = Clinic("Community Clinic")

    print("===================================")
    print("       CLINIC MANAGEMENT SYSTEM")
    print("===================================")
    

    while True:
        print("\nMenu")
        print("1. Add patient billing record")
        print("2. Display all records")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_patient_record(clinic)

        elif choice == "2":
            display_patient_records(clinic)
            print(
                f"\nTotal records in this session: "
                f"{clinic.record_count()}"
            )

        elif choice == "3":
            print(
                f"Program ended. {clinic.record_count()} "
                f"record(s) were entered."
            )
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed. Session records are discarded.")