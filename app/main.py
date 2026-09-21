from fastapi import FastAPI, HTTPException
from app.models import DeploymentRequest, DeploymentResponse
from app.services.config_validator import missing_variables, validate_environment

app = FastAPI(
    title="Azure DevOps Operations Lab",
    version="1.0.0",
    description="Operations API for cloud environment validation and deployment metadata.",
)


@app.get("/health")
def health():
    return {"status": "ok", "service": "operations-api"}


@app.get("/environment")
def environment_status():
    status = validate_environment()
    return {
        "ready": not missing_variables(),
        "checks": status,
        "missing": missing_variables(),
    }


@app.post("/deployments", response_model=DeploymentResponse, status_code=201)
def create_deployment(request: DeploymentRequest):
    if request.environment == "prod" and request.version == "latest":
        raise HTTPException(
            status_code=400,
            detail="Production deployments require an explicit version.",
        )

    return DeploymentResponse(
        service=request.service,
        environment=request.environment,
        version=request.version,
        status="validated",
    )
