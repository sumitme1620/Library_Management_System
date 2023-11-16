from dbhelper import DBHelper


def main():
    db=DBHelper()

    while True:
        print("************WELCOME************")
        print()
        print("PRESS 1 to Insert new user")
        print("PRESS 2 to Display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update  user")
        print("PRESS 5 to exit user")
        print()

        try:
            choice=int(input("Please Enter your input: "))
            if (choice==1):
                #insert user
                uid = int(input("Enter user id: "))
                username=input("Enter user name: ")
                userphone=input("Enter user phone: ")
                db.insert_user(uid,username,userphone)


            elif choice==2:
                #display user
                db.fetch_all()
             

            elif choice==3:
                #delete user
                userid=int(input("Enter user id to which you want to delete: "))
                db.delete_user(userid)
                

            elif choice==4:
                #update user
                uid = int(input("Enter user id: "))
                username=input("Enter New user name: ")
                userphone=input("Enter New user phone: ")
                db.update_user(uid,username,userphone)
                

            elif choice==5:
                break


            else:
                print("Invalid Input ! Try again")

        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")

if __name__=="__main__":
    main()
