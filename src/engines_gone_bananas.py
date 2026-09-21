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
@dataclass(frozen=True)
class DiagnosticReferral:
    service_request: ServiceRequest
    diagnostic_provider: str = "Master-Mechanic-AI"

def create_diagnostic_referral(req: ServiceRequest) -> DiagnosticReferral:
    if not validate_request(req):
        raise ValueError("invalid service request")
    return DiagnosticReferral(req)
@dataclass(frozen=True)
class ServiceWorkflow:
    request: ServiceRequest
    referral: DiagnosticReferral | None = None

def open_service_workflow(req: ServiceRequest, needs_diagnostics: bool = True) -> ServiceWorkflow:
    if not validate_request(req):
        raise ValueError("invalid service request")
    referral = create_diagnostic_referral(req) if needs_diagnostics else None
    return ServiceWorkflow(req, referral)
