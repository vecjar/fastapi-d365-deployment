resource "azurerm_storage_account" "sa" {
  name                     = "${var.project_name}sa"
  resource_group_name      = var.resource_group
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
