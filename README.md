# Azure DevOps Operations Lab

```{=html}
<p align="center">
```
`<strong>`{=html}Cloud operations, automation, infrastructure as code,
and CI/CD in one practical project.`</strong>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img src="https://github.com/Iamaditya9/azure-devops-operations-lab/actions/workflows/ci.yml/badge.svg" alt="CI">`{=html}
`<img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/Azure-DevOps-0078D4?logo=microsoftazure&logoColor=white" alt="Azure">`{=html}
`<img src="https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform&logoColor=white" alt="Terraform">`{=html}
`<img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker">`{=html}
```{=html}
</p>
```
## About

I built this project as a hands-on Azure and DevOps operations lab
rather than a collection of disconnected examples.

It brings together a small FastAPI operations service, configuration
validation, Python and PowerShell tooling, Terraform infrastructure,
Docker, and GitHub Actions. The goal is to show how these pieces fit
together in a realistic development workflow.

The core application and tests run locally without an Azure
subscription. The Terraform and Azure REST examples are kept separate so
the repository is useful for local development while still demonstrating
how the project can connect to Azure.

------------------------------------------------------------------------

## What I built

  -----------------------------------------------------------------------
  Area                                What is included
  ----------------------------------- -----------------------------------
  API                                 FastAPI operations service with
                                      health, environment, and
                                      deployment-validation endpoints

  Automation                          Python and PowerShell scripts for
                                      environment and operational checks

  Azure                               REST API request pattern with a
                                      safe dry-run mode

  Infrastructure                      Terraform configuration for Azure
                                      resources

  Containers                          Dockerfile and Docker Compose
                                      configuration

  CI/CD                               GitHub Actions workflows for
                                      application and Terraform
                                      validation

  Testing                             API and configuration-validation
                                      tests with pytest

  Configuration                       Environment-based validation with
                                      secrets kept outside Git
  -----------------------------------------------------------------------

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Architecture`</strong>`{=html}
```{=html}
</summary>
```
``` text
                         GitHub Actions
                    test / build / validation
                              |
              +---------------+---------------+
              |                               |
          FastAPI                         Terraform
       Operations API                       Azure IaC
              |                               |
      Config Validation                 Azure Resources
              |
      Python / PowerShell
       Operations Scripts
```

The application, infrastructure, and operations tooling are
intentionally kept as separate concerns.

```{=html}
</details>
```

------------------------------------------------------------------------

## API

The FastAPI service exposes a small set of operational endpoints.

### `GET /health`

Returns a simple service health response.

``` json
{
  "status": "ok",
  "service": "operations-api"
}
```

### `GET /environment`

Checks whether the required runtime configuration is present:

-   `APP_ENV`
-   `AZURE_SUBSCRIPTION_ID`
-   `AZURE_RESOURCE_GROUP`

It reports missing configuration without requiring a live Azure
connection.

### `POST /deployments`

Validates deployment information such as service, environment, and
version.

Example:

``` json
{
  "service": "operations-api",
  "environment": "dev",
  "version": "1.0.0"
}
```

Response:

``` json
{
  "service": "operations-api",
  "environment": "dev",
  "version": "1.0.0",
  "status": "validated"
}
```

### Try it locally

`http://127.0.0.1:8000/docs`

FastAPI's Swagger UI provides an interactive way to test the endpoints.

------------------------------------------------------------------------

## Local development

### Prerequisites

-   Python 3.11+
-   Git
-   Docker Desktop
-   Terraform 1.6+
-   PowerShell 7+ for the PowerShell script

### Windows

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app
```

### macOS / Linux

``` bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app
```

Then open `http://127.0.0.1:8000/docs`.

------------------------------------------------------------------------

## Testing

Run:

``` bash
pytest -q
```

The local test suite covers the API and configuration-validation logic.

Current local validation:

``` text
5 passed
```

------------------------------------------------------------------------

## Docker

``` bash
docker build -t azure-devops-operations-lab .
docker run --rm -p 8000:8000 azure-devops-operations-lab
```

Or:

``` bash
docker compose up --build
```

------------------------------------------------------------------------

## Terraform

The Terraform module demonstrates Azure Infrastructure as Code,
including an Azure resource group and storage account.

``` bash
cd terraform
terraform init
terraform fmt -check
terraform validate
```

A real deployment requires an Azure subscription and appropriate
credentials.

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Azure / security notes`</strong>`{=html}
```{=html}
</summary>
```
Credentials are supplied through environment variables rather than
source code.

`.gitignore` excludes:

``` text
.env
.terraform/
*.tfstate
*.tfstate.*
```

The Azure REST example also defaults to dry-run behavior so it does not
unexpectedly modify cloud resources.

Never commit Azure access tokens, API keys, passwords, `.env` files, or
Terraform state.

```{=html}
</details>
```

------------------------------------------------------------------------

## Operations scripts

### Python

``` bash
python scripts/check_environment.py
python scripts/azure_rest_example.py --dry-run
```

### PowerShell

``` powershell
pwsh ./scripts/powershell/validate-environment.ps1
```

The Azure REST example reads configuration from environment variables
and requires `AZURE_ACCESS_TOKEN` only for a live request.

------------------------------------------------------------------------

## CI/CD

Two GitHub Actions workflows are included.

**Application CI** - installs dependencies - checks Python compilation -
runs tests - builds the Docker image

**Terraform workflow** - initializes Terraform - checks formatting -
validates the Terraform configuration

This keeps basic quality checks running whenever changes are pushed to
the repository.

------------------------------------------------------------------------

## Repository structure

``` text
azure-devops-operations-lab/
├── .github/workflows/
│   ├── ci.yml
│   └── terraform.yml
├── app/
│   ├── main.py
│   ├── models.py
│   └── services/config_validator.py
├── scripts/
│   ├── azure_rest_example.py
│   ├── check_environment.py
│   └── powershell/validate-environment.ps1
├── terraform/
│   ├── main.tf
│   ├── outputs.tf
│   ├── variables.tf
│   └── versions.tf
├── tests/
│   ├── test_api.py
│   └── test_config_validator.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## Why I built it

I wanted one project where I could work through the full path from
application code to operational tooling and cloud infrastructure:

**code → test → containerize → validate → automate → provision**

It is deliberately small enough to understand end-to-end, while still
using practices that carry over to larger DevOps and cloud environments.

------------------------------------------------------------------------

## Author

**Aditya Yadav**

Applied Computer Science student focused on software development, cloud,
automation, and DevOps.

-   GitHub: https://github.com/Iamaditya9
-   LinkedIn: https://www.linkedin.com/in/aditya-yadav-tech/

```{=html}
<p align="center">
```
`<sub>`{=html}Built with Python, FastAPI, Terraform, Docker, GitHub
Actions, PowerShell, and Azure.`</sub>`{=html}
```{=html}
</p>
```
