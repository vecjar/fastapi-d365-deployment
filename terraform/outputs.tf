output "resource_group" {
  value = module.resource_group.name
}

output "webapp_url" {
  value = module.web_app.url
}

output "app_service_plan_id" {
  value = module.app_service_plan.id
}

output "app_service_plan_name" {
  value = module.app_service_plan.name
}
