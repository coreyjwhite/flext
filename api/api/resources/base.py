"""Extension of Flask-RESTful Resource class with custom methods and attributes."""

from flask_restful import Resource
import toml

http_status_codes = {
    "200": "OK",
    "201": "Created",
    "202": "Accepted",
    "204": "No Content",
    "301": "Moved Permanently",
    "302": "Found",
    "307": "Temporary Redirect",
    "400": "Bad Request",
    "401": "Unauthorized",
    "403": "Forbidden",
    "404": "Not Found",
    "405": "Method Not Allowed",
    "415": "Unsupported Media Type",
    "500": "Internal Server Error",
    "501": "Not Implemented",
    "502": "Bad Gateway",
    "503": "Service Unavailable",
    "504": "Gateway Time-out",
    "511": "Network Authentication Required",
}


# TODO jsonschema validator
class BaseResource(Resource):

    path = ""  # For OpenAPI spec. For Flask routing, use get_path()
    summary = None
    description = None
    schema = {"type": "object", "properties": {}}
    example = {"example": False}
    responses = None

    # Make hostname available for links in responses
    host = toml.load("pyproject.toml")["tool"]["poetry"]["urls"]["api"]

    # Default empty endpoint return
    def get(self):
        """Return '405' Method not available"""
        return BaseResource.status_response("get", 405, message="See description.")

    # Replace any {} in OpenAPI documentation wtih <> for Flask
    @classmethod
    def get_path(cls):
        """Return a path with angle bracketed parameter for Flask routing."""
        trans = cls.path.maketrans("{}", "<>")
        return cls.path.translate(trans)

    # Parse request args object per OpenAPI response parameters documentation
    @classmethod
    def parse_args(cls, method, args):
        """Return an object of response.method parameters with supplied args."""
        parameters = [field["name"] for field in cls.responses[method]["parameters"]]
        return {param: args.get(param) for param in parameters}

    # Return status messages per OpenAPI response documentation
    @classmethod
    def status_response(cls, method, status_code, message=None, payload=None):
        """Return standard HTTP response code and description."""
        if payload:
            response = payload
        else:
            response = {
                "status": status_code,
                "description": http_status_codes[str(status_code)],
                "message": message or cls.responses[method]["responses"][status_code],
            }
        return response, status_code
