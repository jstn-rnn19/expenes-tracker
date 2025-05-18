import csv
import csv as cs
import os as root
import datetime as date

expenses_file = "expenses.csv"

def adding_expenses(info, amount, file):
    fieldnames = ["Id", "Description", "Amount", "Date"]
    rows = []
    if root.path.exists( file ):
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader(f)
            rows = list(reader)

    new_id = str( len( rows ) + 1 )

    new_row = {
        "Id": new_id,
        "Description": info,
        "Amount": amount,
        "Date": date.datetime.now().isoformat(" ", "seconds" )
    }
    rows.append(new_row)

    with open(file, mode="w", newline="") as f:
        writer = cs.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print( f"Expense'{info}' and {amount} added successfully." )

def update_description(Id, file):
    fieldnames = ["Id", "Description", "Amount", "Date"]
    updated = False
    if root.path.exists( file ):
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader(f)
            rows = list(reader)
        for row in rows:
            if row["Id"] == Id:
                print(f"Enter new Description to ID {Id}")
                new_description = input("Description: ")
                row["Description"] = new_description
                updated = True
                break
        if updated:
            with open( file, mode='w', newline='' ) as f:
                writer = cs.DictWriter( f, fieldnames=fieldnames )
                writer.writeheader()
                writer.writerows( rows )
            print( f"Description for ID {Id} updated successfully." )
        else:
            print( f"No match found for ID {Id}." )
    else:
        print( "CSV file not found." )

def update_amount(Id, file):
    fieldnames = ["Id", "Description", "Amount", "Date"]
    updated = False
    if root.path.exists( file ):
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader( f )
            rows = list( reader )
        for row in rows:
            if row["Id"] == Id:
                print( f"Enter new Amount to ID {Id}" )
                new_amount = input( "Amount: " )
                row["Description"] = new_amount
                updated = True
                break
        if updated:
            with open( file, mode='w', newline='' ) as f:
                writer = cs.DictWriter( f, fieldnames=fieldnames )
                writer.writeheader()
                writer.writerows( rows )
            print( f"Amount for ID {Id} updated successfully." )
        else:
            print( f"No match found for ID {Id}." )
    else:
        print( "CSV file not found." )


def display_expenses(file):
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader(f)
            for row in reader:
                print( row )

def delete_expenses(Id, file):
    fieldnames = ["Id", "Description", "Amount", "Date"]
    updated = False
    if not root.path.exists( file ):
        print( "File not found." )
        return

    ids_to_delete = set( ids.strip() for ids in Id.split( "," ) if ids.strip() )

    with open( file, mode='r', newline='' ) as f:
        reader = cs.DictReader( f )
        rows = [row for row in reader if row["Id"] not in ids_to_delete]

    if len( rows ) == 0:
        print( "No Match Id" )

    for i, row in enumerate( rows, start=1 ):
        row["Id"] = str( i )

    with open( file, mode="w", newline="" ) as f:
        writer = csv.DictWriter( f, fieldnames=fieldnames )
        writer.writeheader()
        writer.writerows( rows )

        print( f"Deleted record with Id {Id} successfully." )


def display_all_amount(file):
    total = 0.0
    try:
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader( f )
            for row in reader:
                amount = row.get("Amount", "").strip()
                if amount:
                    try:
                        total += float(amount)
                    except ValueError:
                        print(f"skipping Invalid Amount: {amount}")
    except FileNotFoundError:
        print("file not found")
    print(f"Total Expenses: {total}")

def display_specific_month(month, file):
    try:
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader( f )
            found = False
            for row in reader:
                date = row.get("Date", "")
                if len(date) >= 7 and date[5:7] == month:
                    print(row)
                    found = True
            if not found:
                print( f"No records found for month {month}" )
    except FileNotFoundError:
        print("File mot Found")



def main():

    while True:
        print("======================================")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. All Expenses")
        print("5. Summary of  All Expenses")
        print("6. Summary of All Expense by Month")
        print("7. Exit")
        print( "======================================" )
        try:
            user_choice = input("Enter choices: ")
            print( "======================================" )
            if user_choice == '1':
                print( "======================================" )
                description = input("Description: ")
                print( "======================================" )
                amount = float(input("Enter Amount: "))
                print( "======================================" )
                adding_expenses(description, amount, expenses_file)
                print( "======================================" )

            elif user_choice == '2':
                print( "======================================" )
                choice = input("Update (1) Description or (2) Amount?: ")
                print( "======================================" )
                if choice == '1':
                    display_expenses(expenses_file)
                    print( "======================================" )
                    update_id = input("Enter Id to update Description: ")
                    print( "======================================" )
                    update_description(update_id, expenses_file)
                    print( "======================================" )
                elif choice == '2':
                    print( "======================================" )
                    display_expenses( expenses_file )
                    print( "======================================" )
                    update_id = input( "Enter Id to update Description: " )
                    print( "======================================" )
                    update_amount(update_id, expenses_file)
                    print( "======================================" )
                else:
                    print( "======================================" )
                    print("Invalid Input")
                    print( "======================================" )
            elif user_choice == '3':
                print( "======================================" )
                display_expenses(expenses_file)
                print( "======================================" )
                delete_id = input("Enter Id to Delete: ")
                print( "======================================" )
                delete_expenses(delete_id, expenses_file)
                print( "======================================" )
            elif user_choice == '4':
                print( "======================================" )
                display_expenses(expenses_file)
                print( "======================================" )
            elif user_choice == '5':
                print( "======================================" )
                display_all_amount( expenses_file )
                print( "======================================" )

            elif user_choice == '6':
                month = input("Enter Month (Ex. 05): ")
                display_specific_month(month, expenses_file)
            elif user_choice == '7':
                break
            else:
                print("Out of Range")

        except (TypeError, SyntaxError, ValueError):
            print("Invalid Input")
        finally:
            print("Execute Successfully")
            pass






main()