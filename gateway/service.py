import json

from marshmallow import ValidationError
from nameko import config
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http


class GatewayService(object):

    name = 'gateway'

    rpc_model_travel_distance = RpcProxy('model_travel_distance')
    rpc_model_charging_period_duration = RpcProxy('model_charging_period_duration')

    @http(
        "GET", 
        "/getTravelDistance"
    )
    def get_travel_distance(self, request):
        travel_distance = self.rpc_model_travel_distance.get_travel_distance()
        return Response(
            travel_distance,
            mimetype='application/json'
        )

    @http(
        "GET", 
        "/getChargingPeriodDuration"
    )
    def get_charging_period_duration(self, request):
        charging_period_duration = self.rpc_model_charging_period_duration.get_charging_period_duration()
        return Response(
            charging_period_duration,
            mimetype='application/json'
        )        