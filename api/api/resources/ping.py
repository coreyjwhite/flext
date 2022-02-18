"""REST endpoint for pinging the client and returning results."""

import json
import platform
import subprocess

from flask import request
from pingparsing import PingParsing

from .base import BaseResource
from .. import db


class PingResource(BaseResource):

    path = "/ping"

    summary = "Ping the client"

    schema = {
        "type": "object",
        "properties": {
            "destination": {"type": "string"},
            "packet_transmit": {"type": "number"},
            "packet_receive": {"type": "number"},
            "packet_loss_count": {"type": "number"},
            "packet_loss_rate": {"type": "number"},
            "rtt_min": {"type": "number"},
            "rtt_avg": {"type": "number"},
            "rtt_max": {"type": "number"},
            "rtt_mdev": {"type": "number"},
            "packet_duplicate_count": {"type": "number"},
            "packet_duplicate_rate": {"type": "number"},
        },
    }

    example = {
        "destination": "192.168.1.77",
        "packet_transmit": 1,
        "packet_receive": 1,
        "packet_loss_count": 0,
        "packet_loss_rate": 0.0,
        "rtt_min": 0.016,
        "rtt_avg": 0.016,
        "rtt_max": 0.016,
        "rtt_mdev": 0.0,
        "packet_duplicate_count": 0,
        "packet_duplicate_rate": 0.0,
    }

    responses = {
        "get": {
            "tags": ["info"],
            "summary": summary,
            "description": "A successful GET request returns an object with ping results data",
            "operationId": "ping",
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
                        subprocess.run(command, stdout=subprocess.PIPE).stdout.decode(
                            "utf-8"
                        )
                    ).as_dict(),
                    indent=4,
                )
            ),
            200,
        )
