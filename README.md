FastAPI Deployment With Dataverse Integration
Overview

This project demonstrates a full automated deployment of a FastAPI application integrated with Microsoft Dataverse. The app is containerized with Docker, deployed using Azure DevOps CI/CD, and the infrastructure is provisioned with Terraform.
The FastAPI app connects to Dataverse (Dynamics 365) via Microsoft Graph using delegated permissions to retrieve Accounts records.

Components
1. FastAPI Application

Provides API endpoints including /accounts to read data from Dataverse.

Uses OAuth2 delegated authentication (Azure AD App Registration).

Stores config and secrets as environment variables.

2. Dataverse Integration

Connects to a Dataverse environment using Microsoft Graph.

Retrieves records from the Accounts table.

Requires the user_impersonation delegated permission.

3. Terraform

Provisions Azure infrastructure:

Resource Group

App Service Plan

Azure Web App (Docker-based)

Manages configuration and environment variables.

Ensures repeatable and consistent deployments.

4. Docker

Packages the FastAPI app and dependencies into a single container image.

Guarantees consistent behavior across local dev, CI, and production.

5. Azure DevOps

CI Pipeline: Builds the Docker image and installs dependencies on commit.

CD Pipeline: Runs Terraform apply and deploys the updated container to Azure Web Apps.

Architecture

FastAPI container → Azure Web App (Linux)

Terraform → Manages all cloud resources

Azure DevOps → Fully automated build + deploy

FastAPI → Connects to Dataverse using Microsoft Graph

Project Workflow

Terraform provisions the Azure Web App and environment.

Docker builds the FastAPI app into a container image.

CI pipeline builds and validates the image on commit.

CD pipeline deploys the container and applies Terraform changes.

FastAPI retrieves Dataverse Accounts data through Graph API.

Purpose

The goal of this project is to demonstrate my ability to combine:

Infrastructure-as-code

Containerization

CI/CD automation

Secure Dataverse API integration

Key Things Learned

How to provision Azure Web Apps with Terraform

How to containerize and deploy FastAPI with Docker

How to build automated CI/CD pipelines in Azure DevOps

How to authenticate and read data from Dataverse using Graph API