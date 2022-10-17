def create_patient_entry(patient_name, patient_id, patient_age):
    newPatient = [patient_name, patient_id, patient_age, []]
    return newPatient


def printDB(db):
    for x in db:
        print("Name: {}, id: {}, age: {}, tests: {}".format(x[0], x[1], x[2], x[3]))


def getPatient(db, id):
    return list(filter(lambda e: e[1] == id, db))


def addTestResultToPatient(db, id, test_name, test_value):
    for index, i in enumerate(db):
        if i[1] == id:
            db[index][3].append((test_name, test_value))


def main():
    db = []
    db.append(create_patient_entry("John Smith", 1, 30))
    db.append(create_patient_entry("Maggie", 2, 23))
    db.append(create_patient_entry("Chase", 3, 30))
    db.append(create_patient_entry("Mark", 4, 50))
    db.append(create_patient_entry("Scott", 5, 23))

    printDB(db)
    print(getPatient(db, 9))
    addTestResultToPatient(db, 1, "height", "6")
    printDB(db)


if __name__ == "__main__":
    main()
