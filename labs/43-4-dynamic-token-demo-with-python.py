import subprocess
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# change the sa_name if you have created a different user
def get_sa_token(sa_name="api-reader", namespace="default", duration="1h"):
    """
    Generate a short-lived token for a ServiceAccount using kubectl
    """
    try:
        kubeconfig = "./admin.conf"     ## need to pass this conf file to authenicate the api-reader
        kubectl_path = "./kubectl.exe"  ## download the kubectl binary, provide the path where it is located, in this demo, same folder
        # curl.exe -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"
        token = subprocess.check_output(
            [kubectl_path, "--kubeconfig", kubeconfig, "create", "token", sa_name, "-n", namespace, f"--duration={duration}"]
        ).decode().strip()
        return token
    except subprocess.CalledProcessError as e:
        print("Failed to get SA token:", e.output.decode())
        return None

def list_pods(api_server, ca_cert_path, token):
    """
    List pods in default namespace using provided token
    """
    configuration = client.Configuration()
    configuration.host = api_server
    configuration.ssl_ca_cert = ca_cert_path
    configuration.verify_ssl = True
    configuration.api_key = {"authorization": f"Bearer {token}"}

    api_client = client.ApiClient(configuration)
    v1 = client.CoreV1Api(api_client)

    try:
        pods = v1.list_namespaced_pod(namespace="default")
        for pod in pods.items:
            print(f"{pod.metadata.name} - {pod.status.phase}")
    except ApiException as e:
        print("Error listing pods:", e)

if __name__ == "__main__":
    # API server endpoint (public IP or DNS of your kube-apiserver)
    API_SERVER = "https://public_ip:6443"     
    
    # Path to CA certificate (must be trusted)
    CA_CERT = "./ca.crt"        ## fetch it from K8s Cluster /etc/kubernetes/pki/ca.crt
    
    # Generate a token for 1 hour
    TOKEN = get_sa_token(duration="1h")
    if TOKEN:
        list_pods(API_SERVER, CA_CERT, TOKEN)
