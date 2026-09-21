# Azure DevOps Operations Lab

**A practical DevOps lab covering Azure, Terraform, Docker, CI/CD, automation, and operational APIs.**

[![CI](https://github.com/Iamaditya9/azure-devops-operations-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/Iamaditya9/azure-devops-operations-lab/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-DevOps-0078D4?logo=microsoftazure&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)

---

## 📌 Quick Navigation

[About](#about) · [What I Built](#what-i-built) · [Architecture](#architecture) · [API](#api) · [Setup](#local-setup) · [Testing](#testing) · [Docker](#docker) · [Terraform](#terraform) · [CI/CD](#cicd) · [Project Structure](#project-structure)

---

## About

I built this project as a hands-on Azure and DevOps operations lab rather than a collection of disconnected examples.

The project brings together a small FastAPI operations service, environment validation, Python and PowerShell tooling, Terraform infrastructure, Docker, and GitHub Actions.

The goal was to work through a practical development flow:

**code → test → containerize → validate → automate → provision**

The API and tests can run locally without an Azure subscription. The Terraform and Azure REST examples are kept separate so the project can be explored without requiring live cloud access.

---

## ⚙️ What I Built

| Area | Implementation |
|---|---|
| **Operations API** | FastAPI service for health, environment, and deployment validation |
| **Automation** | Python and PowerShell operational scripts |
| **Azure Integration** | Azure REST API request pattern with dry-run support |
| **Infrastructure** | Terraform configuration for Azure resources |
| **Containers** | Dockerfile and Docker Compose |
| **CI/CD** | GitHub Actions for application and Terraform validation |
| **Testing** | Pytest API and configuration tests |
| **Configuration** | Environment-based validation with secrets kept outside Git |

---

## 🏗️ Architecture

```text
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

---

## 🔎 API

The FastAPI service provides a small operational API that can be explored through Swagger UI.

### `GET /health`

Basic service health check.

```json
{
  "status": "ok",
  "service": "operations-api"
}
```

### `GET /environment`

Checks whether the required runtime configuration is present:

- `APP_ENV`
- `AZURE_SUBSCRIPTION_ID`
- `AZURE_RESOURCE_GROUP`

The endpoint reports missing configuration without requiring a live Azure connection.

### `POST /deployments`

Validates deployment information such as service, environment, and version.

Example request:

```json
{
  "service": "operations-api",
  "environment": "dev",
  "version": "1.0.0"
}
```

Example response:

```json
{
  "service": "operations-api",
  "environment": "dev",
  "version": "1.0.0",
  "status": "validated"
}
```

### Try It Locally

Start the API and open:

**http://127.0.0.1:8000/docs**

FastAPI's Swagger UI provides an interactive way to send requests and inspect responses.

---

## 🚀 Local Setup

### Prerequisites

- Python 3.11+
- Git
- Docker Desktop
- Terraform 1.6+
- PowerShell 7+

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app
```

Then open:

**http://127.0.0.1:8000/docs**

---

## 🧪 Testing

Run the test suite:

```bash
pytest -q
```

The project includes API and configuration-validation tests.

Current local test result:

```text
5 passed
```

---

## 🐳 Docker

Build the application image:

```bash
docker build -t azure-devops-operations-lab .
```

Run it locally:

```bash
docker run --rm -p 8000:8000 azure-devops-operations-lab
```

Or use Docker Compose:

```bash
docker compose up --build
```

---

## ☁️ Terraform

The Terraform configuration demonstrates Infrastructure as Code for Azure resources.

From the Terraform directory:

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
```

A real Azure deployment requires an Azure subscription and appropriate credentials.

### Security

Credentials are supplied through environment variables rather than source code.

The repository ignores:

```text
.env
.terraform/
*.tfstate
*.tfstate.*
```

Never commit:

- Azure access tokens
- API keys
- passwords
- `.env` files
- Terraform state

The Azure REST example supports dry-run execution so requests can be tested without making live changes.

---

## 🛠️ Operations Scripts

### Python

Check the local environment:

```bash
python scripts/check_environment.py
```

Run the Azure REST example in dry-run mode:

```bash
python scripts/azure_rest_example.py --dry-run
```

### PowerShell

```powershell
pwsh ./scripts/powershell/validate-environment.ps1
```

These scripts provide operational checks that can be run independently of the API.

---

## 🔄 CI/CD

GitHub Actions is used to automate application and infrastructure validation.

### Application CI

The application workflow:

1. Installs Python dependencies
2. Checks Python compilation
3. Runs the automated tests
4. Builds the Docker image

### Terraform Validation

The Terraform workflow:

1. Initializes Terraform
2. Checks Terraform formatting
3. Validates the Terraform configuration

This keeps application and infrastructure changes covered by automated checks.

---

## 📁 Project Structure

```text
azure-devops-operations-lab/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── terraform.yml
├── app/
│   ├── main.py
│   ├── models.py
│   └── services/
│       └── config_validator.py
├── scripts/
│   ├── azure_rest_example.py
│   ├── check_environment.py
│   └── powershell/
│       └── validate-environment.ps1
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

---

## 💡 Why I Built It

I wanted one project where I could work through the path from application code to operational tooling and cloud infrastructure.

Instead of building another standalone API or a basic CI pipeline, I wanted the pieces to work together:

**application → tests → container → CI → infrastructure → cloud operations**

The result is a small end-to-end lab that gives me practical experience with application development, automation, Infrastructure as Code, containers, and CI/CD.

---

## 👤 Author

**Aditya Yadav**

Applied Computer Science student focused on software development, cloud, automation, and DevOps.

- GitHub: [Iamaditya9](https://github.com/Iamaditya9)
- LinkedIn: [Aditya Yadav](https://www.linkedin.com/in/aditya-yadav-tech/)
