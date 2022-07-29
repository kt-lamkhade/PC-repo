provider "aws" {
    region = "us-east-1"
}

resource "aws_resourcegroups_group" "${var.rgname}" {
        name = "${var.rgname}"
        resource_query {
            query = <<JSON
{
  "ResourceTypeFilters": [
    "AWS::EC2::Instance"
  ],
  "TagFilters": [
    {
      "Key": "stagex_Id",
      "Values": ["${var.stagex_ID}"]
    }
  ]
}
JSON
  }
}
