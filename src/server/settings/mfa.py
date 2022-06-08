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