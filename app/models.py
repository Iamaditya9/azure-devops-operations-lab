from pydantic import BaseModel, Field


class DeploymentRequest(BaseModel):
    service: str = Field(min_length=2, max_length=80)
    environment: str = Field(pattern="^(dev|staging|prod)$")
    version: str = Field(min_length=1, max_length=40)


class DeploymentResponse(BaseModel):
    service: str
    environment: str
    version: str
    status: str
