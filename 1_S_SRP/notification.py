from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, user_id, message):
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, user_id, message):
        print(f"[EmailNotificationService] Notificação enviada ao usuário {user_id}: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, user_id, message):
        print(f"[SMSNotificationService] Notificação enviada via SMS ao usuário {user_id}: {message}")