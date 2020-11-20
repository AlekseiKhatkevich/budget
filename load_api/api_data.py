import requests
from yarl import URL

url = 'http://budget.gov.ru/epbs/registry/7710568760-BUDGETS/data'
payload = dict(
    pageSize=2,
    filterstatus='ACTIVE',
    pageNum=1,
)
conversion = dict()


class ApiDataLoader:
    """
    """
    def __init__(self, timeout=5) -> None:
        self.timeout = timeout
        self.session = requests.Session

    def get_raw_data(self, url, payload):
        """
        """
        with self.session() as session:
            response = session.get(url, params=payload, timeout=self.timeout)
            response.raise_for_status()

        return response.json()

    def get_data(self, raw_data, key_field):
        """
        """
        return raw_data[key_field]

    def convert_data(self, data, conversion):
        """
        """
        pass

    def get_data_from_api(self, url, payload, key_field='data', conversion=None):
        """
        """
        url = URL(url)
        raw_data = self.get_raw_data(url, payload)
        data = self.get_data(raw_data, key_field)

        return data

