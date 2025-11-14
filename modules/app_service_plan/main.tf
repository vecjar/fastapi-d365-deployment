resource "azurerm_service_plan" "asp" {
  name                = "${var.project_name}-plan"
  resource_group_name = var.resource_group
  location            = var.location
  os_type             = "Linux"
  sku_name            = "B1"
}
