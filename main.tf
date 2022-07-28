provider "aws" {
    region = "us-east-1"
}

resource "aws_resourcegroups_group" "test-rg" {
        name = "test-group"
        resource_query {
            query = <<JSON
{
  "ResourceTypeFilters": [
    "AWS::EC2::Instance"
  ],
  "TagFilters": [
    {
      "Key": "env",
      "Values": ["dev"]
    },
    {
        "Key": "Name",
        "Values": ["testserver"]
    }
    {
        "Key": "Name",
        "Values": ["devserver1"]
    }
  ]
}
JSON
  }
}
