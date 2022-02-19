"""REST endpoint for root path to return path directory."""

from collections import OrderedDict

from marshmallow import Schema, fields

from .base import BaseResource
from ..utils import get_all_subclasses


class RootSchema(Schema):
    path = fields.Dict()


class RootResource(BaseResource):

    path = "/"
    schema = RootSchema
    example = {
        "/": "Get a directory of API paths",
        "/info": "Get server configuration and version information",
        "/openapi": "Get the OpenAPI specification",
        "/ping": "Ping the client",
    }

    operations = {
        "get": {
            "tags": ["info"],
            "summary": "Get a directory of API paths",
            "responses": {
                200: {
                    "description": "OK",
                    "content": {
                        "application/json": {
                            "schema": schema,
                            "example": example,
                        }
                    },
                },
                404: {"description": "Item not found"},
            },
        }
    }

    def get(self):
        """Return an object of endpoints which have response OpenAPI documentation."""

        return {
            resource.path: resource.summary
            for resource in sorted(
                get_all_subclasses(BaseResource),
                key=lambda instance: instance.path,
            )
            if resource.responses is not None
        }
