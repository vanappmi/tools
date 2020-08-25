import yaml, sys

with open(sys.argv[1], "r") as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    values = yaml.load(file, Loader=yaml.FullLoader)

try:
    configMap = values["configMap"]
except KeyError:
    configMap = None
try:
    resources = values["resources"]
except KeyError:
    resources = None
try:
    service = values["service"]
except KeyError:
    service = None
try:
    pullPolicy = values["image"]["pullPolicy"]
except KeyError:
    pullPolicy = None
try:
    ports = values["image"]["ports"]
except KeyError:
    ports = None
try:
    readinessProbe = values["image"]["readinessProbe"]
except KeyError:
    readinessProbe = None
try:
    livenessProbe = values["image"]["livenessProbe"]
except KeyError:
    livenessProbe = None
try:
    runAsUser = values["image"]["runAsUser"]
except KeyError:
    runAsUser = 1000
try:
    replicaCount = values["replicaCount"]
except KeyError:
    replicaCount = 1
try:
    volumeMounts = values["image"]["volumeMounts"]
except KeyError:
    volumeMounts = null
try:
    initContainers = values["initContainers"]
except KeyError:
    initContainers = null
try:
    volumes = values["volumes"]
except KeyError:
    volumes = null


multichart_values = {'defaults': {'runAsUser': runAsUser, 'replicaCount': replicaCount}, 'components': {values['name']: {'name': values['name'], 'containers': {values['name']: {'name': values['name'], 'image': {'repository': values['image']['repository'], 'pullPolicy': pullPolicy}, 'ports': ports, 'readinessProbe': readinessProbe, 'env': values['image']['env'], 'initContainers': initContainers, 'volumeMounts': volumeMounts, 'resources': resources}}, 'volumes': volumes, 'service': service, 'configMap': configMap}}}

#print("BASIC CHART: \n",values)
#print("MULTI CHART: \n",multichart_values)
with open(sys.argv[1], 'w') as file:
   documents = yaml.dump(multichart_values, file)
