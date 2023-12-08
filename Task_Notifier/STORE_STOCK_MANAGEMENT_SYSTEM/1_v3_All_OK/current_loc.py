import os

# Get the directory where the Flask application is located
app_directory = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the app directory
a=os.chdir(app_directory)
print (a)
print("Current working directory:", os.getcwd())
print("App directory:", app_directory)
