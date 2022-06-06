# MFA Settings
MFA_ISSUER_NAME = 'Zeron : Re-Imagining Cyber Security with the power of AI'
MFA_RECOVERY_CODE_LENGTH = 16
MFA_REMEMBER_MY_BROWSER = False
MFA_REMEMBER_DAYS = 7

from server.settings.default import MIDDLEWARE

MIDDLEWARE += [
    # Multi-Factor Authentication
    'django_mfa.middleware.MfaMiddleware'
]