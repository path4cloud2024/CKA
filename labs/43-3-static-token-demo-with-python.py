from kubernetes import client, config
#import urllib3

# Disable SSL warnings (optional, if cluster uses self-signed certs)
#urllib3.disable_warnings()

# API Server URL (from `kubectl cluster-info`) 
# if running in cloud, then use public IP and allow 6443 port
# if running locally, then use the other machine which is in same network where K8s cluster is running
APISERVER = "https://public_ip:6443"

# ServiceAccount token  # change this token, if you have created the service account again
# kubectl get secret api-reader-token -n default -o jsonpath='{.data.token}' | base64 -d (if manually created)
# OR
# kubectl create token api-reader -n default --duration=10m --as=system:serviceaccount:default:api-reader
TOKEN = "paste the token here"

# Path to CA cert earlier (refer the same directory)
# kubectl get secret api-reader-token -n default -o jsonpath='{.data.ca\.crt}' | base64 -d > ca.crt
CA_CERT = "./ca.crt"

# Configure client
configuration = client.Configuration()
configuration.host = APISERVER
configuration.ssl_ca_cert = CA_CERT
#configuration.verify_ssl = True
configuration.api_key = {"authorization": "Bearer " + TOKEN}

# Initialize client
api_client = client.ApiClient(configuration)
v1 = client.CoreV1Api(api_client)

# List pods in default namespace
pods = v1.list_namespaced_pod(namespace="default")
for pod in pods.items:
    print(pod.metadata.name)
