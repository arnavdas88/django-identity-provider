#              This file is part of the Zeron distribution.
#               https://github.com/teamcognito-solutions
#
#                   Copyright (c) 2022 Teamcognito.
#                         --.. . .-. --- -.
#
#
# SPDX-License-Identifier: AGPL-3.0
#
#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

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