import json

def save_data(students, courses, filename="data.json"):
    # Save all student and course data to a JSON file
    data = {
        "students": [s.__dict__ for s in students],
        "courses": [c.__dict__ for c in courses]
    }
    with open(filename, "w") as file:
        json.dump(data, file)
    print("Data saved successfully.")

def load_data(filename="data.json"):
    # Load student and course data from JSON file
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found.")
        return None