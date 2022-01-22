locals {
  subnets = {
    a = cidrsubnet(var.base_vpc_cidr, 4, 1)
    b = cidrsubnet(var.base_vpc_cidr, 4, 2)
  }
}

resource "aws_vpc" "main" {
  cidr_block = var.base_vpc_cidr

  tags = {
    Name = "weather-monitor"
  }
}

resource "aws_subnet" "main-subnets" {
  for_each            = local.subnets
  vpc_id              = aws_vpc.main.id
  cidr_block          = each.value
  availability_zone   = "eu-west-1${each.key}"

  tags = {
    Name = "weather-monitor"
  }
}
