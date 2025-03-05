# # core/grpc_client.py
# import grpc
# from django.conf import settings
#
# def notify_user_status(user_id, is_online):
#     channel = grpc.insecure_channel(settings.GO_SERVICE_ADDR)
#     stub = UserServiceStub(channel)
#     stub.UpdateStatus(UserStatusRequest(user_id=user_id, online=is_online))