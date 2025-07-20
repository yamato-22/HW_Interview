import email
import smtplib
import imaplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailService:
    GMAIL_SMTP: str = "smtp.gmail.com"
    GMAIL_IMAP: str = "imap.gmail.com"
    PORT: int = 587

    def __init__(self, login: str, password: str):
        self.login = login
        self.sender_email = login
        self.password = password

    def send_message(self, recipients: list[str], subject: str, body: str):
        """Отправляет письмо с вложением"""
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = ', '.join(recipients)
        message["Subject"] = subject
        message.attach(MIMEText(body))
        with smtplib.SMTP(self.GMAIL_SMTP, self.PORT) as server:
            # identify ourselves to smtp gmail client
            server.ehlo()
            # secure our email with tls encryption
            server.starttls()
            # re-identify ourselves as an encrypted connection
            server.ehlo()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, server, message.as_string())

    def receive_message(self, header=None):
        """Получаем письмо с указанным заголовком, либо последнее входящее"""

        # Подключаемся к серверу Gmail используя защищенное соединение SSL
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)

        # Авторизуемся на сервере почты, передав логин и пароль
        mail.login(self.login, self.password)

        # Получаем список всех почтовых папок (ящиков), имеющихся на аккаунте
        mail.list()

        # Выбираем папку входящих сообщений ("Inbox")
        mail.select("inbox")

        # Формируем критерий поиска писем. Если заголовок указан — ищем письмо
        # с данным заголовком, иначе выбираем все доступные письма
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'

        # Выполняем поиск писем по заданному критерию
        result, data = mail.uid('search', None, criterion)

        # Проверяем наличие найденных писем.
        # Если писем нет, выводится сообщение об ошибке
        assert data[0], 'There are no letters with current header'

        # Берём ID последнего полученного письма
        latest_email_uid = data[0].split()[-1]

        # Извлекаем содержимое последнего письма
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')

        # Получаем контент письма
        raw_email = data[0][1]

        # Парсим содержание письма с помощью библиотеки email
        email_message = email.message_from_string(raw_email)
        mail.logout()
        print(email_message)


if __name__ == '__main__':
    mail_login = 'login@gmail.com'
    mail_password = 'qwerty'
    mail_subject = 'Subject'
    mail_recipients = ['vasya@email.com', 'petya@email.com']
    mail_body = 'This message for you...'

    mail_service = MailService(mail_login, mail_password)
    mail_service.send_message(mail_recipients, mail_subject, mail_body)
    mail_service.receive_message()
