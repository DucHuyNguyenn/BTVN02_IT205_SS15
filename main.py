# =====================================================
# SMART ATM SYSTEM
# =====================================================

# ---------------- GLOBAL VARIABLES -------------------
# Global Variables:
# Được sử dụng để lưu trạng thái chung của hệ thống ATM.

atm_vault_balance = 50000000      # Tiền mặt trong ATM
user_account_balance = 10000000   # Số dư tài khoản khách hàng


# ---------------- HELPER FUNCTIONS -------------------

def get_positive_amount(message):
    """
    Nhập số tiền hợp lệ từ bàn phím.

    Parameters:
        message (str): Nội dung hiển thị cho người dùng.

    Returns:
        int:
            Số tiền hợp lệ (> 0)
        None:
            Nếu dữ liệu không hợp lệ.
    """
    try:
        amount = int(input(message))

        if amount <= 0:
            print("Số tiền không hợp lệ")
            return None

        return amount

    except ValueError:
        print("Vui lòng nhập đúng định dạng số.")
        return None


# ---------------- BUSINESS FUNCTIONS -----------------

def display_balances():
    """
    Hiển thị thông tin số dư hiện tại.

    Parameters:
        None

    Returns:
        None
    """

    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Nạp tiền vào tài khoản.

    Parameters:
        amount (int): Số tiền muốn nạp.

    Returns:
        bool:
            True nếu nạp tiền thành công.
    """

    global user_account_balance
    global atm_vault_balance

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra các điều kiện rút tiền.

    Parameters:
        amount (int): Số tiền khách muốn rút.

    Returns:
        tuple:
        (
            status,
            total_deduction,
            fee
        )

        status có thể là:
        - "INVALID_AMOUNT"
        - "INSUFFICIENT_FUNDS"
        - "ATM_OUT_OF_CASH"
        - "OK"
    """

    # -------- LOCAL VARIABLES --------
    fee = 1100
    total_deduction = amount + fee

    if amount % 50000 != 0:
        return ("INVALID_AMOUNT", total_deduction, fee)

    if total_deduction > user_account_balance:
        return ("INSUFFICIENT_FUNDS", total_deduction, fee)

    if amount > atm_vault_balance:
        return ("ATM_OUT_OF_CASH", total_deduction, fee)

    return ("OK", total_deduction, fee)


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện giao dịch rút tiền.

    Parameters:
        total_deduction (int):
            Tổng tiền bị trừ khỏi tài khoản.

        amount_to_dispense (int):
            Tiền thực tế ATM nhả ra.

    Returns:
        None
    """

    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(
        f"Số dư tài khoản còn lại: "
        f"{user_account_balance:,} VND."
    )


# ---------------- MAIN FUNCTION ----------------------

def main():
    """
    Hàm điều khiển chương trình ATM.

    Parameters:
        None

    Returns:
        None
    """

    while True:

        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        # -------- CHỨC NĂNG 1 --------
        if choice == "1":
            display_balances()

        # -------- CHỨC NĂNG 2 --------
        elif choice == "2":

            print("\n--- NẠP TIỀN ---")

            amount = get_positive_amount(
                "Nhập số tiền muốn nạp: "
            )

            if amount is None:
                continue

            if deposit_money(amount):
                print(
                    "Giao dịch thành công! "
                    f"Số dư tài khoản hiện tại: "
                    f"{user_account_balance:,} VND."
                )

        # -------- CHỨC NĂNG 3 --------
        elif choice == "3":

            print("\n--- RÚT TIỀN ---")

            amount = get_positive_amount(
                "Nhập số tiền cần rút: "
            )

            if amount is None:
                continue

            status, total_deduction, fee = (
                check_withdrawal_rules(amount)
            )

            if status == "INVALID_AMOUNT":
                print("Số tiền rút phải là bội số của 50,000")

            elif status == "INSUFFICIENT_FUNDS":
                print(
                    "Giao dịch thất bại: "
                    "Số dư tài khoản không đủ."
                )

            elif status == "ATM_OUT_OF_CASH":
                print(
                    "Giao dịch thất bại: "
                    "Máy ATM không đủ tiền mặt để phục vụ."
                )

            elif status == "OK":
                execute_withdrawal(
                    total_deduction,
                    amount
                )

        # -------- CHỨC NĂNG 4 --------
        elif choice == "4":
            print("\nCảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


# ---------------- RUN PROGRAM ------------------------

if __name__ == "__main__":
    main()