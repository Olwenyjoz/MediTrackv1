from enum import Enum


class UserRole(str, Enum):
    ADMIN = "Admin"
    DOCTOR = "Doctor"
    RECEPTIONIST = "Receptionist"
    NURSE = "Nurse"


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class AppointmentStatus(str, Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class VisitStatus(str, Enum):
    WAITING = "Waiting"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class AccountStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"