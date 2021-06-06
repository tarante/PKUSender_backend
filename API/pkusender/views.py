from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .models import Order
from .models import Order_wait
from .models import Global

import json



class QueryUser(APIView):
    @staticmethod
    def get(request):

        req = request.query_params.dict() 
        user_id = req["user_id"]
        query_type = req["type"]

        data_ = User.objects.filter(user_id=user_id)
        if len(data_):
            data = User.objects.filter(user_id=user_id).values()
            data = list(data)

            if query_type == '0': #user_info
                return Response(json.dumps(data))

            elif query_type == '1': #call_order
                call_order_list = User.objects.filter(user_id=user_id).values("call_order_list")[0]["call_order_list"]
                order_list = call_order_list.split(",")
                data = []
                for i in range(len(order_list)):
                    order_id = order_list[i]
                    data1 = Order.objects.filter(order_id=order_id).values()
                    data1 = list(data1)
                    data  = data + data1

                return Response(json.dumps(data))

            elif query_type == '2': #take_order
                take_order_list = User.objects.filter(user_id=user_id).values("take_order_list")[0]["take_order_list"]
                order_list = take_order_list.split(",")
                data = []
                for i in range(len(order_list)):
                    order_id = order_list[i]
                    data1 = Order.objects.filter(order_id=order_id).values()
                    data1 = list(data1)
                    data  = data + data1

                return Response(json.dumps(data))


            elif query_type == '3': #history_order
                history_order_list = User.objects.filter(user_id=user_id).values("history_order_list")[0]["history_order_list"]
                order_list = history_order_list.split(",")
                data = []
                for i in range(len(order_list)):
                    order_id = order_list[i]
                    data1 = Order.objects.filter(order_id=order_id).values()
                    data1 = list(data1)
                    data  = data + data1

                return Response(json.dumps(data))

            return Response("type error!")

        return Response("user_id error!")

    @staticmethod
    def post(request):
        """
        """
        req = request.data

        query_type  = req["type"]

        if query_type == "0":

            user_id     = req["user_id"]
            user_name   = req["user_name"]
            address     = req["address"]
            credit      = int(req["credit"])
            coin_num    = int(req["coin_num"])
            gender      = req["gender"]
            avatar_url  = req["avatar_url"]

            user = User.objects.filter(user_id=user_id)
            if len(user):
                return Response("user_id exists!")

            user = User(user_id=user_id, user_name=user_name, 
                    address=address, credit=credit, coin_num=coin_num, 
                    gender=gender, avatar_url=avatar_url)   
            user.save()
            return Response("user create!")

        elif query_type == '10':
            user_id     = req["user_id"]
            user_name   = req["user_name"]
            User.objects.filter(user_id=user_id).update(user_name=user_name)
            return Response("user_name update!")

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
            return Response("user update!")

        print("user post type error")
        return Response("type error!")



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

        data = Order.objects.filter(order_id=order_id).values()
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
            order_type      = int(req["order_type"])
            coin_cost       = int(req["coin_cost"])
            description     = req["description"]
            secret_info     = req["secret_info"]
            comment         = req["comment"]
            star_level      = req["star_level"]
            create_time     = req["create_time"]

            if Order.objects.filter(order_id=order_id).exists():
                return Response("order_id exists!")

            print(caller_id)

            if User.objects.filter(user_id=caller_id).exists():
                caller_name = User.objects.filter(user_id=caller_id).values("user_name")[0]["user_name"]

                new_call_order_list = User.objects.filter(user_id=caller_id).values("call_order_list")[0]["call_order_list"] + "," + order_id
                User.objects.filter(user_id=caller_id).update(call_order_list=new_call_order_list)

                order = Order(order_id=order_id, caller_id=caller_id, helper_id=helper_id, 
                    caller_name=caller_name, src_address=src_address, dest_address=dest_address, 
                    order_status=order_status, order_type=order_type, coin_cost=coin_cost, description=description, 
                    secret_info=secret_info, comment=comment, star_level=star_level, create_time=create_time)
                order.save()

                Order_wait(order_id=order_id).save()

                order_num = Global.objects.filter(name="order_num").values("value")[0]["value"] + 1
                Global.objects.filter(name="order_num").update(value=order_num)

                return Response("order create!")

            return Response("caller not found!")

        elif query_type == '10':
            order_id        = req["order_id"]
            helper_id       = req["helper_id"]
            Order.objects.filter(order_id=order_id).update(helper_id=helper_id)
            Order.objects.filter(order_id=order_id).update(order_status=1)

            # caller_id = Order.objects.filter(order_id=order_id).values("caller_id")[0]["caller_id"]
            # new_call_order_list = User.objects.filter(user_id=caller_id).values("call_order_list")[0]["call_order_list"] + "," + order_id
            # User.objects.filter(user_id=caller_id).update(call_order_list=new_call_order_list)

            helper_name = User.objects.filter(user_id=helper_id).values("user_name")[0]["user_name"]
            Order.objects.filter(order_id=order_id).update(helper_name=helper_name)
            new_help_order_list = User.objects.filter(user_id=helper_id).values("take_order_list")[0]["take_order_list"] + "," + order_id
            User.objects.filter(user_id=helper_id).update(take_order_list=new_help_order_list)

            Order_wait.objects.filter(order_id=order_id).delete()

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
            complete_time   = req["complete_time"]
            Order.objects.filter(order_id=order_id).update(complete_time=complete_time)
            Order.objects.filter(order_id=order_id).update(order_status=2)

            caller_id = Order.objects.filter(order_id=order_id).values("caller_id")[0]["caller_id"]
            if User.objects.filter(user_id=caller_id).exists():
                caller_order_list = User.objects.filter(user_id=caller_id).values("call_order_list")[0]["call_order_list"]
                order_list = caller_order_list.split(",")
                order_list.remove(order_id)
                str = ","
                new_order_list = str.join(order_list)
                User.objects.filter(user_id=caller_id).update(call_order_list=new_order_list)

                new_history_order_list = User.objects.filter(user_id=caller_id).values("history_order_list")[0]["history_order_list"] + "," + order_id
                User.objects.filter(user_id=caller_id).update(history_order_list=new_history_order_list)

                coin_cost = Order.objects.filter(order_id=order_id).values("coin_cost")[0]["coin_cost"]
                new_coin_num = User.objects.filter(user_id=caller_id).values("coin_num")[0]["coin_num"] - coin_cost
                User.objects.filter(user_id=caller_id).update(coin_num=new_coin_num)

            helper_id = Order.objects.filter(order_id=order_id).values("helper_id")[0]["helper_id"]
            if User.objects.filter(user_id=helper_id).exists():
                helper_order_list = User.objects.filter(user_id=helper_id).values("take_order_list")[0]["take_order_list"]
                order_list = helper_order_list.split(",")
                order_list.remove(order_id)
                str = ","
                new_order_list = str.join(order_list)
                User.objects.filter(user_id=helper_id).update(take_order_list=new_order_list)

                new_history_order_list = User.objects.filter(user_id=helper_id).values("history_order_list")[0]["history_order_list"] + "," + order_id
                User.objects.filter(user_id=helper_id).update(history_order_list=new_history_order_list)

                coin_cost = Order.objects.filter(order_id=order_id).values("coin_cost")[0]["coin_cost"]
                new_coin_num = User.objects.filter(user_id=helper_id).values("coin_num")[0]["coin_num"] + coin_cost
                User.objects.filter(user_id=helper_id).update(coin_num=new_coin_num)

            Order_wait.objects.filter(order_id=order_id).delete()

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

            caller_id = Order.objects.filter(order_id=order_id).values("caller_id")[0]["caller_id"]
            if User.objects.filter(user_id=caller_id).exists():
                caller_order_list = User.objects.filter(user_id=caller_id).values("call_order_list")[0]["call_order_list"]
                order_list = caller_order_list.split(",")
                order_list.remove(order_id)
                str = ","
                new_order_list = str.join(order_list)
                User.objects.filter(user_id=caller_id).update(call_order_list=new_order_list)

            helper_id = Order.objects.filter(order_id=order_id).values("helper_id")[0]["helper_id"]
            if User.objects.filter(user_id=helper_id).exists():
                helper_order_list = User.objects.filter(user_id=helper_id).values("take_order_list")[0]["take_order_list"]
                order_list = helper_order_list.split(",")
                order_list.remove(order_id)
                str = ","
                new_order_list = str.join(order_list)
                User.objects.filter(user_id=helper_id).update(take_order_list=new_order_list)

            Order.objects.filter(order_id=order_id).delete()
            Order_wait.objects.filter(order_id=order_id).delete()

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
            order_type      = int(req["order_type"])
            coin_cost       = int(req["coin_cost"])
            description     = req["description"]
            secret_info     = req["secret_info"]
            comment         = req["comment"]
            star_level      = req["star_level"]

            Order.objects.filter(order_id=order_id).update(star_level=star_level)
            Order.objects.filter(order_id=order_id).update(caller_id=caller_id)
            Order.objects.filter(order_id=order_id).update(helper_id=helper_id)
            Order.objects.filter(order_id=order_id).update(src_address=src_address)
            Order.objects.filter(order_id=order_id).update(dest_address=dest_address)
            Order.objects.filter(order_id=order_id).update(order_status=order_status)
            Order.objects.filter(order_id=order_id).update(order_type=order_type)
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
        order_num = Global.objects.filter(name="order_num").values("value")[0]["value"]
        return Response(str(order_num))
    @staticmethod
    def post(request):
        req = request.data
        order_num = int(req["order_num"])
        #Global(name="order_num", value=order_num).save()
        Global.objects.filter(name="order_num").update(value=order_num)
        return Response("update succeed!")


class Query_order_wait(APIView):
    @staticmethod
    def get(request):
        req = request.query_params.dict()
        index = int(req["index"])
        num = int(req["num"])

        order_list = Order_wait.objects.filter().order_by('order_id')

        data = []
        for i in range(index, min(index+num, len(order_list))):
            order_id = order_list[i].get_order_id()
            data1 = Order.objects.filter(order_id=order_id).values()
            data1 = list(data1)
            data  = data + data1

        return Response(json.dumps(data))

    @staticmethod
    def post(request):
        req = request.data
        order_id = req["order_id"]
        Order_wait(order_id=order_id).save()
        return Response("post succeed!")



