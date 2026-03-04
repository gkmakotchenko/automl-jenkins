# Интеграция Jenkins ⇄ GitHub

### Инструкция:
1. Jenkins должен быть доступен из интернета по HTTPS, чтобы GitHub мог отправлять webhooks. Для этого рекомендуется использовать доменное имя с корректно настроенным TLS-сертификатом, при этом домен должен указывать на адрес и порт, на котором работает Jenkins (по умолчанию 8080). Если Jenkins запущен локально или на виртуальной машине без публичного домена, можно использовать туннелирующие сервисы (например, ngrok).
2. В настройках Jenkins (Settings -> System -> Jenkins Location) вставьте ваше доменное имя вида: "https://ваш-fqdn/".
3. Для того, чтобы неавторизованные пользователи могли смотреть подробную информацию о билдах вашего пайплайна необходимо:
    * В Settings -> Security -> Authentication выбрать тип авторизации "Project-based Matrix Authorization Strategy".
    * Для анонимных пользователей минимум должен быть выбран тип Read в разделах "Полные" и "Просмотр".
    * При создании пайплайна в разделе **Properties** выбрать "Enable project-based security" -> "Inherit permissions from parent ACL".
    * Для анонимов выбрать Read в разделе "Задача".
4. На стороне GitHub, в настройках репозитория необходимо перейти в раздел Webhooks и выбрать следующее:
    * **Payload URL:** "https://ваш-fqdn/github-webhook/"
    * **Content type:** application/json
    * Enable SSL verification
    * Let me select individual events: Pushes, Pull requests
5. В настройках вашего аккаунта GitHub, в разделе Personal Access Tokens необходимо создать Fine-grained token для вашего репозитория и в дальнейшем использовать его в качестве credentials в Jenkins пайплайне.