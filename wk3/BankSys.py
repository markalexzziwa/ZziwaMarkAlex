class Transaction:
    """Parent class representing a generic banking operation."""
    def __init__(self, account_number: str, amount: float):
        self.account_number = account_number
        self.amount = amount

    def execute(self):
        """Method to be overridden by child classes."""
        print(f"Processing a generic transaction of UGX{self.amount:.2f}")
class Deposit(Transaction):
    """Child class for Deposit operations."""
    # METHOD OVERLOADING: Achieved using a default value for 'source'
    def __init__(self, account_number: str, amount: float, source: str = "Standard Deposit"):
        super().__init__(account_number, amount)
        self.source = source

    # METHOD OVERRIDING: Custom execution for deposit
    def execute(self):
        print(f"[DEPOSIT] Deposited UGX{self.amount:.2f} into account {self.account_number} via {self.source}.")


class Withdrawal(Transaction):
    """Child class for Withdrawal operations."""
    def __init__(self, account_number: str, amount: float):
        super().__init__(account_number, amount)

    # METHOD OVERRIDING & OVERLOADING:
    # Overrides parent 'execute', and overloads via the optional 'atm_fee' parameter
    def execute(self, atm_fee: float = None):
        if atm_fee is not None:
            total_debit = self.amount + atm_fee
            print(f"[WITHDRAWAL] Withdrew UGX{self.amount:.2f} (Fee: UGX{atm_fee:.2f}). Total account debit: UGX{total_debit:.2f}.")
        else:
            print(f"[WITHDRAWAL] Withdrew UGX{self.amount:.2f} from account {self.account_number}.")


class Transfer(Transaction):
    """Child class for Transfer operations."""
    def __init__(self, source_account_number: str, amount: float, target_account_number: str):
        super().__init__(source_account_number, amount)
        self.target_account_number = target_account_number

    # METHOD OVERRIDING: Custom execution for transfer
    def execute(self):
        print(f"[TRANSFER] Transferred UGX{self.amount:.2f} from account {self.account_number} to account {self.target_account_number}.")
if __name__ == "__main__":
    print("=== Employer Banking System Simulation ===\n")

    # 1. DEMONSTRATING OVERLOADING: Employer deposits salary using the optional source parameter
    corporate_payroll = Deposit("ACC-7789", 5000.0, source="Employer Payroll")
    corporate_payroll.execute()  # Calls overridden method

    # 2. DEMONSTRATING OVERRIDING: Standard execution of a withdrawal
    standard_withdrawal = Withdrawal("ACC-7789", 200.0)
    standard_withdrawal.execute()  # Calls overridden method without optional arguments

    # 3. DEMONSTRATING OVERLOADING: Withdrawal execution with a specific fee
    atm_withdrawal = Withdrawal("ACC-7789", 100.0)
    atm_withdrawal.execute(atm_fee=3.50)  # Calls overloaded variation by passing the fee

    # 4. DEMONSTRATING OVERRIDING: Execution of an account-to-account transfer
    employee_transfer = Transfer("ACC-7789", 1200.0, "ACC-1142")
    employee_transfer.execute()  # Calls overridden method
