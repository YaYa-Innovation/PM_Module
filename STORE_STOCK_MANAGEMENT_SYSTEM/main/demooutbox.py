import os
from flask import Flask, render_template, request
from openpyxl import Workbook
from datetime import datetime

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_excel_file(user_name, location_name):
    try:
        # Create a unique filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        excel_filename = f'locations_{timestamp}.xlsx'
        excel_filepath = os.path.join(BASE_DIR, excel_filename)

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Locations'
        sheet['A1'] = 'User Name'
        sheet['B1'] = 'Location Name'
        sheet['C1'] = 'Date Created'

        # Add user input to the Excel file
        sheet.append([user_name, location_name, datetime.now()])

        workbook.save(excel_filepath)
        return excel_filepath
    except Exception as e:
        print(f"Error creating Excel file: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_location', methods=['POST'])
def add_location():
    user_name = request.form.get('userName')
    location_name = request.form.get('locationName')
    
    if user_name and location_name:
        excel_filepath = create_excel_file(user_name, location_name)
        if excel_filepath:
            return f'Location "{location_name}" created by "{user_name}" and added to Excel file: {excel_filepath}'
        else:
            return 'Error creating Excel file. Please check the server logs for more information.'
    else:
        return 'Invalid input. Please provide both your name and a location name.'

if __name__ == '__main__':
    app.run(debug=True)
