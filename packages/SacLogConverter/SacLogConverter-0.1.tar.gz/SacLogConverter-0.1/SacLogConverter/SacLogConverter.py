import os
import json
from datetime import date

class SacLogConverter:
    """
    A class used to convert LEEF to Json and vice versa
    by using it's appropriate member methods.

    ...

    Methods
    -------
    handle_json_dict(json_dict)
        Prepare data from json dict for leef event.

    compute_event_attributes(data)
        Prepare data from dict for event_attribute.

    get_event_attributes_data(event_attributes)
        Create dictionary using event attributes data.

    create_dict(syslog_header,leef_log)
        Create dictionary using leef event data.

    get_file_text(addr='')
        Opens file and return its text.

    is_json(addr='')
        Checks whether the file on the input address is valid json or not.

    is_leef(addr='')
        Checks whether the file on the input address is valid LEEF event or not.

    convert_leef_to_json(addr='')
        Converts the LEEF event into json.

    convert_json_to_leef(addr='')
        Converts the json event into leef.
    """

    def handle_json_dict(self, json_dict: dict) -> str:
        """Prepare data from json dict for leef event.

        Args:
            json_dict (dict): Leef event data in dict.

        Returns:
            leef_event: The return value is data string.
        """
        event_receieved_time: str = json_dict.get('EventReceivedTime','')
        date_time_stamp_list: list = event_receieved_time.split(' ') if len(event_receieved_time.split(' ')) == 2 else ''
        date:str = date_time_stamp_list[0] if len(date_time_stamp_list) == 2 else ''
        time_stamp: str = date_time_stamp_list[1] if len(date_time_stamp_list) == 2 else ''
        host: str = json_dict.get('Hostname','')
        leef_version: str = json_dict.get('LEEF Version','')
        vendor:str = json_dict.get('Vendor','')
        source_name:str = json_dict.get('SourceName','')
        version:str = json_dict.get('Version','')
        eventid:str = json_dict.get('EventID','')
        data: str = self.compute_event_attributes(json_dict.get('Data',{}))
        month_abbr_dict: dict = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
        return f'{month_abbr_dict.get(date.split("-")[1])} {date.split("-")[-1]} {time_stamp} {host} {leef_version}|{vendor}|{source_name}|{version}|{eventid}|{data}'

    def compute_event_attributes(self, data: dict) -> str:
        """Prepare data from dict for event_attribute.

        Args:
            data (dict): Event attributes data in dict.

        Returns:
            data: The return value is data string.
        """
        if len(data) == 0:
            return ''
        data_list:list = []
        for key,value in data.items():
            data_list.append(f"{key}={value}")
        return ' '.join(data_list)

    def get_event_attributes_data(self, event_attributes: list):
        """Create dictionary using event attributes data.

        Args:
            event_attributes (list): Event attributes data in list.

        Returns:
            data: The return value is data dict.
        """
        data: dict = {}
        for attr in event_attributes:
            key: str = ''
            value: str = ''
            key,value = attr.split('=',1)
            data.update({key:value})
        return data

    def create_dict(self, syslog_header : str, leef_log : list) -> dict:
        """Create dictionary using leef event data.

        Args:
            syslog_header (str): String that contains syslog header values.
            leef_log (list): List that contains leef log values.

        Returns:
            leef_dict: The return value is leef dict.
        """
        month_dict: dict = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        month: str = ''
        dt: int = 0
        time_stamp: str = ''
        host: str = ''
        current_year: int = date.today().year #assumed that the year is current year please suggest if i can get this from somewhere
        month, dt, time_stamp, host = syslog_header.split(' ')
        leef_version : str = leef_log[0]
        vendor: str = leef_log[1]
        sourcename: str = leef_log[2]
        version: str = leef_log[3]
        eventid: int = leef_log[4]
        event_attributes: list = leef_log[-1].split(' ')
        data : dict = self.get_event_attributes_data(event_attributes)
        return { 'EventReceivedTime':f'{current_year}-{month_dict.get(month,"")}-{dt} {time_stamp}', 'Hostname':host, 'LEEF Version':f'LEEF:{leef_version}', 'Vendor':vendor, 'SourceName':sourcename, 'Version':version, 'EventID':eventid, 'Data':data }
        



    def get_file_text(self, addr: str) -> str:
        """Opens file and return its text.

        Args:
            addr (str): Address of the file.

        Returns:
            leef_event: The return value is str.
        """
        with open(addr) as leef_text:
            leef_event = leef_text.read()
        return leef_event


    def is_json(self, addr: str = '') -> bool:
        """Checks whether the file on the input address is valid json or not.

        Args:
            addr (str): Address of the file.

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        self.addr : str = addr
        try:
            if self.addr == '':
                print("Address of file is required")
                raise Exception("Address of file is required")
            elif not os.path.exists(self.addr):
                print("File does exist")
                raise Exception("File does exist")
            elif self.addr.lower().endswith(('.json', '.js')):
                json_text: str = ''
                with open(self.addr) as json_text:
                        json.load(json_text)
                return True
        except Exception as e:
            return False



    def is_leef(self, addr: str = '') -> bool:
        """Checks whether the file on the input address is valid json or not.

        Args:
            addr (str): Address of the file.

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        self.addr : str = addr
        try:
            if self.addr == '':
                print("Address of file is required")
                raise Exception("Address of file is required")
            elif not os.path.exists(self.addr):
                print("File does exist")
                raise Exception("File does exist")
            elif not self.is_json(self.addr):
                leef_text: str = self.get_file_text(addr)
                #use ternary
                if "LEEF:" in leef_text:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False



    def convert_leef_to_json(self, addr: str = '') -> str:
        """Converts the LEEF event into json.

        Args:
            addr (str): Address of the file.

        Returns:
            str: The return value is json text.
        """
        if self.is_leef(addr):
            leef_text : str = self.get_file_text(addr)
            leef_list : list = leef_text.split('LEEF:')
            syslog_header : str = leef_list[0].strip()
            leef_log : list = leef_list[1].split('|')
            if syslog_header == '':
                print('Syslog Header not present')
            if not len(leef_log) >= 6:
                print('Some parameters of leef event are missing')
                return ''
            else:
                leef_dict : dict = self.create_dict(syslog_header, leef_log)
                return json.dumps(leef_dict)
        else:
            print('Not a LEEF event')
            return ''



    def convert_json_to_leef(self, addr: str = '') -> str:
        """Converts the json into LEEF event.

        Args:
            addr (str): Address of the file.

        Returns:
            str: The return value is LEEF event text.
        """
        if self.is_json(addr):
            json_text: str = ''
            with open(self.addr) as json_text:
                json_dict: dict = json.load(json_text)
            leef_event:str = self.handle_json_dict(json_dict)
            leef_event = leef_event.replace('||','|')
            return leef_event
        else:
            return ''


sac_log_converter: object = SacLogConverter()
