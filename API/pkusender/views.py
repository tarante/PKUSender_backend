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
        elif query_type == '1': #call_order
            return Response("call_order")
        elif query_type == '2': #help_order
            return Response("help_order")


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
            avatar_url  = req["avatar_url"]
            user = User(user_id=user_id, user_name=user_name, 
                    address=address, credit=credit, coin_num=coin_num, 
                    gender=gender, avatar_url=avatar_url)
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

        elif query_type == '15':
            user_id     = req["user_id"]
            avatar_url  = req["avatar_url"]
            User.objects.filter(user_id=user_id).update(avatar_url=avatar_url)
            return Response("avatar_url update!")

        elif query_type == '20':
            user_id     = req["user_id"]
            user_name   = req["user_name"]
            address     = req["address"]
            credit      = int(req["credit"])
            coin_num    = int(req["coin_num"])
            gender      = req["gender"]
            avatar_url  = req["avatar_url"]

            User.objects.filter(user_id=user_id).update(user_name=user_name)
            User.objects.filter(user_id=user_id).update(address=address)
            User.objects.filter(user_id=user_id).update(credit=credit)
            User.objects.filter(user_id=user_id).update(coin_num=coin_num)
            User.objects.filter(user_id=user_id).update(gender=gender)
            User.objects.filter(user_id=user_id).update(avatar_url=avatar_url)
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
        # description   = Order.objects.filter(order_id=order_id).values("description")
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
            description      = req["description"]
            secret_info     = req["secret_info"]
            comment         = req["comment"]
            star_level      = req["star_level"]
            create_time     = req["create_time"]

            caller_name = User.objects.filter(user_id=caller_id).values("user_name")
            helper_name = User.objects.filter(user_id=helper_id).values("user_name")

            order = Order(order_id=order_id, caller_id=caller_id, helper_id=helper_id, 
                caller_name=caller_name, helper_name=helper_name,
                src_address=src_address, dest_address=dest_address, order_status=order_status,
                coin_cost=coin_cost, description=description, secret_info=secret_info,
                comment=comment, star_level=star_level)
            order.save()
            order_num += 1

            return Response("order create!")

        elif query_type == '10':
            order_id        = req["order_id"]
            helper_id       = req["helper_id"]
            Order.objects.filter(order_id=order_id).update(helper_id=helper_id)
            Order.objects.filter(order_id=order_id).update(order_status=1)

            caller_id = Order.objects.filter(order_id=order_id).values("caller_id")
            caller = User.objects.get(user_id=caller_id)
            new_call_order_list = caller.values("call_order_list") + "," + order_id
            caller.update(call_order_list=new_call_order_list)

            helper = User.objects.filter(user_id=helper_id)
            helper_name = helper.values("user_name")
            Order.objects.filter(order_id=order_id).update(helper_name=helper_name)
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
            complete_time   = int(req["complete_time"])
            Order.objects.filter(order_id=order_id).update(complete_time=complete_time)
            Order.objects.filter(order_id=order_id).update(order_status=2)
            return Response("order_status update!")

        elif query_type == '14':
            order_id        = req["order_id"]
            coin_cost       = int(req["coin_cost"])
            Order.objects.filter(order_id=order_id).update(coin_cost=coin_cost)
            return Response("coin_cost update!")

        elif query_type == '15':
            order_id        = req["order_id"]
            description      = req["description"]
            Order.objects.filter(order_id=order_id).update(description=description)
            return Response("description update!")

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

        elif query_type == '19':
            order_id        = req["order_id"]
            order = Order.objects.get(order_id=order_id)

            caller_id = order.values("caller_id")
            caller = User.objects.get(user_id=caller_id)
            if caller.exists():
                caller_order_list = caller.values("call_order_list")
                order_list = caller_order_list.split(",")
                order_list.remove("order_id")
                str = ","
                new_order_list = str.join(order_list)
                caller.update(call_order_list=new_order_list)

            helper_id = order.values("helper_id")
            helper = User.objects.get(user_id=helper_id)
            if helper.exists():
                helper_order_list = helper.values("take_order_list")
                order_list = helper_order_list.split(",")
                order_list.remove("order_id")
                str = ","
                new_order_list = str.join(order_list)
                caller.update(take_order_list=new_order_list)

            order.delete()

            return Response("Order delete!")

        elif query_type == '20':
            order_id        = req["order_id"]
            caller_id       = req["caller_id"]
            helper_id       = req["helper_id"]
            caller_name     = req["caller_name"]
            helper_name     = req["helper_name"]
            src_address     = req["src_address"]
            dest_address    = req["dest_address"]
            order_status    = int(req["order_status"])
            coin_cost       = int(req["coin_cost"])
            description      = req["description"]
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
            Order.objects.filter(order_id=order_id).update(description=description)
            Order.objects.filter(order_id=order_id).update(secret_info=secret_info)
            Order.objects.filter(order_id=order_id).update(comment=comment)
            Order.objects.filter(order_id=order_id).update(star_level=star_level)

            return Response("all update!")

        return Response("type error!")


class Query_order_num(APIView):
    @staticmethod
    def get(request):
        return Response(str(order_num))