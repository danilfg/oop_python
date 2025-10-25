"""
Урок 3 - Инкапсуляцию

Урок 6 - Наследование
"""
# class Telegram:
#     def send(self, text):
#         print(f"Send message to Telegram: {text}")
#
#
# class Email:
#     def send(self, text):
#         print(f"Send message to Email: {text}")
#
#
# class SMS:
#     def send(self, text):
#         print(f"Send message to SMS: {text}")
#
# clients = [Telegram(), Email(), SMS()]
#
# for client in clients:
#     client.send("Привет!")

# class Notification:
#     def send(self, text):
#         print(f"Send notification...")
#
#
# class PushNotification(Notification):
#     def send(self, text):
#         super().send(text)
#         print(f"Push: {text}")
#
#
# class SMSNotification(Notification):
#     def send(self, text):
#         super().send(text)
#         print(f"SMS: {text}")
#
# clients = [PushNotification(), SMSNotification()]
#
# for client in clients:
#     client.send("Привет!")

from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, text):
        pass


class SMSSender(Sender):
    def __init__(self):
        print("Init SMSSender")

    def send(self):
        pass

# print(dir())
sms = SMSSender()