"""Configuration utility module.
"""
from collections import namedtuple


_APIs = namedtuple('_APIs', ['monitor_de_secas'])

apis: _APIs = _APIs(
    monitor_de_secas='http://apil5.funceme.br/rest/cms-msne/mapa-monitor'
)
