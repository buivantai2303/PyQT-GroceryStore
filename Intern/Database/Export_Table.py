
import pyodbc

def connect_db():
    # Define the database connection parameters
    server = 'BANHMIBIETBAY\\SQLEXPRESS'
    database = 'Sales_Manager'
    username = 'sa'
    password = '180403'

    # Create the database connection
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

    cursor = conn.cursor()

    cursor.execute('BEGIN TRANSACTION')

    try:
        # Thêm người dùng mới vào bảng users
        insert_user_query = "INSERT INTO users (username, password, full_name, email) VALUES (?, ?, ?, ?)"
        user_values = ('new_user', '123456', 'New User', 'new_user@example.com')
        cursor.execute(insert_user_query, user_values)

        # Thêm thông tin đăng nhập của người dùng mới vào bảng login
        insert_login_query = "INSERT INTO login (username, password) VALUES (?, ?)"
        login_values = ('new_user', '123456')
        cursor.execute(insert_login_query, login_values)

        # Hoàn tất giao dịch
        cursor.commit()
        print("Đăng ký thành công!")

    except Exception as e:
        # Nếu có lỗi, rollback giao dịch
        cursor.rollback()
        print("Đăng ký thất bại:", str(e))

    finally:
        # Đóng kết nối
        conn.close()
