class StudentRecord:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def read_records(file_name):
    records = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, age = line.strip().split()
                records.append(StudentRecord(name, int(age)))
    except FileNotFoundError:
        print("Error: File not found.")
    return records

def sort_records(records):
    return sorted(records, key=lambda x: x.name)

def display_records(records):
    print("Student records sorted by name:")
    for record in records:
        print(f"Name: {record.name}, Age: {record.age}")

def main():
    file_name = input("Enter the name of the file containing student records: ")
    records = read_records(file_name)
    if records:
        sorted_records = sort_records(records)
        display_records(sorted_records)

if __name__ == "__main__":
    main()