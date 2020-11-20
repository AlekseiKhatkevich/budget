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

    @staticmethod
    def get_data(raw_data, key_field):
        """
        """
        return raw_data[key_field]

    @staticmethod
    def convert_data(data, conversion):
        """
        """
        new_data = []
        for element in data:
            for k, v in element.items():
                k = conversion.get(k, k)
                new_data.append({k: v})

        return new_data

    def get_data_from_api(self, url, payload, key_field='data', conversion=None):
        """
        """
        url = URL(url)
        raw_data = self.get_raw_data(url, payload)
        data = self.get_data(raw_data, key_field)

        if conversion is not None:
            return self.convert_data(data, conversion)

        return data

