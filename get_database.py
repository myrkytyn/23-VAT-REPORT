import pyodbc as db

SERVER = "IIKOSERVER\RESTO"
DATABASE = "fabbrica"

def main():
    conn = db.connect(f"DRIVER={{SQL Server}};SERVER={SERVER};UID=me;PWD=password;DATABASE=db")
    print(conn)


if __name__ == "__main__":
    main()