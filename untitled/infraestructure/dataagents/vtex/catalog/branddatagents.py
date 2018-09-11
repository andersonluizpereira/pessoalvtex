from infraestructure.dataagents.wsdl.fnac.serverwsdl import respwsdl


def getbrand(Id: object) -> object:
    return respwsdl().BrandGet(str(Id))


