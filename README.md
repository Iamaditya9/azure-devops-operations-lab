# Azure DevOps Operations Lab

A production-style DevOps engineering portfolio project demonstrating cloud environment validation, Infrastructure as Code, CI/CD, Python automation, PowerShell scripting, and Azure REST API integration patterns.

The project is runnable locally without an Azure subscription. Terraform and Azure REST examples are integration-ready examples; the default API and tests use local fixtures.

## What this demonstrates

- Infrastructure as Code with Terraform
- GitHub Actions CI/CD
- Python automation and FastAPI
- PowerShell operational scripting
- Azure REST API request patterns
- Environment configuration validation
- Dockerized service delivery
- Automated unit and API tests
- Separation of application, infrastructure, and operations concerns

## Architecture

```text
                    +----------------------+
                    |     GitHub Actions    |
                    | test -> build -> lint |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
          +------v------+             +------v------+
          |   FastAPI   |             |  Terraform  |
          | Operations  |             | Azure IaC   |
          +------+------+             +------+------+
                 |                           |
          +------v------+             +------v------+
          | Config /    |             | Azure       |
          | Validation  |             | Resources   |
          +-------------+             +-------------+
                 |
        +--------+---------+
        | Python / PowerShell|
        | Operations Scripts |
        +--------------------+
```

## Local setup

### Prerequisites

- Python 3.11+
- Docker Desktop
- Terraform 1.6+
- PowerShell 7+
- Git

### Run locally

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

### Test

```bash
pytest
```

### Docker

```bash
docker build -t azure-devops-operations-lab .
docker run --rm -p 8000:8000 azure-devops-operations-lab
```

## Terraform

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
```

The module demonstrates an Azure resource group and storage account. A real deployment requires Azure credentials. Never commit secrets or Terraform state.

## Operations scripts

```bash
python scripts/check_environment.py
python scripts/azure_rest_example.py --dry-run
```

PowerShell:

```powershell
pwsh ./scripts/powershell/validate-environment.ps1
```

The Azure REST example defaults to dry-run mode so a clone cannot unexpectedly mutate cloud resources.

## CI/CD

GitHub Actions performs dependency installation, Python compilation checks, automated tests, Docker build, and Terraform validation.

## Repository structure

```text
app/                 FastAPI application and validation services
scripts/              Python and PowerShell operations tooling
terraform/            Azure Infrastructure as Code
tests/                Automated tests
.github/workflows/    CI/CD workflows
Dockerfile            Container build
docker-compose.yml    Local container orchestration
```

## Portfolio positioning

This project complements the existing `devops-service-pipeline` repository by adding Terraform, Azure-oriented operations, PowerShell, cloud API integration patterns, and environment governance rather than duplicating another basic Flask CI pipeline.

## Contact

**Aditya Yadav**  
GitHub: https://github.com/Iamaditya9  
LinkedIn: https://www.linkedin.com/in/aditya-yadav-tech/  
Email: ydaditya39@gmail.com
