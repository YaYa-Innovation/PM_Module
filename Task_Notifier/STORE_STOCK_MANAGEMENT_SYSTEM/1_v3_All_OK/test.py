from openpyxl import Workbook
from datetime import datetime

def create_main_excel(file_path):
    # Create a new workbook and select the active sheet
    wb = Workbook()
    ws = wb.active

    # Add headers
    headers = ["Spare Name", "Spare ID", "Quantity", "Booking"]
    ws.append(headers)

    # Add sample data
    data = [
        ["Pen", 1, 10, 2],
        ["Pencil", 2, 5, 1],
        ["Notebook", 3, 20, 5],
        # Add more rows as needed
    ]

    # Populate the worksheet with data
    for row in data:
        ws.append(row)

    # Save the workbook to the specified file path
    wb.save(file_path)

def create_history_excel(file_path):
    # Create a new workbook and select the active sheet
    wb = Workbook()
    ws = wb.active

    # Add headers
    headers = ["Timestamp", "Spare Name", "Spare ID", "Quantity Requested", "Purpose"]
    ws.append(headers)

    # Add sample history data
    history_data = [
        [datetime.now(), "Pen", 1, 3, "Task 1"],
        [datetime.now(), "Pencil", 2, 2, "Task 2"],
        # Add more rows as needed
    ]

    # Populate the worksheet with history data
    for row in history_data:
        ws.append(row)

    # Save the workbook to the specified file path
    wb.save(file_path)

if __name__ == "__main__":
    # Specify the file paths for the new Excel files
    main_excel_path = " D:/STORE_STOCK_MANAGEMENT_SYSTEM/v1_STORE_STOCK_MANAGEMENT_SYSTEM/tasks.xlsx"
    history_excel_path = " D:/STORE_STOCK_MANAGEMENT_SYSTEM/v1_STORE_STOCK_MANAGEMENT_SYSTEM/history.xlsx"

    # Call the functions to create and populate the Excel files
    create_main_excel(main_excel_path)
    create_history_excel(history_excel_path)

    print(f"Excel files '{main_excel_path}' and '{history_excel_path}' created successfully.")

