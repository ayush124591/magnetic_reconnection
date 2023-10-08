import os
import csv

# Specify the folder path where your CSV files are located
folder_path = '/home/punch/Desktop/hackathon/data'

# Function to edit a CSV file
def edit_csv_file(file_path):
    # Create a temporary list to store the edited data
    edited_data = []

    # Open the CSV file for reading
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Iterate through each row in the CSV
        for row in reader:
            # Here, you can edit the row as needed
            # For example, let's add "Edited" to the end of each row
            edited_row = row + ["Edited"]
            
            # Append the edited row to the temporary list
            edited_data.append(edited_row)

    # Open the same CSV file for writing (this will overwrite the existing file)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the edited data back to the CSV file
        writer.writerows(edited_data)

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        
        # Call the edit_csv_file function to edit the CSV file
        edit_csv_file(file_path)