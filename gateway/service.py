import json

from marshmallow import ValidationError
from nameko import config
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http

class GatewayService(object):

    name = 'gateway_energysim'

    rpc_model_travel_distance = RpcProxy( 'model_energysim_travel_distance' )
    rpc_model_charging_period_duration = RpcProxy( 'model_energysim_charging_period_duration' )
    rpc_model_charging_period_energy_spent = RpcProxy( 'model_energysim_charging_period_energy_spent' )
    rpc_model_travel_final_battery_level = RpcProxy( 'model_energysim_travel_final_battery_level' )
    rpc_model_travel_affluence = RpcProxy( 'model_energysim_travel_affluence' )

    @http(
        "GET", 
        "/travel/distance"
    )
    def get_travel_distance( self, request ):
        travel_distance = self.rpc_model_travel_distance.get_distance( )
        return Response(
            travel_distance,
            mimetype='application/json'
        )

    @http(
        "GET", 
        "/charging_period/duration"
    )
    def get_charging_period_duration( self, request ):
        charging_period_duration = self.rpc_model_charging_period_duration.get_duration( )
        return Response(
            charging_period_duration,
            mimetype='application/json'
        )        

    @http(
        "GET", 
        "/charging_period/energy_spent/<string:charging_progress>"
    )
    def get_charging_period_energy_spent( self, request, charging_progress ):
        charging_period_peak = self.rpc_model_charging_period_energy_spent.get_energy_spent( charging_progress )
        return Response(
            charging_period_peak,
            mimetype='application/json'
        )                


    @http(
        "GET", 
        "/travel/final_battery_level/<string:initial_battery_level>/<string:travel_distance>"
    )
    def get_final_battery_level( self, request, initial_battery_level, travel_distance ):
        final_battery_level = self.rpc_model_travel_final_battery_level.get_final_battery_level( initial_battery_level, travel_distance )
        return Response(
            final_battery_level,
            mimetype='application/json'
        )                        

    @http(
        "GET", 
        "/travel/affluence/<string:hour_of_day>"
    )
    def get_affluence( self, request, hour_of_day ):
        affluence = self.rpc_model_travel_affluence.get_affluence( hour_of_day )
        return Response(
            affluence,
            mimetype='application/json'
        )                 