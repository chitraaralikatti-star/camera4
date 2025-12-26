from camera import CameraResourceManager

def test_approved_when_capacity_available():
    manager = CameraResourceManager()
    manager.allocate_existing(3)
    assert manager.allocation_decision(4, "LOW") == "APPROVED"


def test_conditionally_approved_for_high_priority():
    manager = CameraResourceManager()
    manager.allocate_existing(9)
    assert manager.allocation_decision(2, "HIGH") == "CONDITIONALLY APPROVED"


def test_rejected_when_capacity_exceeded():
    manager = CameraResourceManager()
    manager.allocate_existing(8)
    assert manager.allocation_decision(5, "LOW") == "REJECTED"
