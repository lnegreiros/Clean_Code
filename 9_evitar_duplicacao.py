def print_payment_info(employee):
    print(f"Pagando {employee.name}")
    print(f"Transferindo R${employee.salary} para conta {employee.bank_account}")

def pay_employee(employee):
    print_payment_info(employee)