provider "aws" {
    region = "us-east-1"
}

variable "rg_name" {
    type = string
}
variable "stagex_id" {
    type = string
}

resource "aws_resourcegroups_group" "stages_rg" {
        name = "${var.rg_name}"
        resource_query {
            query = <<JSON
{
  "ResourceTypeFilters": [
    "AWS::EC2::Instance"
  ],
  [
    "AWS::EC2::Volume"
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
