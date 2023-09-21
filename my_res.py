from datetime import datetime, timedelta
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

# Set your Azure subscription ID
subscription_id = 'YOUR_SUBSCRIPTION_ID'

# Initialize Azure credentials using DefaultAzureCredential, which supports multiple authentication methods
credentials = DefaultAzureCredential()

# Create a ResourceManagementClient instance
resource_client = ResourceManagementClient(credentials, subscription_id)

# Calculate the date two weeks ago
two_weeks_ago = datetime.utcnow() - timedelta(weeks=2)

# List all resource groups in the subscription
resource_groups = resource_client.resource_groups.list()

# Iterate through resource groups
for resource_group in resource_groups:
    # List resources in the resource group
    resources = resource_client.resources.list_by_resource_group(resource_group.name)

    # Iterate through resources and check their creation date
    for resource in resources:
        if resource.properties and resource.properties.provisioning_state == 'Succeeded':
            created_time = resource.properties.created_date
            if created_time and created_time <= two_weeks_ago:
                print(f"Resource Name: {resource.name}")
                print(f"Resource Type: {resource.type}")
                print(f"Resource Group: {resource_group.name}")
                print(f"Creation Date: {created_time}")
                print("-" * 40)
