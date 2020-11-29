import pymysql#databse stuff

def connect():#tell each of the functions below how to connect to database
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        db="drinks_rounds"
    )
    return connection

def remove_from_database(table, condition):
    connection = connect()
    cursor = connection.cursor()
    query(f"DELETE FROM {table} WHERE name='{condition}'")


def load_from_database(table):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    return data


def save_people_to_database(List_of_people):
    connection = connect()
    cursor = connection.cursor()

    entry_errors = 0
    entry_errors_list = []
    error_messages_list = []
    for person in List_of_people:#iterate through list of objects and check IF entry doesnt exists exist [0] in db, insert new entry, ELSE update
        try:#try to update existing entry
            cursor.execute("select if(exists(select name from people where name=%s), 'True', 'False')",(person.name))
            a = cursor.fetchone()
            if a[0] == "False": #if entry doesnt exist in db, create one
                cursor.execute("INSERT INTO people(name, age, preference) VALUES (%s,%s,%s)",
                               (person.name, person.age, person.preference))
                connection.commit()
            else: #update entry
                cursor.execute("UPDATE people SET name=%s, age=%s, preference=%s WHERE name=%s",(person.name, person.age, person.preference, person.name))
                connection.commit()

        except Exception as error:#skip over the values that could not be entered, let user know what names were not entered, let user decide if they want to see the error message or if they want to ignore the problem
            error_messages_list.append(error)
            entry_errors_list.append(person.name)
            entry_errors += 1
            continue

    if entry_errors > 1:
        print(f"{entry_errors} errors found entering {entry_errors_list}")
        if input("these names were not added to the people database \n press enter to continue, to see error messages input [Y]\n").capitalize() == "Y":
            for i in range(len(error_messages_list)):
                print(f"{entry_errors_list[i]} : {error_messages_list[i]}\n")
            input("press enter to continue")


def save_drinks_to_database(List_of_drinks):
    connection = connect()
    cursor = connection.cursor()

    entry_errors = 0
    entry_errors_list = []
    error_messages_list = []
    for drink in List_of_drinks:  # iterate through list of objects and check IF entry doesnt exists exist [0] in db, insert new entry, ELSE update
        try:  # try to update existing entry
            cursor.execute("select if(exists(select name from drinks where name=%s), 'True', 'False')", (drink.name))  # if entry doesnt exist in db, create one
            a = cursor.fetchone()
            if a[0] == 'False':
                cursor.execute("INSERT INTO drinks(name, price) VALUES (%s,%s)",
                               (drink.name, drink.price))
                connection.commit()
            else:  # update entry
                cursor.execute("UPDATE drinks SET name=%s, price=%s WHERE name=%s",
                               (drink.name, drink.price, drink.name))
                connection.commit()

        except Exception as error:  # skip over the values that could not be entered, let user know what names were not entered, let user decide if they want to see the error message or if they want to ignore the problem
            error_messages_list.append(error)
            entry_errors_list.append(drink.name)
            entry_errors += 1
            continue

    if entry_errors > 1:
        print(f"{entry_errors} errors found entering {entry_errors_list}")
        if input("these drinks were not added to the drinks database \n press enter to continue, to see error messages input [Y]\n").capitalize() == "Y":
            for i in range(len(error_messages_list)):
                print(f"{entry_errors_list[i]} : {error_messages_list[i]}\n")
            input("press enter to continue")


def save_receipts_to_database(Receipts_list):
    connection = connect()
    cursor = connection.cursor()

    entry_errors = 0
    entry_errors_list = []
    error_messages_list = []

    for Receipt in Receipts_list:
        for order in Receipt.Full_order:
            try:
                cursor.execute("select if(exists(select receipt_id from receipts where receipt_id=%s), 'True', 'False')",
                               (Receipt.receipt_id))
                a = cursor.fetchone()

                if a[0] == 'False': # if entry doesnt exist in db, create one
                    cursor.execute("INSERT INTO receipts(receipt_id, customer_name, drink_name, drink_price) VALUES (%s,%s,%s,%s)",
                                   (Receipt.receipt_id, order.person.name, order.drink.name, order.drink.price))
                    connection.commit()

            except Exception as error:  # skip over the values that could not be entered, let user know what names were not entered, let user decide if they want to see the error message or if they want to ignore the problem
                error_messages_list.append(error)
                entry_errors_list.append(order.drink.name)
                entry_errors += 1
                continue

        if entry_errors > 1:
            print(f"{entry_errors} errors found entering {entry_errors_list}")
            if input("these entries were not added to the receipts database \n press enter to continue, to see error messages input [Y]\n").capitalize() == "Y":
                for i in range(len(error_messages_list)):
                    print(f"{entry_errors_list[i]} : {error_messages_list[i]}\n")
                input("press enter to continue")
