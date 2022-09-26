def create_patient_entry(patient_first_name,
                         patient_last_name,
                         patient_id,
                         patient_age):
    new_patient = {"First Name": patient_first_name,
                   "Last Name": patient_last_name,
                   "Patient ID": patient_id,
                   "Age": patient_age,
                   "Tests": []}
    return new_patient


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def get_full_name(entry):
    return entry["First Name"] + " " + entry["Last Name"]


def print_db(db):
    for x in db.values():
        print("Name: {}, id: {}, age: {}, tests: {}".format(get_full_name(x),
                                                            x["Patient ID"],
                                                            x["Age"],
                                                            x["Tests"]))


def get_patient(db, id_no):
    return db[id_no]
    # return list(filter(lambda e: e[1] == id, db))


def add_test_result_to_patient(db, id, test_name, test_value):
    db[id]["Tests"].append((test_name, test_value))


def main():
    db = {}
    db[1] = create_patient_entry("John", "Smith", 1, 30)
    db[2] = create_patient_entry("Maggie", "Sills", 2, 23)
    db[3] = create_patient_entry("Chase", "Morell", 3, 30)
    db[4] = create_patient_entry("Mark", "Smith", 4, 50)
    db[5] = create_patient_entry("Scott", "Morell", 5, 23)

    print_db(db)
    # print(getPatient(db,9))
    add_test_result_to_patient(db, 1, "height", "6")
    print_db(db)
    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])))


if __name__ == "__main__":
    main()
