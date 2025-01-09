# program to: Create a class hierarchy for employees, with a base class and
# subclasses for full-time, part-time, and contractor employees.
# Include shared attributes like name, ID, and salary calculation in
# the base class. Each subclass should calculate the salary based
# on its type (full-time, part-time, contractor). Apply tax deductions
# (e.g., 10%) and Provident Fund (PF) deductions (e.g., 12%) for
# full-time and part-time employees. For contractors, apply only the
# tax deduction and no PF. The final salary after deductions should
# be returned for each employee type.


class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        tax = self.base_salary * 0.10  # 10% tax deduction
        pf = self.base_salary * 0.12  # 12% PF deduction
        net_salary = self.base_salary - tax - pf
        return net_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        tax = self.base_salary * 0.10  # 10% tax deduction
        pf = self.base_salary * 0.12  # 12% PF deduction
        net_salary = self.base_salary - tax - pf
        return net_salary

class ContractorEmployee(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        tax = self.base_salary * 0.10  # 10% tax deduction
        net_salary = self.base_salary - tax
        return net_salary
        
if __name__ == "__main__":
    full_time = FullTimeEmployee("John Doe", 101, 50000)
    part_time = PartTimeEmployee("Jane Doe", 102, 20000)
    contractor = ContractorEmployee("Mark Smith", 103, 30000)

    print(f"{full_time.name}'s salary: ₹{full_time.calculate_salary():.2f}")
    print(f"{part_time.name}'s salary: ₹{part_time.calculate_salary():.2f}")
    print(f"{contractor.name}'s salary: ₹{contractor.calculate_salary():.2f}")
