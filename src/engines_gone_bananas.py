from dataclasses import dataclass

@dataclass(frozen=True)
class ServiceRequest:
    customer_id: str
    vehicle_id: str
    concern: str

def master_mechanic_dependency() -> str:
    return "Master-Mechanic-AI"

def validate_request(req: ServiceRequest) -> bool:
    return bool(req.customer_id.strip() and req.vehicle_id.strip() and req.concern.strip())
