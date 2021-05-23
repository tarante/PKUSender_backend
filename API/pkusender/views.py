from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .models import Order

import json

global order_num
order_num = 0


class QueryUser(APIView):
    @staticmethod
    def get(request):

        req = request.query_params.dict() 
        user_id = req["user_id"]
        query_type = req["type"]

        data = User.objects.filter(user_id=user_id).values()
        data = list(data)

        if query_type == '0': #user_info
            return Response(json.dumps(data))
        elif query_type == '1': #order_info
            return Response("order")


        return Response("type error!")

    @staticmethod
    def post(request):
        """
        """
        req = request.data

        query_type  = req["type"]

        if query_type == '0':
            user_id     = req["user_id"]
            user_name   = req["user_name"]
            address     = req["address"]
            credit      = int(req["credit"])
            coin_num    = int(req["coin_num"])
            gender      = req["gender"]
            user = User(user_id=user_id, user_name=user_name, 
                    address=address, credit=credit, coin_num=coin_num, 
                    gender=gender)
            user.save()

        elif query_type == '10':
            user_id     = req["user_id"]
            user_name   = req["user_name"]
            User.objects.filter(user_id=user_id).update(user_name=user_name)
            return Response("all update!")

        elif query_type == '11':
            user_id     = req["user_id"]
            address     = req["address"]
            User.objects.filter(user_id=user_id).update(address=address)
            return Response("address update!")

        elif query_type == '12':
            user_id     = req["user_id"]
            credit      = int(req["credit"])
            User.objects.filter(user_id=user_id).update(credit=credit)
            return Response("credit update!")

        elif query_type == '13':
            user_id     = req["user_id"]
            coin_num    = int(req["coin_num"])
            User.objects.filter(user_id=user_id).update(coin_num=coin_num)
            return Response("coin_num update!")

        elif query_type == '14':
            user_id     = req["user_id"]
            gender      = req["gender"]
            User.objects.filter(user_id=user_id).update(gender=gender)
            return Response("gender update!")

        elif query_type == '20':
            user_id     = req["user_id"]
            user_name   = req["user_name"]
            address     = req["address"]
            credit      = int(req["credit"])
            coin_num    = int(req["coin_num"])
            gender      = req["gender"]

            User.objects.filter(user_id=user_id).update(user_name=user_name)
            User.objects.filter(user_id=user_id).update(address=address)
            User.objects.filter(user_id=user_id).update(credit=credit)
            User.objects.filter(user_id=user_id).update(coin_num=coin_num)
            User.objects.filter(user_id=user_id).update(gender=gender)
            return Response("all update!")

        return Response("type error!")#不需要返回数据



class QueryOrder(APIView):
    @staticmethod
    def get(request):
        """
        """
        req = request.query_params.dict()
        order_id = req["order_id"]

        # caller_id 	 = Order.objects.filter(order_id=order_id).values("caller_id")
        # helper_id 	 = Order.objects.filter(order_id=order_id).values("helper_id")
        # src_address  = Order.objects.filter(order_id=order_id).values("src_address")
        # dest_address = Order.objects.filter(order_id=order_id).values("dest_address")
        # coin_cost 	 = Order.objects.filter(order_id=order_id).values("coin_cost")
        # descrption   = Order.objects.filter(order_id=order_id).values("descrption")
        # secret_info  = Order.objects.filter(order_id=order_id).values("secret_info")
        # order_status = Order.objects.filter(order_id=order_id).values("order_status")
        # comment      = Order.objects.filter(order_id=order_id).values("comment")
        # star_level   = Order.objects.filter(order_id=order_id).values("star_level")

        data = User.objects.filter(order_id=order_id).values()
        data = list(data)

        return Response(json.dumps(data))


    @staticmethod
    def post(request):
        """
        """
        req = request.data 
        query_type      = req["type"]

        if query_type == '0':
            
            order_id        = req["order_id"]
            caller_id       = req["caller_id"]
            helper_id       = req["helper_id"]
            src_address     = req["src_address"]
            dest_address    = req["dest_address"]
            order_status    = int(req["order_status"])
            coin_cost       = int(req["coin_cost"])
            descrption      = req["descrption"]
            secret_info     = req["secret_info"]
            comment         = req["comment"]
            star_level      = req["star_level"]

            order = Order(order_id=order_id, caller_id=caller_id, helper_id=helper_id, 
                src_address=src_address, dest_address=dest_address, order_status=order_status,
                coin_cost=coin_cost, descrption=descrption, secret_info=secret_info,
                comment=comment, star_level=star_level)
            order.save()
            order_num += 1
            return Response("order create!")

        elif query_type == '10':
            order_id        = req["order_id"]
            helper_id       = req["helper_id"]
            Order.objects.filter(order_id=order_id).update(helper_id=helper_id)

            caller_id = Order.objects.filter(order_id=order_id).values("caller_id")
            caller = User.objects.get(user_id=caller_id)
            new_call_order_list = caller.values("call_order_list") + "," + order_id
            caller.update(call_order_list=new_call_order_list)

            helper = User.objects.filter(user_id=helper_id)
            new_help_order_list = helper.values("help_order_list") + "," + order_id
            helper.update(help_order_list=new_help_order_list)

            return Response("helper_id update!")

        elif query_type == '11':
            order_id        = req["order_id"]
            src_address     = req["src_address"]
            Order.objects.filter(order_id=order_id).update(src_address=src_address)
            return Response("src_address update!")

        elif query_type == '12':
            order_id        = req["order_id"]
            dest_address    = req["dest_address"]
            Order.objects.filter(order_id=order_id).update(dest_address=dest_address)
            return Response("dest_address update!")

        elif query_type == '13':
            order_id        = req["order_id"]
            order_status    = int(req["order_status"])
            Order.objects.filter(order_id=order_id).update(order_status=order_status)
            return Response("order_status update!")

        elif query_type == '14':
            order_id        = req["order_id"]
            coin_cost       = int(req["coin_cost"])
            Order.objects.filter(order_id=order_id).update(coin_cost=coin_cost)
            return Response("coin_cost update!")

        elif query_type == '15':
            order_id        = req["order_id"]
            descrption      = req["descrption"]
            Order.objects.filter(order_id=order_id).update(descrption=descrption)
            return Response("descrption update!")

        elif query_type == '16':
            order_id        = req["order_id"]
            secret_info     = req["secret_info"]
            Order.objects.filter(order_id=order_id).update(secret_info=secret_info)
            return Response("secret_info update!")

        elif query_type == '17':
            order_id        = req["order_id"]
            comment         = req["comment"]
            Order.objects.filter(order_id=order_id).update(comment=comment)
            return Response("comment update!")

        elif query_type == '18':
            order_id        = req["order_id"]
            star_level      = req["star_level"]
            Order.objects.filter(order_id=order_id).update(star_level=star_level)
            return Response("star_level update!")

        elif query_type == '20':
            order_id        = req["order_id"]
            caller_id       = req["caller_id"]
            helper_id       = req["helper_id"]
            src_address     = req["src_address"]
            dest_address    = req["dest_address"]
            order_status    = int(req["order_status"])
            coin_cost       = int(req["coin_cost"])
            descrption      = req["descrption"]
            secret_info     = req["secret_info"]
            comment         = req["comment"]
            star_level      = req["star_level"]

            Order.objects.filter(order_id=order_id).update(star_level=star_level)
            Order.objects.filter(order_id=order_id).update(caller_id=caller_id)
            Order.objects.filter(order_id=order_id).update(helper_id=helper_id)
            Order.objects.filter(order_id=order_id).update(src_address=src_address)
            Order.objects.filter(order_id=order_id).update(dest_address=dest_address)
            Order.objects.filter(order_id=order_id).update(order_status=order_status)
            Order.objects.filter(order_id=order_id).update(coin_cost=coin_cost)
            Order.objects.filter(order_id=order_id).update(descrption=descrption)
            Order.objects.filter(order_id=order_id).update(secret_info=secret_info)
            Order.objects.filter(order_id=order_id).update(comment=comment)
            Order.objects.filter(order_id=order_id).update(star_level=star_level)

            return Response("all update!")

        return Response("type error!")


class Query_order_num(APIView):
    @staticmethod
    def get(request):
        return Response(str(order_num))