"""REST endpoint for querying Meditech administration records."""

from flask import request
from sqlalchemy import select

from .base import BaseResource
from .. import db
from ..interfaces.nws import get_hourly_forecast
from ..models.weather import Forecast
from ..utils import if_then, query_json, df_json, json_df


class AdminsResource(BaseResource):

    path = "/weather"

    summary = "Administration records"

    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date-time"},
                "location": {"type": "string"},
                "acct_number": {"type": "string"},
                "rx_number": {"type": "string"},
                "mnemonic": {"type": "string"},
                "admin_dose": {"type": "number", "format": "float"},
                "admin_dose_unit": {"type": "string"},
                "prescriber": {"type": "string"},
            },
        },
    }

    example = [
        {
            "date": "2020-21-11T06:27:00",
            "location": "3W",
            "acct_number": "E043045004",
            "rx_number": "03311143",
            "mnemonic": "DIAZ5",
            "admin_dose": 2.5,
            "admin_dose_unit": "MG",
            "prescriber": "ARANAJ",
        }
    ]

    responses = {
        "get": {
            "tags": ["transactions"],
            "summary": summary,
            "description": "A list of administration records",
            "operationId": "getAdmins",
            "produces": ["application/json"],
            "parameters": [
                {
                    "name": "encounter-id",
                    "in": "query",
                    "description": "An encounter id",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "item-id",
                    "in": "query",
                    "description": "An item mnemonic",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "location",
                    "in": "query",
                    "description": "A location identifier",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "prescriber",
                    "in": "query",
                    "description": "A prescriber user ID",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "rx-id",
                    "in": "query",
                    "description": "An RX number",
                    "required": False,
                    "schema": {"type": "string"},
                },
            ],
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
                400: {"description": "No parameters received"},
            },
        }
    }

    def post(self):

        # Return error if no query parameters
        if not request.args:
            return self.status_response("get", 400)

        # Parse parameters per responses documentation
        # pargs = self.parse_args("get", request.args)
        data = get_hourly_forecast(
            request.args["office"],
            request.args["grid_x"],
            request.args["grid_y"],
        )

        for datum in data:
            forecast = Forecast(**datum)
            db.session.add(forecast)

        query = select(Forecast)
        return query_json(query)
