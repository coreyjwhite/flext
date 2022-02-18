"""REST endpoint for root path to return path directory."""

from collections import OrderedDict

from .base import BaseResource
from ..utils import get_all_subclasses


class RootResource(BaseResource):

    path = "/"

    summary = "Get a directory of API paths"

    schema = {"type": "object", "properties": {"path": {"type": "string"}}}

    example = {
        "/": "Get a directory of API paths",
        "/info": "Get server configuration and version information",
        "/openapi": "Get the OpenAPI specification",
        "/ping": "Ping the client",
    }

    responses = {
        "get": {
            "tags": ["info"],
            "summary": summary,
            "description": "",
            "operationId": "getDirectory",
            "produces": ["application/json"],
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
