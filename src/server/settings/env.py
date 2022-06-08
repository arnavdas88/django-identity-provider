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

import os

PREFIX = 'ZERON_'

env_var = os.environ
variables = dict(env_var).keys()

zeron_configurations = [ variable for variable in variables if str(variable).startswith(PREFIX) ]

for conf in zeron_configurations:
    key = "_".join(conf.split("_")[1:])
    value = os.environ.get(conf)

    globals()[key] = value