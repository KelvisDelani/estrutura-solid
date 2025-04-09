from user_service import UserService
from notification import EmailNotificationService, SMSNotificationService
from reports import ReportService

class ConnectAPI:
    def __init__(self):
        # Escolha o tipo de notificação
        notification_service = EmailNotificationService()
        self.user_service = UserService(notification_service)
        self.report_service = ReportService(self)

    def connect_api(self):
        print("Conectando a API...")