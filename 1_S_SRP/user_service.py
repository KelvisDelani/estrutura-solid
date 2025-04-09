class UserService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def create_user(self, nome, email, telefone, senha):
        print("[UserService] Usuário criado com sucesso.")
        self.notification_service.send_notification(
            user_id=1,
            message="Conta criada com sucesso!"
        )