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
