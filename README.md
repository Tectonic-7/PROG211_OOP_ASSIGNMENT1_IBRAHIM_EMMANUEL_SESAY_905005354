# Clinic Management System

A simple Python program that demonstrates basic Object-Oriented Programming (OOP) through a clinic billing system.

## Student Information

- **Name:** Ibrahim E. Sesay
- **Student ID:** 905005354
- **Course:** PROG211 – Object-Oriented Programming I
- **Institution:** Limkokwing University, Sierra Leone Campus

## Project Overview

The program allows a user to enter fictional patient ages and treatment costs, calculate bills, and display records.

It uses a fixed consultation fee of **$50.00**. Each total bill is calculated as:

**Total bill = consultation fee + treatment cost**

The program also indicates whether the total bill is above $100 or at or below $100. This is a billing category, not a measure of medical severity.

## Features

- Add a patient billing record.
- Generate a patient reference such as `P001`.
- Calculate the total bill.
- Display all records.
- Display the number of records entered.
- Reject invalid ages and treatment costs.
- Provide a simple menu.

## OOP Concepts Demonstrated

### Classes and Objects

The program contains two classes:

- **PatientRecord:** Stores a patient's reference, age, treatment cost, total bill, and billing status.
- **Clinic:** Stores and manages PatientRecord objects.

The classes interact when a PatientRecord object is added to a Clinic object.

### Attributes

PatientRecord attributes include:

- `patient_id`
- `age`
- `treatment_cost`
- `total_bill`
- `status`

Clinic attributes include:

- `clinic_name`
- `patient_records`

### Instance Methods

Instance methods work with individual objects.

Examples include:

- `calculate_total_bill()`
- `get_case_status()`
- `display_record()`
- `add_record()`
- `display_records()`
- `record_count()`

### Class Method

`create_record()` uses `@classmethod` to create a PatientRecord object through the class.

### Static Method

`validate_details()` uses `@staticmethod` to check ages and treatment costs without requiring an existing object.

### Collection

The program uses one list, `patient_records`, to store multiple PatientRecord objects.

### Functions

- `add_patient_record()` collects input, creates a record, and adds it to the clinic.
- `display_patient_records()` displays the stored records.
- `main()` controls the menu and program flow.

## Requirements

- Python 3
- A terminal or an editor such as Visual Studio Code

No additional Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the folder containing the program.
3. Run:

```bash
python Clinic_management_system_modified.py
```

On Windows, you can also use:

```bash
py Clinic_management_system_modified.py
```

## How to Use

Choose an option from the menu:

```text
1. Add patient billing record
2. Display all records
3. Exit
```

For option 1, enter a fictional patient's age and treatment cost. Use option 2 to view the records entered during the session. Use option 3 to close the program.

## Sample Input and Output

Example inputs:

```text
Choose an option (1-3): 1
Enter the patient's age in years: 25
Enter the treatment cost (le): 75
```

Output for the first record in a new session:

```text
Record added successfully.
Patient reference: P001
Patient age: 25
Consultation fee: le50.00
Treatment cost: le75.00
Total bill: le125.00
Billing threshold status: Above le2400 billing threshold
```

Choosing option 2 displays all stored records and the total number of records in the session.

## Input Validation

The program checks that:

- Age is a whole number between 0 and 120.
- Treatment cost is a finite, non-negative number.
- The calculated total bill remains finite.
- Menu choices are valid.
- Only PatientRecord objects are added to the clinic.
- The same record object is not added twice.

## Digital Public Good Principles

This educational project follows several principles relevant to digital public goods.

### Open Source

Publishing the code on GitHub makes it available for inspection and learning. A separate open-source licence should be included to specify how others may use, modify, and share the code.

### Privacy

The program does not request names, addresses, phone numbers, or medical histories. Users should enter fictional ages and costs only.

Records are stored in memory and are discarded when the program closes.

### Accessibility and Inclusion

The program uses a text menu with clear instructions and error messages. It does not require an internet connection once downloaded.

The current version requires users to understand English and operate a terminal. Translations and additional accessibility improvements could be added later.

### Reusability

The PatientRecord and Clinic classes separate record details from clinic management. This makes the code easier to understand and adapt for similar educational projects.

These design choices do not constitute official certification as a digital public good.

## Limitations

- Records are not saved to a file or database.
- Records cannot be edited or deleted through the menu.
- The consultation fee is fixed.
- All amounts are displayed in US dollars.
- The program is an educational billing demonstration and is not intended for real clinical use.

## Possible Future Improvements

- Save fictional records to a file.
- Add options to edit or delete records.
- Allow the consultation fee to be changed.
- Support additional currencies and languages.

## Licence

Add a `LICENSE` file to this repository before describing the project as licensed open-source software. The MIT License is one possible choice.
