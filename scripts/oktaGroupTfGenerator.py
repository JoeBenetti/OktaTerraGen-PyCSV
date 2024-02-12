import csv

def generate_terraform_file(csv_file, terraform_file):
    # Open the CSV file for reading
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        
        # Open the Terraform file for writing
        with open(terraform_file, 'w') as tf_file:
            # Iterate over each row in the CSV file
            for row in reader:
                # Extract group details from the current row
                name = row['name']
                description = row['description']

                # Create a Terraform configuration block for the group
                terraform_code = f'''
                resource "okta_group" "{name}" {{
                  name = "{name}"
                  description = "{description}"
                }}
                '''
                # Write the Terraform code to the file
                tf_file.write(terraform_code)
                # Optional: Print the Terraform code to the console
                print(terraform_code)

# Specify paths for the input CSV file and output Terraform file
csv_file_path = '../dummyData/okta_groups.csv'
terraform_file_path = '../terraformExamples/oktaGroups.tf'
# Generate the Terraform file based on the CSV input
generate_terraform_file(csv_file_path, terraform_file_path)
