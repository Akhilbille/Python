import emp, pickle

with open("data.txt", "rb") as f:
    # pickle.dump(emp.emp1, f)
    emp.emp1 = pickle.load(f)
