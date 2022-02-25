"""REST endpoint for pinging the client and returning results."""

import json
import platform
import subprocess

from flask import request
from marshmallow import Schema, fields
from pingparsing import PingParsing

from .base import BaseResource
from .. import db


class PingSchema(Schema):
    destination = fields.Str(example="192.168.1.77")
    packet_transmit = fields.Int(example=1)
    packet_receive = fields.Int(example=1)
    packet_loss_count = fields.Int(example=0)
    packet_loss_rate = fields.Float(example=0.0)
    rtt_min = fields.Float(example=0.016)
    rtt_avg = fields.Float(example=0.016)
    rtt_max = fields.Float(example=0.016)
    rtt_mdev = fields.Float(example=0.0)
    packet_duplicate_count = fields.Int(example=0)
    packet_duplicate_rate = fields.Float(example=0.0)


class PingResource(BaseResource):

    path = "/ping"
    schema = PingSchema
    operations = {
        "get": {
            "tags": ["info"],
            "summary": "Ping the client",
            "responses": {
                200: {
                    "description": "OK",
                    "content": {"application/json": {"schema": schema}},
                }
            },
        }
    }

    def get(self):
        """Ping the requesting client's address and return the resutls data."""

        host = request.remote_addr
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        ping_parser = PingParsing()

        return (
            json.loads(
                json.dumps(
                    ping_parser.parse(
                        subprocess.run(
                            command, stdout=subprocess.PIPE
                        ).stdout.decode("utf-8")
                    ).as_dict(),
                    indent=4,
                )
            ),
            200,
        )
