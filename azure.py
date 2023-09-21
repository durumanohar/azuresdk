import os
from datetime import datetime, timedelta
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Your Azure subscription ID and resource group name
subscription_id = 'YOUR_SUBSCRIPTION_ID'
resource_group_name = 'YOUR_RESOURCE_GROUP_NAME'

# Initialize Azure credentials
credential = DefaultAzureCredential()

# Initialize the Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Calculate the date two weeks ago
two_weeks_ago = datetime.utcnow() - timedelta(days=14)

# List resources in the specified resource group
resources = resource_client.resources.list_by_resource_group(resource_group_name)

# Filter and print resources older than two weeks
for resource in resources:
    if resource.tags is not None and 'createdDate' in resource.tags:
        created_date = datetime.strptime(resource.tags['createdDate'], '%Y-%m-%d %H:%M:%S.%f')
        if created_date < two_weeks_ago:
            print(f"Resource Name: {resource.name}")
            print(f"Resource Type: {resource.type}")
            print(f"Resource Location: {resource.location}")
            print(f"Created Date: {created_date}")
            print("=" * 50)

