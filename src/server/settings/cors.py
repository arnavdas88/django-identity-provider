from server.settings.default import DEBUG

if DEBUG:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"http://*",
        r"https://*"
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https:\/\/\w+\.zeron\.one$",
        r"^http:\/\/\w+\.zeron\.one$"
    ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]

from server.settings.default import MIDDLEWARE
MIDDLEWARE += [
    # Django CORS Headers
    'corsheaders.middleware.CorsMiddleware',
]
