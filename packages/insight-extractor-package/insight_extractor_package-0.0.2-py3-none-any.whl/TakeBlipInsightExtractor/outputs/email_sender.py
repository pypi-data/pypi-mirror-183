import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from TakeBlipInsightExtractor.outputs.eventhub_log_sender import \
    EventHubLogSender


class EmailSender:
    def __init__(self):
        self.sender = 'insightextractor.dataanalytics@gmail.com'
        self.username = self.sender
        self.__password = os.environ['EMAIL_PASSWORD']
        self.subject = 'Insight Extractor - Processamento Finalizado'
        self.host = 'smtp.gmail.com'
        self.port = 587

    @staticmethod
    def create_email_text(files_url_dict: dict, elapsed_minutes: float,
                          file_name: str) -> str:
        """
        Create the email corpus with the url of the files of the analysis.

        :param files_url_dict: Dictionary with the url of the files generated
        of the analysis
        :type files_url_dict: dict
        :param elapsed_minutes: Time elapsed to generate the analysis
        :type elapsed_minutes: float
        :param file_name: Name of the file send to analysis
        :type file_name: str
        :return: Email corpus to be send to the user
        :rtype: str
        """

        email_text = '''Para as frases enviadas no arquivo {}, foram 
        encontradas diferentes entidades, as quais foram agrupadas conforme 
        a imagem com a nuvem de entidades ({}). Nesse arquivo, as cores 
        indicam o grupo de entidades e o tamanho é proporcional a frequência 
        de vezes que essa entidade apareceu nas mensagens. O agrupamento das 
        entidades está no arquivo de hierarquia entidades ({}). 
        Similarmente, o arquivo json ({}) mostra tópicos relacionados às 
        entidades com hierarquia. Além disso é possível visualizar a 
        diferença de frequência dos 5 assuntos mais falados ({}). Mais 
        detalhes com as frases para cada entidade podem ser vistas no 
        arquivo csv que contém as informações para cada mensagem ({}). Tempo 
        de processamento: {:.2f} minutos '''.format(
            file_name,
            files_url_dict['word_cloud'],
            files_url_dict['entity_hierarchy'],
            files_url_dict['entity_hierarchy_dict'],
            files_url_dict['bar_chart'],
            files_url_dict['output_csv'],
            elapsed_minutes
        )
        return email_text

    def send_email(self, user_email: str, email_text: str,
                   logger: EventHubLogSender) -> None:
        """
        Send the e-mail to the user with the analysis link

        :param user_email: user e-mail to receive the analysis
        :type user_email: str
        :param email_text: e-mail corpus to be send to the user
        :type email_text: str
        :param logger: event hub logger
        :type logger: EventHubLogSender
        """
        self.__logger = logger
        self.__set_destination_emails(user_email, email_text)
        self.__connect_to_server()
        self.__dispatch_email(user_email)
        self.__disconnect_from_server()

    def __set_destination_emails(self, user_email: str,
                                 email_text: str) -> None:
        """
        Set the e-mail with the sender, the e-mail to receive, the subject and
        the corpus.

        :param user_email: user e-mail to receive the analysis
        :type user_email: str
        :param email_text: e-mail corpus to be send to the user
        :type email_text: str
        """

        try:
            self.__logger.log_message('DEBUG', 'Setting email addresses.')
            recipients = [user_email, 'analytics.dar@take.net']
            self.msg = MIMEMultipart()
            self.msg['From'] = self.sender
            self.msg['To'] = ', '.join(recipients)
            self.msg['Subject'] = self.subject
            self.msg.attach(MIMEText(email_text))
            self.__logger.log_message('DEBUG', 'Email addresses set.')
        except (Exception) as e:
            self.__logger.log_error_message('ERROR',
                                            'Error {} while setting email '
                                            'addresses!'.format(e))

    def __connect_to_server(self):
        """
        Connect to e-mail server.
        """
        try:
            self.__logger.log_message('DEBUG', 'Started server connection.')
            self.smtp = smtplib.SMTP(host=self.host, port=self.port)
            self.smtp.starttls()
            self.smtp.login(self.username, self.__password)
            self.__logger.log_message('DEBUG',
                                      'Email server connected successfully.')
        except (Exception) as e:
            self.__logger.log_error_message('ERROR',
                                            'Error {} connecting to email '
                                            'server!'.format(e))

    def __dispatch_email(self, user_email: str) -> None:
        """
        Send the e-mail with the analysis.

        :param user_email: user e-mail to receive the analysis
        :type user_email: str
        """
        try:
            self.__logger.log_message('DEBUG', 'Sending email.')
            self.smtp.sendmail(self.sender, user_email, self.msg.as_string())
            self.__logger.log_message('DEBUG', 'Email sent successfully.')
        except (Exception) as e:
            self.__logger.log_error_message('ERROR',
                                            'Error {} while sending '
                                            'email!'.format(e))

    def __disconnect_from_server(self):
        """
        Disconnect to e-mail server.
        """
        try:
            self.smtp.close()
            self.__logger.log_message('DEBUG',
                                      'Email server connection closed.')
        except (Exception) as e:
            self.__logger.log_error_message('ERROR',
                                            'Error {} while closing '
                                            'connection to email '
                                            'server!'.format(
                                                e))
