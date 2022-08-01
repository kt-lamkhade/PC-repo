
resource "aws_resourcegroups_group" "stages_rg" {
  name = var.rg_name
  resource_query {
    query = "${"./modules/query.json"}"
  }
}