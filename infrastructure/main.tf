terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

terraform {
  backend "s3" {
    bucket = "weather-monitor-terraform"
    key    = "weather-monitor-terraoform"
    region = "eu-west-1"
  }
}