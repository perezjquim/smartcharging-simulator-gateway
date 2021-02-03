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
    rpc_model_charging_period_peak = RpcProxy('model_charging_period_peak')
    rpc_model_battery_consumption = RpcProxy('model_battery_consumption')
    rpc_model_affluence = RpcProxy('model_affluence')

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

    @http(
        "GET", 
        "/getChargingPeriodPeak"
    )
    def get_charging_period_peak(self, request):
        charging_period_peak = self.rpc_model_charging_period_peak.get_charging_period_peak()
        return Response(
            charging_period_peak,
            mimetype='application/json'
        )                


    @http(
        "GET", 
        "/getFinalBatteryLevel/<int:initial_battery_level>/<string:travel_distance>"
    )
    def get_final_battery_level(self, request, initial_battery_level, travel_distance):
        final_battery_level = self.rpc_model_battery_consumption.get_final_battery_level(initial_battery_level, travel_distance)
        return Response(
            final_battery_level,
            mimetype='application/json'
        )                        

    @http(
        "GET", 
        "/getAffluence/<int:hour_of_day>"
    )
    def get_affluence(self, request, hour_of_day):
        affluence = self.rpc_model_affluence.get_affluence(hour_of_day)
        return Response(
            affluence,
            mimetype='application/json'
        )                 