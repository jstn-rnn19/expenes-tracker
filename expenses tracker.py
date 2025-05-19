import csv
import csv as cs
import os as root
import datetime as date_time
import calendar as calendar_name

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
        "Date": date_time.datetime.now().isoformat(" ", "seconds" )
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
            for row in range (reader):
                yield row



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
                amount = row.get( "Amount", "" ).strip()
                descript = row.get("Description", "").strip()
                if amount:
                    try:
                        total += float(amount)
                    except ValueError:
                        print(f"skipping Invalid Amount: {amount}")
                print("===================")
                yield descript
                yield amount
                print( "===================" )


    except FileNotFoundError:
        print("file not found")
    yield total



def display_specific_month(month, file):
    found = False
    total = 0.0
    month_name = calendar_name.month_name[int(month)]
    try:
        with open( file, mode='r', newline='' ) as f:
            reader = cs.DictReader( f )

            for row in reader:
                date_str = row.get( "Date", "" )
                descript = row.get( "Description", "" )
                amount = row.get( "Amount", "" )

                if len( date_str ) >= 7 and int(date_str[5:7]) == int(month):
                    if not found:
                        date_obj = date_time.datetime.strptime( date_str, "%Y-%m-%d %H:%M:%S" )
                        month_name = date_obj.strftime( "%B" )
                        print( f"Records for {month_name}" )
                        print( "===================" )
                        found = True

                    yield descript
                    yield amount
                    print( "===================" )
                    total += float(amount)


            print(total)

            if not found:
                print( f"No records found for month {month_name}" )
    except FileNotFoundError:
        print( "File not found" )



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
                display_Expense = display_expenses(expenses_file)
                for expenses in display_Expense:
                    print(expenses)
                print( "======================================" )


            elif user_choice == '5':
                print( "======================================" )
                display_Expense = display_all_amount( expenses_file )


                for amount  in display_Expense:

                    print(amount)
                print( "======================================" )



            elif user_choice == '6':
                month = int(input("Enter Month (Ex. '05' or '5'): "))
                if 1 <= month <= 12:
                    display_month = display_specific_month(month, expenses_file)
                    for date in display_month:
                        print(date)
            elif user_choice == '7':
                break
            else:
                print("Out of Range")

        except (TypeError, SyntaxError, ValueError):
            print("Invalid Input")
        finally:
            print( "======================================" )
            print("Execute Successfully")
            pass






main()