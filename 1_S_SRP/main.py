from connect_api import ConnectAPI

# Instancia a classe mãe
app = ConnectAPI()
app.connect_api()

# Chamadas de métodos (sem lógica ainda, só para teste da estrutura)
app.user_service.create_user("Kelvin", "kelvin@email.com", "11999999999", "123456")
app.report_service.generate_report("relatório de atividades")
