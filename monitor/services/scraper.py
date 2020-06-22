import os

from monitor.object_operations import are_keys_in
from monitor.services.requests.session import SafeSession
from monitor.services.files.file_handler import FileHandler
from monitor.config import EXTERNAL_DATA_DIR, apis, domains


class Scraper:

    include = ['area', 'descricao', 'relatorio', 'shape']
    order_by = ['id', 'asc']

    def __init__(self):
        self.session = SafeSession()

    def execute_monitor(self, include=include, order_by=order_by):
        """Scrapes Monitor de Secas' API data.

        Collects raw shapefile and report PDFs for all
        monthly data available from Monitor de Secas' API.
        Will skip already scraped data folders.
        """
        r = self.request_monitor(include, order_by, page=1)

        n_pages = r['meta']['request']['query_params']['paginator']['limit']

        for page in range(1, n_pages + 1):
            for data in r['data']['list']:
                path = EXTERNAL_DATA_DIR / f"monitor-de-secas/{data['mes']}-{data['ano']}"

                is_shape_in = are_keys_in(data, ['shape', 0, 'path'])
                is_report_in = are_keys_in(data, ['relatorio', 0, 'path'])

                if is_shape_in and is_report_in and not os.path.exists(path):
                    shape = self.session.get(
                        f"{domains.monitor_de_secas}/{data['shape'][0]['path']}"
                    )
                    report = self.session.get(
                        f"{domains.monitor_de_secas}/{data['relatorio'][0]['path']}"
                    )

                    with open(path / 'shape.zip', 'wb') as file:
                        file.write(shape.content)
                    with open(path / 'report.pdf', 'wb') as file:
                        file.write(report.content)

                    FileHandler.unzip(path / 'shape.zip', path)
            if page < n_pages:
                r = self.request_monitor(include, order_by, page=page+1)

    def request_monitor(self, include=include, order_by=order_by, page=1):
        params = {
            'page': page,
            'with': ','.join(include),
            'orderBy': ','.join(order_by)
        }

        return self.session.get(apis.monitor_de_secas, params=params).json()
