module "resource_group" {
  source       = "../modules/resource_group"
  project_name = var.project_name
  location     = var.location
}

module "storage_account" {
  source         = "../modules/storage_account"
  resource_group = module.resource_group.name
  project_name   = var.project_name
  location       = var.location
}

module "app_service_plan" {
  source         = "../modules/app_service_plan"
  resource_group = module.resource_group.name
  project_name   = var.project_name
  location       = var.location
}

module "web_app" {
  source           = "../modules/web_app"
  resource_group   = module.resource_group.name
  project_name     = var.project_name
  location         = var.location
  app_service_plan = module.app_service_plan.id
  storage_account  = module.storage_account.name
}


