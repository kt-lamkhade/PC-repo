provider "aws" {
    region = "us-east-1"
}

resource "aws_resourcegroups_group" "stages_rg" {
        name = "${var.rg_name}"
        resource_query {
            query = <<JSON
{
  "ResourceTypeFilters": [
    "AWS::EC2::Instance"
  ],
  "TagFilters": [
    {
      "Key": "stagex_Id",
      "Values": ["${var.stagex_id}"]
    }
  ]
}
JSON
  }
}
