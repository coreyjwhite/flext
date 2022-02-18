"""REST endpoint for the OpenAPI specification YAML file."""

import yaml

from .base import BaseResource
from .. import db


class OpenApiResource(BaseResource):

    path = "/openapi"

    summary = "Get the OpenAPI specification"

    schema = {
        "type": "object",
        "properties": {
            "info": {"type": "object"},
            "paths": {"type": "object"},
            "tags": {"type": "array"},
            "openapi": {"type": "string"},
        },
    }

    responses = {
        "get": {
            "summary": summary,
            "description": "The server's OpenAPI specification YAML file",
            "tags": ["info"],
            "responses": {
                200: {
                    "description": "OK",
                    "content": {"application/json": {"schema": schema}},
                }
            },
        }
    }

    def get(self):
        """Get OpenAPI spec YAML from root dir."""

        with open("openapi_spec.yaml", "r") as stream:
            data_loaded = yaml.safe_load(stream)

        return data_loaded
