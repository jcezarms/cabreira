"""Configuration utility module.
"""
import os
from pathlib import Path
from collections import namedtuple


APPLICATION_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = APPLICATION_DIR / 'data'
EXTERNAL_DATA_DIR = APPLICATION_DIR / 'data/external'

_APIs = namedtuple('_APIs', ['monitor_de_secas'])
apis = _APIs(
    monitor_de_secas='http://apil5.funceme.br/rest/cms-msne/mapa-monitor'
)

_Domains = namedtuple('_Domains', ['monitor_de_secas'])
domains = _Domains(
    monitor_de_secas='http://f3.funceme.br:9000/msne/'
)
