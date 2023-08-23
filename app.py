from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated in-memory database tables
departments = {
    10: "Admin",
    20: "Accounts",
    30: "Sales",
    40: "Marketing",
    50: "Purchasing",
}

employees = {
    1: {"ENAME": "Amal", "DNO": 10, "SALARY": 30000},
    2: {"ENAME": "Shyamal", "DNO": 30, "SALARY": 50000},
    3: {"ENAME": "Kamal", "DNO": 40, "SALARY": 10000},
    4: {"ENAME": "Nirmal", "DNO": 50, "SALARY": 60000},
    5: {"ENAME": "Bimal", "DNO": 20, "SALARY": 40000},
    6: {"ENAME": "Parimal", "DNO": 10, "SALARY": 20000},
}


# routes
@app.route("/api", methods=["GET"])
def get_employee_by_eno():
    eno = request.args.get("ENO", type=int)
    employee = employees.get(eno)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404


@app.route("/api/employees_by_department", methods=["GET"])
def get_employees_by_department():
    dname = request.args.get("DNAME")
    department_employees = []
    for eno, employee in employees.items():
        department = departments.get(employee["DNO"])
        if department == dname:
            department_employees.append(employee)
    return jsonify(department_employees)


if __name__ == "__main__":
    app.run(host="localhost", port=9000)
