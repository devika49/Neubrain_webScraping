import pandas as pd

# Load the CSV file without headers
file_path = 'D:/Neubrain_webScraping/table_data2.csv'  # Update with your file path if needed
data = pd.read_csv(file_path, header=None)

# Assign the correct number of column names (7 columns)
data.columns = ['Date of Application', 'Legal Name', 'Trade Name 2', 'App NO', 'Registration Number', 'Type of PIBO', 'Application Status']

# Print the columns of the DataFrame to verify
print(data.columns)

# Filter data for each type and status
# Separate data by Type and Status

# For Brand Owner
brand_owner_registered = data[(data['Type of PIBO'] == 'Brand Owner') & (data['Application Status'] == 'Approved')]
brand_owner_in_process = data[(data['Type of PIBO'] == 'Brand Owner') & (data['Application Status'] == 'In Progress')]
brand_owner_rejected = data[(data['Type of PIBO'] == 'Brand Owner') & (data['Application Status'] == 'Rejected')]

# For Importer
importer_registered = data[(data['Type of PIBO'] == 'Importer') & (data['Application Status'] == 'Approved')]
importer_in_process = data[(data['Type of PIBO'] == 'Importer') & (data['Application Status'] == 'In Progress')]
importer_rejected = data[(data['Type of PIBO'] == 'Importer') & (data['Application Status'] == 'Rejected')]

# For Producer
producer_registered = data[(data['Type of PIBO'] == 'Producer') & (data['Application Status'] == 'Approved')]
producer_in_process = data[(data['Type of PIBO'] == 'Producer') & (data['Application Status'] == 'In Progress')]
producer_rejected = data[(data['Type of PIBO'] == 'Producer') & (data['Application Status'] == 'Rejected')]

# Combine all filtered data into a single DataFrame for CSV output
combined_data = pd.concat([
    brand_owner_registered.assign(Category='Brand Owner - Registered'),
    brand_owner_in_process.assign(Category='Brand Owner - In Process'),
    brand_owner_rejected.assign(Category='Brand Owner - Rejected'),
    importer_registered.assign(Category='Importer - Registered'),
    importer_in_process.assign(Category='Importer - In Process'),
    importer_rejected.assign(Category='Importer - Rejected'),
    producer_registered.assign(Category='Producer - Registered'),
    producer_in_process.assign(Category='Producer - In Process'),
    producer_rejected.assign(Category='Producer - Rejected')
])

# Print the first few rows of the combined data for verification
print(combined_data.head())

# Save the combined data to a CSV file
combined_data.to_csv('combined_data.csv', index=False)
