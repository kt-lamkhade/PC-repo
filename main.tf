provider "aws" {
  region = "us-east-1"
}

variable "rg_name" {
  type = string
}
variable "stagex_id" {
  type = string
}

module "aws_resourcegroups_group" {
  source = "./modules/"
}