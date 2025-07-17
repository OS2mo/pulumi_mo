#!/bin/bash
# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0

USERNAME=${FASTRAMQPI__DATABASE__USER}
PASSWORD=${FASTRAMQPI__DATABASE__PASSWORD}
HOST=${FASTRAMQPI__DATABASE__HOST}
NAME=${FASTRAMQPI__DATABASE__NAME}

export PULUMI_CONFIG_PASSPHRASE="hunter2"

pulumi login "postgres://${USERNAME}:${PASSWORD}@${HOST}:5432/${NAME}?sslmode=disable"
pulumi stack select test --create --non-interactive

pulumi preview
