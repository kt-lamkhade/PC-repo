provider "aws" {
  region = "us-east-1"
}

variable "stagex_id" {
  type = string
}

module "aws_resourcegroups_group" {
  source    = "./modules/"
  stagex_id = var.stagex_id
  rg_name   = format("%s_rg", var.stagex_id)
}