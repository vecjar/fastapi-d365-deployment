resource "azurerm_linux_web_app" "webapp" {
  name                = "${var.project_name}-webapp"
  resource_group_name = var.resource_group
  location            = var.location
  service_plan_id     = var.app_service_plan

  site_config {
    application_stack {
      python_version = "3.10"
    }
  }

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
    "STORAGE_ACCOUNT_NAME"     = var.storage_account
  }
}