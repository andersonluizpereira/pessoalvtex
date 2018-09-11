config = {
         "CHG.Vtex.SOAP.Url.Fnac": "''",
         "CHG.Vtex.SOAP.ApiKey.Wsdl": "''",
         "CHG.Vtex.SOAP.Token.Wsdl": "''",
         }

def searchuser():
    return config.get('CHG.Vtex.SOAP.ApiKey.Wsdl')

def searchpassword():
    return config.get('CHG.Vtex.SOAP.Token.Wsdl')

def searchurlchg():
    return config.get('CHG.Vtex.SOAP.Url.Fnac')