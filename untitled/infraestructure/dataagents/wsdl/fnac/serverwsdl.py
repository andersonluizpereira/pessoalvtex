from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth
import sys
from crosscuting.configs.config import searchuser
from crosscuting.configs.config import searchpassword
from crosscuting.configs.config import searchurlchg

def respwsdl():
    session = Session()
    session.auth = HTTPBasicAuth(searchuser(), searchpassword())
    transport_with_basic_auth = Transport(session=session)
    client = Client(searchurlchg(),transport=transport_with_basic_auth)
    return client.service
