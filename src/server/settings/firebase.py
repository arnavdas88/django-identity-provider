import os, warnings

from firebase_admin import credentials, initialize_app

# Optional ONLY IF you have initialized a firebase app already:
# Visit https://firebase.google.com/docs/admin/setup/#python
# for more options for the following:
# Store an environment variable called GOOGLE_APPLICATION_CREDENTIALS
# which is a path that point to a json file with your credentials.
# Additional arguments are available: credentials, options, name

if os.path.exists('./google_cloud_fcm_credentials.json'):
    # To learn more, visit the docs here:
    # https://cloud.google.com/docs/authentication/getting-started
    cred = credentials.Certificate('google_cloud_fcm_credentials.json')
    FIREBASE_APP = initialize_app(cred)
else:
    warnings.warn("No Firebase Found")
    FIREBASE_APP = None