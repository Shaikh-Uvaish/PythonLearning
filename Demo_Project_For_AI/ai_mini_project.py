diseases = {
    "Flu": {"fever", "cough", "body_pain", "fatigue"},
    "Common Cold": {"cough", "runny_nose", "sneezing"},
    "Migraine": {"headache", "nausea", "light_sensitivity"},
    "Allergy": {"sneezing", "runny_nose", "itchy_eyes"},
    "Bronchitis": {"cough", "fatigue", "shortness_of_breath"}
}

def forward_chaining():
    print("\n=== FORWARD CHAINING ===")

    symptoms = set()

    all_symptoms = set()
    for s in diseases.values():
        all_symptoms.update(s)

    for symptom in sorted(all_symptoms):
        ans = input(f"Do you have {symptom.replace('_',' ')}? (y/n): ").lower()

        if ans == "y":
            symptoms.add(symptom)

    found = False

    print("\nPossible Diagnosis:")

    for disease, req_symptoms in diseases.items():
        if req_symptoms.issubset(symptoms):
            print(f"\nDisease: {disease}")
            print("Matched Symptoms:")
            for s in req_symptoms:
                print("-", s.replace("_", " "))
            found = True

    if not found:
        print("No matching disease found.")

def backward_chaining():
    print("\n=== BACKWARD CHAINING ===")

    disease = input("Enter disease to verify: ").title()

    if disease not in diseases:
        print("Disease not found in knowledge base.")
        return

    print(f"\nChecking symptoms for {disease}")

    matched = True

    for symptom in diseases[disease]:
        ans = input(f"Do you have {symptom.replace('_',' ')}? (y/n): ").lower()

        if ans != "y":
            matched = False

    if matched:
        print(f"\nResult: {disease} is likely.")
    else:
        print(f"\nResult: {disease} cannot be confirmed.")

while True:

    print("\n===== MEDICAL DIAGNOSIS SYSTEM =====")
    print("1. Forward Chaining")
    print("2. Backward Chaining")
    print("3. Show Rules")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        forward_chaining()

    elif choice == "2":
        backward_chaining()

    elif choice == "3":
        print("\nKnowledge Base:\n")

        for disease, symptoms in diseases.items():
            print(f"{disease} -> {', '.join(symptoms)}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")