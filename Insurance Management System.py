class Transaction:
    def __init__(self, transaction_id, amount, user):
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__user = user

    def get_transaction_id(self):
        return self.__transaction_id

    def get_amount(self):
        return self.__amount

    def get_user(self):
        return self.__user

    def set_amount(self, amount):
        self.__amount = amount

    def process(self):
        print(f"Processing transaction ID {self.__transaction_id} for {self.__user.get_name()} with amount {self.__amount}.")


class User:
    def __init__(self, user_id, name, role, password):
        self.__user_id = user_id
        self.__name = name
        self.__role = role
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def verify_password(self, password):
        return self.__password == password

    def set_name(self, new_name):
        self.__name = new_name


class Admin(User):
    def generate_report(self, report_type):
        print(f"Generating {report_type} report.")


class Customer(User):
    def view_policy_details(self, policies):
        customer_policies = [p for p in policies if p.get_owner() == self.get_user_id()]
        if not customer_policies:
            print("No policies found for this customer.")
        else:
            for policy in customer_policies:
                policy.display_policy_details()


class Agent(User):
    def __init__(self, user_id, name, role, password, agent_id, commission):
        super().__init__(user_id, name, role, password)
        self.__agent_id = agent_id
        self.__commission = commission

    def sell_policy(self, policy):
        print(f"Selling policy {policy.get_policy_id()}.")

    def get_commission(self):
        return self.__commission


class ClaimAdjuster(Agent):
    def investigate_claim(self, claim):
        print(f"Investigating claim ID {claim.get_claim_id()}.")


class Underwriter(Agent):
    def specialize_in_risk(self):
        print(f"Specializing in risk assessment.")


class Policy:
    def __init__(self, policy_id, policy_type, premium, owner):
        self.__policy_id = policy_id
        self.__policy_type = policy_type
        self.__premium = premium
        self.__owner = owner

    def get_policy_id(self):
        return self.__policy_id

    def get_policy_type(self):
        return self.__policy_type

    def get_premium(self):
        return self.__premium

    def get_owner(self):
        return self.__owner

    def set_premium(self, new_premium):
        self.__premium = new_premium

    def display_policy_details(self):
        print(f"Policy ID: {self.__policy_id}, Type: {self.__policy_type}, Premium: {self.__premium}, Owner: {self.__owner}")


class Claim(Transaction):
    def __init__(self, transaction_id, amount, user, claim_id, claim_amount, status="Pending"):
        super().__init__(transaction_id, amount, user)
        self.__claim_id = claim_id
        self.__claim_amount = claim_amount
        self.__status = status

    def get_claim_id(self):
        return self.__claim_id

    def get_claim_amount(self):
        return self.__claim_amount

    def get_status(self):
        return self.__status

    def update_status(self, new_status):
        self.__status = new_status
        print(f"Claim {self.__claim_id} status updated to {self.__status}.")

    def display_claim_details(self):
        print(f"Claim ID: {self.__claim_id}, Amount: {self.__claim_amount}, Status: {self.__status}")


class Payment(Transaction):
    def __init__(self, transaction_id, amount, user, payment_date):
        super().__init__(transaction_id, amount, user)
        self.__payment_date = payment_date

    def get_payment_date(self):
        return self.__payment_date

    def process_payment(self):
        print(f"Processing payment of {self.get_amount()} for user {self.get_user().get_name()} on {self.__payment_date}.")


class InsuranceSystem:
    def __init__(self):
        self.__users = []
        self.__policies = []
        self.__claims = []
        self.__payments = []

    def register_user(self, user):
        self.__users.append(user)
        print(f"User {user.get_name()} registered successfully.")

    def login_user(self, user_id, password):
        for user in self.__users:
            if user.get_user_id() == user_id and user.verify_password(password):
                return user
        return None

    def add_policy(self, policy):
        self.__policies.append(policy)
        print(f"Policy {policy.get_policy_id()} added.")

    def remove_policy(self, policy_id):
        self.__policies = [p for p in self.__policies if p.get_policy_id() != policy_id]
        print(f"Policy with ID {policy_id} removed.")

    def modify_policy(self, policy_id, new_premium):
        for policy in self.__policies:
            if policy.get_policy_id() == policy_id:
                policy.set_premium(new_premium)
                print(f"Policy {policy_id} modified.")
                return
        print(f"Policy with ID {policy_id} not found.")

    def file_claim(self, claim):
        self.__claims.append(claim)
        print(f"Claim {claim.get_claim_id()} filed successfully.")

    def list_claims(self):
        if not self.__claims:
            print("No claims found.")
            return
        for claim in self.__claims:
            claim.display_claim_details()

    def process_payment(self, payment):
        self.__payments.append(payment)
        payment.process_payment()

    def list_payments(self):
        if not self.__payments:
            print("No payments found.")
            return
        for payment in self.__payments:
            print(f"Payment ID: {payment.get_transaction_id()}, Amount: {payment.get_amount()}, Date: {payment.get_payment_date()}")

    def list_users(self):
        if not self.__users:
            print("No users found.")
            return
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Role: {user.get_role()}")

    def list_policies(self):
        if not self.__policies:
            print("No policies found.")
            return
        for policy in self.__policies:
            policy.display_policy_details()


def main():
    system = InsuranceSystem()

    while True:
        print("\n====================================")
        print("  Welcome to the Insurance System")
        print("====================================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("====================================")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                register_menu(system)
            elif choice == "2":
                login_menu(system)
            elif choice == "3":
                print("Thank you for using the Insurance System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def register_menu(system):
    print("\n====================================")
    print("          User Registration")
    print("====================================")
    try:
        user_id = input("Enter user ID: ")
        name = input("Enter name: ")
        role = input("Enter role (Admin/Customer/Agent): ")
        password = input("Enter password: ")

        if role.lower() == "admin":
            user = Admin(user_id, name, role, password)
        elif role.lower() == "customer":
            user = Customer(user_id, name, role, password)
        elif role.lower() == "agent":
            agent_id = input("Enter agent ID: ")
            commission = float(input("Enter commission: "))
            user = Agent(user_id, name, role, password, agent_id, commission)
        else:
            print("Invalid role. Registration failed.")
            return

        system.register_user(user)
    except Exception as e:
        print(f"An error occurred during registration: {e}")


def login_menu(system):
    print("\n====================================")
    print("            User Login")
    print("====================================")
    try:
        user_id = input("Enter user ID: ")
        password = input("Enter password: ")

        user = system.login_user(user_id, password)
        if user:
            print(f"Welcome {user.get_name()}! You are logged in as {user.get_role()}.")
            if user.get_role().lower() == "admin":
                admin_menu(system)
            elif user.get_role().lower() == "customer":
                customer_menu(system, user)
            elif user.get_role().lower() == "agent":
                agent_menu(system, user)
        else:
            print("Invalid user ID or password. Please try again.")
    except Exception as e:
        print(f"An error occurred during login: {e}")


def admin_menu(system):
    while True:
        print("\n====================================")
        print("          Admin Dashboard")
        print("====================================")
        print("1. Add Policy")
        print("2. Remove Policy")
        print("3. Modify Policy")
        print("4. List Policies")
        print("5. List Claims")
        print("6. Log Out")
        print("====================================")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                policy_id = input("Enter policy ID: ")
                policy_type = input("Enter policy type: ")
                premium = float(input("Enter premium: "))
                owner = input("Enter owner ID: ")
                policy = Policy(policy_id, policy_type, premium, owner)
                system.add_policy(policy)
            elif choice == "2":
                policy_id = input("Enter policy ID to remove: ")
                system.remove_policy(policy_id)
            elif choice == "3":
                policy_id = input("Enter policy ID to modify: ")
                new_premium = float(input("Enter new premium: "))
                system.modify_policy(policy_id, new_premium)
            elif choice == "4":
                system.list_policies()
            elif choice == "5":
                system.list_claims()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def customer_menu(system, customer):
    while True:
        print("\n====================================")
        print("        Customer Dashboard")
        print("====================================")
        print("1. View Policy Details")
        print("2. File Claim")
        print("3. Log Out")
        print("====================================")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                customer.view_policy_details(system._InsuranceSystem__policies)
            elif choice == "2":
                transaction_id = input("Enter transaction ID: ")
                claim_id = input("Enter claim ID: ")
                claim_amount = float(input("Enter claim amount: "))
                claim = Claim(transaction_id, claim_amount, customer, claim_id, claim_amount)
                system.file_claim(claim)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def agent_menu(system, agent):
    while True:
        print("\n====================================")
        print("          Agent Dashboard")
        print("====================================")
        print("1. Sell Policy")
        print("2. Log Out")
        print("====================================")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                policy_id = input("Enter policy ID: ")
                policy_type = input("Enter policy type: ")
                premium = float(input("Enter premium: "))
                owner = input("Enter owner ID: ")
                policy = Policy(policy_id, policy_type, premium, owner)
                agent.sell_policy(policy)
                system.add_policy(policy)
            elif choice == "2":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()
