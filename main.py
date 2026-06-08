atm_vault_balance = 50000000
user_account_balance = 10000000

# chức năng 1: 
def display_balance():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")
# chức năng 2:
def deposit_money():
    print("--- NẠP TIỀN ---")
  
    try:
          value = int(input("Nhập số tiền muốn nạp"))
    except ValueError:
        print("Nhập đúng định dạng")
    if value < 0 or value ==0:
        print("Tiền không hợp lệ")
    else:
        global user_account_balance
        user_account_balance += value
        print(f"Giao dịch thành công! số dư tài khoản hiện tại: {user_account_balance}")
# chức năng 3:
def check_withdrawal_rules(amount):
    
    fee =  1100
    toltal_fee = amount + fee
    if toltal_fee > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    elif amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return toltal_fee
def main():
        while True:
            

            print("SMART ATM".center(50,"="))
            print("""1. Xem số dư
        2. Nạp tiền
        3. Rút tiền
        4. Kết thúc giao dịch""")
            print("="*50)

            user_choice = input("Vui lòng chọn giao dịch (1-4):")

            match user_choice:
                case "1":
                    display_balance()
                case "2":
                    deposit_money()
                case "3":
                    print("--- RÚT TIỀN ---")
                    
                    
                    try:
                        amount = int(input("Nhập số tiền muốn rút"))
                    except ValueError:
                        print("Lỗi định dạng nhập lại")    

                    if amount < 0 or amount ==0 :
                        print("Tiền không hợp lệ nhập lại: ")
                        continue   
                    check = check_withdrawal_rules(amount)
                    if check == "INSUFFICIENT_FUNDS" or check =="ATM_OUT_OF_CASH":
                        print(f"Giao dịch thất bại: {check}")
                        
                    else:
                        global user_account_balance
                        user_account_balance -=amount
                        print(f"Giao dịch đang xử lý...")
                        print(f"Phí giao dịch: {check}")
                        print(f"Bạn đã rút thành công {amount}")
                        print(f"Số dư tài khoản còn lại: {user_account_balance  }")
                case "4":
                    print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                    break
                case _:
                    print("Nhập cho đúng  1 - 4")