# Module Structure: custom domain exceptions belong in a dedicated module.
class InspectionError(Exception):
    """Device did not pass Inspection"""
    pass