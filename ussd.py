

"""
Assignment... 

Create a realistic USSD for buying data with any network of your choice. Glo, MTN, Airtel etc

From where you type *312# up until where you have "You have successfully purchased ##MB of data"

Your github link is to be submitted on Sunday
"""

def ussd_data_purchase():
    dialed_code = input("Enter USSD code: ")

    if dialed_code == "*312#":
        print("\n--- MTN Data Menu ---")
        print("1. Daily Plans")
        print("2. Weekly Plans")
        print("3. Monthly Plans")
        
        choice_plan = input("Reply: ")

        if choice_plan == "1":
            print("\n--- Daily Plans ---")
            print("1. 50MB for ₦50")
            print("2. 150MB for ₦100")
            print("3. 1GB for ₦300")
            
            choice_data = input("Reply: ")

            # Map choice to data amount
            if choice_data == "1":
                data_amount = "50MB"
                price = "₦50"
            elif choice_data == "2":
                data_amount = "150MB"
                price = "₦100"
            elif choice_data == "3":
                data_amount = "1GB"
                price = "₦300"
            else:
                print("\nInvalid choice. Session ended.")
                return

            # Confirmation Step
            print(f"\nYou selected {data_amount} for {price}.")
            print("1. Confirm")
            print("2. Cancel")
            
            confirm = input("Reply: ")

            if confirm == "1":
                print(f"\nYou have successfully purchased {data_amount} of data. Thank you!")
            else:
                print("\nTransaction cancelled.")

        elif choice_plan == "2":
            print("\n--- Weekly Plans ---")
            print("1. 350MB for ₦300")
            print("2. 750MB for ₦500")
            
            choice_data = input("Reply: ")
            
            if choice_data == "1":
                data_amount = "350MB"
                price = "₦300"
            elif choice_data == "2":
                data_amount = "750MB"
                price = "₦500"
            else:
                print("\nInvalid choice. Session ended.")
                return

            print(f"\nYou selected {data_amount} for {price}.")
            print("1. Confirm")
            print("2. Cancel")
            
            confirm = input("Reply: ")

            if confirm == "1":
                print(f"\nYou have successfully purchased {data_amount} of data. Thank you!")
            else:
                print("\nTransaction cancelled.")

        else:
            print("\nInvalid menu option. Session ended.")

    else:
        print("\nInvalid USSD code. Please try again.")

ussd_data_purchase()
