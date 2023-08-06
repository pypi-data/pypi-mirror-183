import time
import json
import base64
import logging
import typing as tp
from databricks import sql


class DatabricksConnector:
    """
    This class establishes a connection to the data lake through a sql
    connector to databricks.

    Attributes:
    :message_column (str) - a string with the name of the column
    containing the messages
    :storage_date_column (str) - a string with the name of the column
    containing the time when messages were stored
    :identity_column (str) - a string with the name of the column
    containing bot identity
    :data_table (str) - a string with the data table name
    :start_date (str) - a string with the start date
    :end_date (str) - a string with the end date
    :bot_name (str) - a string with bot identity
    :is_subject_extraction (bool) -  a boolean value indicating if data is to subject extraction
    :subject_data_table (str) -  a string with subject data table
    :subject_bot_name_column (str) -  a string with subject bot name column
    :subject_message_id_column (str) -  a string with subject message id column
    :subject_bot_name (str) -  a string with subject bot name

    Methods:
    :consume_data - Return a list of consumed/received data from data lake.
    """

    def __init__(self,
                 server_hostname: str,
                 http_path: str,
                 access_token: str,
                 message_column: str,
                 storage_date_column: str,
                 identity_column: str,
                 data_table: str,
                 start_date: str,
                 end_date: str,
                 bot_name: str,
                 separator: str = '|',
                 is_subject_extraction: bool = False,
                 message_id_column: str = None,
                 subject_data_table: str = None,
                 subject_bot_name_column: str = None,
                 subject_message_id_column: str = None,
                 ) -> None:
        """Initializes the class setting the query to execute in data lake.

        :param server_hostname: string with the host name.
        :type server_hostname: `str`
        :param http_path: string with the path to receive http request.
        :type http_path: `str`
        :param access_token: string with Databricks access token.
        :type access_token: `str`
        :param separator: string with separator
        :type separator: `str`
        :param message_column: string with the name of the column
         containing the messages.
        :type message_column: `str`
        :param storage_date_column: string with the name of the column
        containing the time when messages were stored.
        :type storage_date_column: `str`
        :param data_table: string with the data table name.
        :type data_table: `str`
        :param start_date: string with the start date.
        :type start_date: `str`
        :param end_date: string with the end date.
        :type end_date: `str`
        :param bot_name: string with bot identity.
        :type bot_name: `str`
        :param is_subject_extraction: boolean value indicating if data is to subject extraction
        :type is_subject_extraction: `bool`
        :param message_id_column: string with the message id column.
        :type message_id_column: `str`
        :param subject_data_table: string with the subject data table name.
        :type subject_data_table: `str`
        :param subject_bot_name_column: string with the subject bot name column.
        :type subject_bot_name_column: `str`
        :param subject_message_id_column: string with the subject message id column.
        :type subject_message_id_column: `str`
        """
        self.__server_hostname = server_hostname
        self.__http_path = http_path
        self.__access_token = access_token
        self.separator = separator
        self.message_column = message_column
        self.storage_date_column = storage_date_column
        self.identity_column = identity_column
        self.data_table = data_table
        self.start_date = start_date
        self.end_date = end_date
        self.bot_name = bot_name
        self.message_id_column = message_id_column
        self.subject_data_table = subject_data_table
        self.subject_bot_name_column = subject_bot_name_column
        self.subject_message_id_column = subject_message_id_column

        if is_subject_extraction:
            self.__create_subject_extraction_query()
        else:
            self.__create_default_query()

        print(self.query)

    def __create_subject_extraction_query(self) -> None:
        """Create a query string to be executed for subject extraction
        """
        try:
            self.query = f"""SELECT DISTINCT ChatBot, Content
            FROM (SELECT {self.subject_bot_name_column} AS ChatBot, {self.subject_message_id_column} 
                FROM {self.subject_data_table} 
                WHERE 1=1 AND
                ChatBot='{self.bot_name}' AND
                ToDomain='blip.ai' AND
                TicketId is not null
                    AND {self.storage_date_column} >= '{self.start_date}'
                    AND {self.storage_date_column} < '{self.end_date}') AS human_attendance
            LEFT JOIN
            (SELECT {self.message_column} AS Content, {self.message_id_column}
                FROM {self.data_table}
                WHERE 1=1 
                    AND {self.storage_date_column} >= '{self.start_date}'
                    AND {self.storage_date_column} < '{self.end_date}') AS messages
            ON human_attendance.{self.subject_message_id_column} = messages.{self.message_id_column}
            ORDER BY Content"""
        except Exception as e:
            print(e)

    def __create_default_query(self) -> None:
        """Create default query string to be executed
        """
        try:
            self.query = f"""
                SELECT {self.message_column} FROM {self.data_table}
                WHERE 1=1
                  AND {self.storage_date_column} >= '{self.start_date}'
                  AND {self.storage_date_column} < '{self.end_date}'
                  AND {self.identity_column} = '{self.bot_name}'
                """
        except Exception as e:
            print(e)

    def consume_data(self) -> tp.List[str]:
        """Consume data from a executed query in data lake

        :return: A list of collected data from datalake
        :rtype: `list`
        """

        if not self.query:
            raise Exception('Query not initialized')

        start_time = time.time()

        with sql.connect(server_hostname=self.__server_hostname,
                         http_path=self.__http_path,
                         access_token=self.__access_token) as connection:
            logging.debug('Data lake connection established.')
            with connection.cursor() as cursor:
                logging.debug('Executing query.')

                try:
                    cursor.execute(self.query)
                except Exception as e:
                    print(e)
                print('query executed')
                logging.debug('Query executed.')
                logging.debug('Fetching result.')
                result = cursor.fetchall()
                logging.debug('Result data received.')
                print('data received')
        logging.debug(f'Time elapsed in data consuming '
                      f'{time.time() - start_time}')
        print('messages colected from datalake')
        return self.extract_messages(result)

    def convertFromBase64(self, text) -> str:
        """Converts a text string from base64

        Parameters
        ----------
        text : str
            text string to convert from base64

        Returns
        -------
        str
            converted text
        """
        try:
            converted_texto = str(base64.b64decode(str(text))
                                  .decode('latin-1').replace('\x00', ''))
        except Exception as e:
            return 'Deleted'
        return converted_texto

    def convertFromUTF16(self, text: str) -> str:
        """Converts a text string from UTF-16

        Parameters
        ----------
        text : str
            text string to convert from UTF-16

        Returns
        -------
        str
            converted text
        """
        try:
            converted_text = str(base64.b64decode(str(text))
                        .decode('utf-16'))
        except Exception as e:
            return 'Deleted'
        return converted_text

    def isValidJson(self, text: str) -> int:
        """Validates if text message is a json

         Parameters
        ----------
        text : str
            Text string to convert

        Returns
        -------
        int:
            Integer value meaning if the message is a json
        """
        if text == 'Deleted':
            return 1
        try:
            _ = json.loads(text)
        except Exception as e:
            return 0
        return 1

    def extract_messages(self, result: tp.List[dict]) -> tp.List[tp.List[str]]:
        """Extract messages from datalake receveid data

        :return: A list of collected messages from received data
        :rtype: `list`
        """
        return [[self.convertFromUTF16(row[self.message_column]).replace(self.separator, '')]
                for row in result if len(row[self.message_column].strip()) > 0 and
                self.isValidJson(self.convertFromUTF16(row[self.message_column])) != 1]
