
resource "aws_resourcegroups_group" "stages_rg" {
  name = var.rg_name
  resource_query {
    query = <<JSON
{
  "ResourceTypeFilters": ["AWS::EC2::Instance","AWS::EC2::Volume","AWS::EC2::SecurityGroup"],
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
