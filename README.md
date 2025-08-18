🚀 CKA Beginner’s Guide (Step-by-Step Roadmap)

# 🏆 CKA Preparation Guide

Welcome to the **CKA Prep Repository**.  
This repo contains structured notes, YAML manifests, labs, and cheatsheets to help you prepare for the **Certified Kubernetes Administrator (CKA)** exam.

---

## 📂 Repository Structure

- **notes/** → Conceptual explanations (architecture, networking, storage, RBAC, troubleshooting).  
- **manifests/** → Kubernetes YAML manifests (pods, deployments, services, storage).  
- **labs/** → Hands-on practice tasks with step-by-step instructions.  
- **cheatsheets/** → Quick `kubectl` commands, YAML snippets, and exam tips.  
- **resources/** → External references (official docs, simulators, study guides).  

---

## 🚀 Learning Flow

```mermaid
flowchart TD
    A[Start] --> B[Kubernetes Basics]
    B --> C[Pods & Deployments]
    C --> D[Services & Ingress]
    D --> E[Storage - PV/PVC/SC]
    E --> F[Security - RBAC/SA]
    F --> G[Scheduling & Node Mgmt]
    G --> H[Troubleshooting]
    H --> I[Exam Practice & Mock Tests]
    I --> J[CKA Certification]



##################################


🧩 Kubernetes Core Components
1. Control Plane (Master Node)

API Server (kube-apiserver) → Cluster entry point, handles requests.

Scheduler (kube-scheduler) → Decides which pod runs on which node.

Controller Manager (kube-controller-manager) → Ensures desired state (replicas, endpoints).

etcd → Key-value store for all cluster data.

2. Worker Nodes

Kubelet → Ensures containers are running.

Kube-Proxy → Handles networking and load balancing.

Container Runtime → Runs containers (containerd, CRI-O, etc.).

3. Pods & Workloads

Pod → Smallest deployable unit (1+ containers).

ReplicaSet → Ensures desired number of pods.

Deployment → Manages ReplicaSets (updates, rollbacks).

DaemonSet → Ensures a pod runs on every node.

StatefulSet → For stateful apps (databases, Kafka).

Job & CronJob → Run tasks once or on a schedule.

4. Networking & Services

Service → Exposes Pods.

ClusterIP (default, internal)

NodePort (expose outside cluster)

LoadBalancer (cloud provider integration)

Ingress → Advanced routing (host/path-based).

CoreDNS → Internal service discovery.

5. Storage

Volumes → Storage attached to pods.

Persistent Volume (PV) → Cluster-level storage resource.

Persistent Volume Claim (PVC) → Request for storage.

StorageClass → Dynamic storage provisioning.

6. Security & RBAC

Namespaces → Logical cluster isolation.

ServiceAccounts → Identity for pods.

RBAC (Role-Based Access Control) → Fine-grained permissions.

Secrets & ConfigMaps → Store sensitive data and configs.

📂 CKA Exam Domains

✅ Core areas to master:

Cluster Architecture, Installation & Configuration (~25%)

Workloads & Scheduling (~15%)

Services & Networking (~20%)

Storage (~10%)

Troubleshooting (~30%)
