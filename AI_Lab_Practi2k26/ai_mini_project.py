
diseases = {
    "Flu": {"fever", "cough", "body_pain", "fatigue"},
    "Common Cold": {"cough", "runny_nose", "sneezing"},
    "Migraine": {"headache", "nausea", "light_sensitivity"},
    "Allergy": {"sneezing", "runny_nose", "itchy_eyes"},
    "Bronchitis": {"cough", "fatigue", "shortness_of_breath"}
}

def get_answer(question):
    while True:
        ans = input(question).lower().strip()

        if ans in ["yes", "y"]:
            return True
        elif ans in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")

def forward_chaining():

    print("\n=== FORWARD CHAINING ===")
    symptoms = set()

    all_symptoms = set()
    for s in diseases.values():
        all_symptoms.update(s)

    print("Please answer the following questions:")

    for symptom in sorted(all_symptoms):
        if get_answer(f"Do you have {symptom.replace('_', ' ')}? (yes/no): "):
            symptoms.add(symptom)

    print("\n=== POSSIBLE RESULTS ===")

    results = []

    for disease, required in diseases.items():
        matched = symptoms.intersection(required)
        missing = required - symptoms

        if matched:
            score = len(matched) / len(required) * 100
            results.append((disease, score, matched, missing))

    if results:
        results.sort(key=lambda x: x[1], reverse=True)

        for disease, score, matched, missing in results:
            print(f"\nDisease: {disease}")
            print(f"Match: {score:.0f}%")
            print("Matched symptoms:", matched)
            print("Missing symptoms:", missing)
    else:
        print("No matching symptoms found.")

def backward_chaining():

    print("\n=== BACKWARD CHAINING ===")

    disease = input("Enter disease name: ").strip().title()

    if disease not in diseases:
        print("Disease not found in knowledge base.")
        return

    print(f"\nChecking symptoms for {disease}:")

    matched = set()
    missing = set()

    for symptom in diseases[disease]:

        if get_answer(f"Do you have {symptom.replace('_', ' ')}? (yes/no): "):
            matched.add(symptom)
        else:
            missing.add(symptom)

    print("\n=== RESULT ===")
    print("Matched symptoms:", matched)
    print("Missing symptoms:", missing)

    if not missing:
        print(f"All required symptoms match {disease}.")
    else:
        print(f"{disease} could not be confirmed.")

while True:

    print("\n===== MEDICAL DIAGNOSIS SYSTEM =====")
    print("1. Forward Chaining")
    print("2. Backward Chaining")
    print("3. Show Knowledge Base")
    print("4. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        forward_chaining()

    elif choice == "2":
        backward_chaining()

    elif choice == "3":
        print("\n=== KNOWLEDGE BASE ===")

        for disease, symptoms in diseases.items():
            print(f"\n{disease}:")
            for symptom in sorted(symptoms):
                print("-", symptom.replace("_", " "))

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please select 1 to 4.")