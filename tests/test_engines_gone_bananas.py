from engines_gone_bananas import ServiceRequest, master_mechanic_dependency, validate_request

def test_service_request_requires_core_fields():
    assert validate_request(ServiceRequest("c1","v1","no-start"))
    assert not validate_request(ServiceRequest("","v1","no-start"))

def test_master_mechanic_is_external_dependency():
    assert master_mechanic_dependency()=="Master-Mechanic-AI"
def test_diagnostic_referral_preserves_external_boundary():
    from engines_gone_bananas import ServiceRequest, create_diagnostic_referral
    referral=create_diagnostic_referral(ServiceRequest("c1","v1","misfire"))
    assert referral.diagnostic_provider=="Master-Mechanic-AI"
def test_service_workflow_routes_diagnostics_without_absorbing_provider():
    from engines_gone_bananas import ServiceRequest, open_service_workflow
    workflow=open_service_workflow(ServiceRequest("c1","v1","rough idle"))
    assert workflow.referral is not None
    assert workflow.referral.diagnostic_provider=="Master-Mechanic-AI"
