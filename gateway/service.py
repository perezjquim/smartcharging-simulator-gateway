import json

from marshmallow import ValidationError
from nameko import config
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http
from gateway.exceptions import OrderNotFound, ProductNotFound


class GatewayService(object):

    name = 'gateway'

    rpc_model_travel_distance = RpcProxy('model_travel_distance')

    @http(
        "GET", 
        "/getTravelDistance",
        expected_exceptions=ProductNotFound
    )
    def get_travel_distance(self, request):
        travel_distance = self.rpc_model_travel_distance.get_travel_distance()
        return Response(
            travel_distance,
            mimetype='application/json'
        )