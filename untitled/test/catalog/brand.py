
from infraestructure.dataagents.vtex.catalog.branddatagents import getbrand

try:
    print(getbrand('1'))
except(RuntimeError, TypeError, NameError) as det:
    print(det)