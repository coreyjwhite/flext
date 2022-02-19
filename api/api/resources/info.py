"""REST endpoint for returning API server config and version information."""

import platform

from marshmallow import Schema, fields
import toml

from .base import BaseResource
from .. import db


class InfoSchema(Schema):
    platform = fields.String()
    machine_name = fields.String()
    python_version = fields.String()
    api_version = fields.String()
    database = fields.String()
    db_version = fields.String()


class InfoResource(BaseResource):

    path = "/info"
    schema = InfoSchema
    example = {
        "platform": "Linux-4.4.0-19041-Microsoft-x86_64-with-glibc2.29",
        "machine_name": "dev-machine",
        "python_version": "3.8.10",
        "api_version": "0.3.0",
        "database": "phetch",
        "db_version": "10.4.22-MariaDB-1:10.4.22+maria~focal-log",
    }

    operations = {
        "get": {
            "summary": "Get server configuration and version information",
            "tags": ["info"],
            "responses": {
                200: {
                    "description": "OK",
                    "content": {
                        "application/json": {
                            "schema": schema,
                            "example": example,
                        }
                    },
                }
            },
        }
    }

    def get(self):

        # Load poetry configuration data
        api_version = toml.load("pyproject.toml")["tool"]["poetry"]["version"]
        db_name = db.session.bind.url.database
        db_version = db.session.execute("SELECT VERSION()").first()[0]

        return (
            {
                "platform": platform.platform(),
                "machine_name": platform.node(),
                "python_version": platform.python_version(),
                "api_version": api_version,
                "database": db_name,
                "db_version": db_version,
            },
            200,
        )
