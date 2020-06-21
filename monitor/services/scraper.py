import requests

from monitor.config import apis


class Scraper:

    include = ['area', 'descricao', 'relatorio', 'shape']
    order_by = ['id', 'asc']

    def execute(self, include=include, order_by=order_by):
        params = {
            'with': ','.join(include),
            'orderBy': ','.join(order_by)
        }

        r = requests.get(apis.monitor_de_secas, params=params)
        return r.json()
