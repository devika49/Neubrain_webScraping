import pandas as pd

# Load the CSV file without headers
file_path = 'D:/Neubrain_webScraping/table_data2.csv'  # Update with your file path if needed
data = pd.read_csv(file_path, header=None)

# Assign the columns based on the indices you mentioned (assuming the Type is at index 6 and Status at index 7)
data.columns = ['Index', 'Company Name', 'Company Name 2', 'Number', 'ID', 'Some Other Column', 'Type', 'Status']

# Print the columns of the DataFrame
print(data.columns)

# Filter data for each type and status
# Separate data by Type and Status

# For Brand Owner
brand_owner_registered = data[(data['Type'] == 'Brand Owner') & (data['Status'] == 'Approved')]
brand_owner_in_process = data[(data['Type'] == 'Brand Owner') & (data['Status'] == 'In Progress')]
brand_owner_rejected = data[(data['Type'] == 'Brand Owner') & (data['Status'] == 'Rejected')]

# For Importer
importer_registered = data[(data['Type'] == 'Importer') & (data['Status'] == 'Approved')]
importer_in_process = data[(data['Type'] == 'Importer') & (data['Status'] == 'In Progress')]
importer_rejected = data[(data['Type'] == 'Importer') & (data['Status'] == 'Rejected')]

# For Producer
producer_registered = data[(data['Type'] == 'Producer') & (data['Status'] == 'Approved')]
producer_in_process = data[(data['Type'] == 'Producer') & (data['Status'] == 'In Progress')]
producer_rejected = data[(data['Type'] == 'Producer') & (data['Status'] == 'Rejected')]

# Display counts of each category for quick reference
print("Brand Owner - Registered:", len(brand_owner_registered))
print("Brand Owner - In Process:", len(brand_owner_in_process))
print("Brand Owner - Rejected:", len(brand_owner_rejected))

print("Importer - Registered:", len(importer_registered))
print("Importer - In Process:", len(importer_in_process))
print("Importer - Rejected:", len(importer_rejected))

print("Producer - Registered:", len(producer_registered))
print("Producer - In Process:", len(producer_in_process))
print("Producer - Rejected:", len(producer_rejected))

# Save each subset to a CSV file if needed
brand_owner_registered.to_csv('brand_owner_registered.csv', index=False)
brand_owner_in_process.to_csv('brand_owner_in_process.csv', index=False)
brand_owner_rejected.to_csv('brand_owner_rejected.csv', index=False)

importer_registered.to_csv('importer_registered.csv', index=False)
importer_in_process.to_csv('importer_in_process.csv', index=False)
importer_rejected.to_csv('importer_rejected.csv', index=False)

producer_registered.to_csv('producer_registered.csv', index=False)
producer_in_process.to_csv('producer_in_process.csv', index=False)
producer_rejected.to_csv('producer_rejected.csv', index=False)
