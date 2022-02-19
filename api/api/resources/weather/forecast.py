"""REST endpoint for querying Meditech administration records."""

from flask import jsonify, request
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import select
from webargs.flaskparser import use_args, use_kwargs

from ..base import BaseResource
from ... import db
from ...interfaces.nws import get_hourly_forecast
from ...models.weather import Forecast
from ...utils import if_then, query_json, df_json, json_df


class ForecastSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Forecast
        include_relationships = True
        load_instance = True


class ForecastRequestSchema(Schema):
    office = fields.Str(example="description for a field")
    grid_x = fields.Int()
    grid_y = fields.Int()


class ForecastResource(BaseResource):

    path = "/weather/forecast"
    summary = "Weather forecast data"

    schema = ForecastSchema
    req_schema = ForecastRequestSchema

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

    operations = {
        "post": {
            "tags": ["transactions"],
            "summary": summary,
            "description": "A list of administration records",
            "parameters": [{"in": "query", "schema": ForecastRequestSchema}],
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

    @use_args(ForecastRequestSchema(), location="query")
    def post(self, args):

        # Return error if no query parameters
        if not request.args:
            return self.status_response("post", 400)

        # Parse parameters per operations documentation
        # pargs = self.parse_args("get", request.args)
        data = get_hourly_forecast(**args)

        for datum in data:
            forecast = Forecast(**datum)
            db.session.add(forecast)

        users = db.session.execute(select(Forecast))
        data = ForecastSchema().dump(users, many=True)
        return jsonify({"users": data})
