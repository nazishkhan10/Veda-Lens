"""
Custom exception hierarchy for VedaLens.
Maps domain exceptions directly to standard HTTP status codes.
"""
from __future__ import annotations

class VedaLensBaseException(Exception):
    """Base exception for all VedaLens errors."""
    status_code: int = 400

class NotFoundError(VedaLensBaseException):
    """Resource not found."""
    status_code: int = 404

class UnauthorizedError(VedaLensBaseException):
    """Authentication failed or missing."""
    status_code: int = 401

class ForbiddenError(VedaLensBaseException):
    """Insufficient permissions."""
    status_code: int = 403

class ValidationError(VedaLensBaseException):
    """Data validation failed."""
    status_code: int = 422

class ConflictError(VedaLensBaseException):
    """Resource conflict."""
    status_code: int = 409

# Backward compatibility alias
VedaLensBaseException = VedaLensBaseException

class InternalError(VedaLensBaseException):
    """Internal server error."""
    status_code: int = 500
