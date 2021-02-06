import sqlite3 as lite

# functionality goes here

class DataManage(object):
    def __init__(self):
        global con 
        try:
            con = lite.connect('ideas.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS idea(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,description TEXT, price TEXT, isPrivate BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB !")

    def insert_data(self, data):
        try:
             with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO idea(name,description,price,isPrivate) VALUES (?,?,?,?)", data
                    );
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
             with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM idea")
                return cur.fetchall()
                #this fetchall work almost same as array
        except Exception:
            return False

    def delete_data(self,id):
        try:
             with con:
                cur = con.cursor()
                sql="DELETE FROM idea WHERE id =?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


#interface goes here
def main():
    #design
    print('*'*40)
    print("\n:: idea management:: \n")
    print('*'*40)

    db=DataManage()
    print('*'*40)
    print("\n:: User manual :: \n")
    print('*'*40)
        
    print('\nPress 1. Inset a new idea\n')
    print('\nPress 2. Show all idea\n')
    print('\nPress 3. delete a idea(Need ID of idea)\n')
    print("#"*40)
    print('\n') 

    choice = input("\n Enter a choice")

    if choice =="1":
        name = input("\n Enter idea name: ")
        description = input("\n Enter idea description: ")
        price = input("\n Enter idea price: ")
        private = input("\n is this idea private(0/1): ")
        
        if db.insert_data([name,description,price,private]):
            print("idea was inseted successful")
        else:
            print("OOPS Something is wrong")


    elif choice == '2':
        print("\n:: idea List ::")

        for index,item in enumerate(db.fetch_data()):
            print("\n Serial No: "+ str(index+1))
            print("\n idea id: "+ str(item[0]))
            print("\n idea name: "+ str(item[1]))
            print("\n idea description: "+ str(item[2]))
            print("\n idea price: "+ str(item[3]))
            private = "YES" if item[4] else "NO"
            print("\n Is private: "+private)
            print("\n")

    elif choice =="3":
        record_id = input("Enter idea ID: ")

        if db.delete_data(record_id):
            print("idea was deleted with success")
        else:
            print("Unable to delete")
        
    else:
        print("\n Wrong choice")
    
if __name__ == '__main__':
    main()
     