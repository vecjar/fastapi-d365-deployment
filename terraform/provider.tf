terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}

  subscription_id = "c7b3597b-5533-4cff-a5a1-b2a326277e67"

  tenant_id       = "b41db68e-4e43-42ce-9121-a29e1dd53e32"
}

