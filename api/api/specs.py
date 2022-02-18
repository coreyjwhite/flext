"""Initialization of APISpec with info from BaseResource subclasses and tags."""

import toml

from apispec import APISpec

from .resources import BaseResource

# Load data from tool.poetry section of the pyproject.toml file
pyproject = toml.load("pyproject.toml")["tool"]["poetry"]

# Initialize APISpec info object with poetry fields
spec = APISpec(
    title=pyproject["name"],
    version=pyproject["version"],
    openapi_version="3.0.2",
    info=dict(
        description=pyproject["description"],
        license=pyproject["license"],
        servers={"url": pyproject["urls"]["api"]},
    ),
)

# List and describe tags
tags = []

# Append each resource to spec paths object, sorted by path
for cls in sorted(
    BaseResource.__subclasses__(), key=lambda instance: instance.path
):
    spec.path(
        path=cls.path,
        description=cls.description if cls.description else None,
        operations=cls.responses if cls.responses else None,
    )

# Append tags to spec root object
for tag in tags:
    spec.tag(tag)


def add_specs():
    """Dump OpenAPI spec as yaml file for client consumption."""

    f = open("openapi_spec.yaml", "w")
    f.write(spec.to_yaml(yaml_dump_kwargs={"sort_keys": False}))
    f.close()
