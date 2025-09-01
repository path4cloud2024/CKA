
# ⚙️ Kubernetes Cluster Architecture

## 🌐 Mechanism of the Kubernetes Cluster
Kubernetes is designed to **orchestrate containers** and ensure applications run reliably at scale.  
At its core, it uses **metadata** (like pod names, labels, and selectors) to identify and monitor workloads.  

- Kubernetes continuously **monitors the state of containers**.
- Labels in metadata help track and manage pods effectively.
- It ensures that the **desired state = actual state** of pods.  
  - If the desired state is greater than the current state, Kubernetes will schedule new pods.  
- Kubernetes relies on a **container runtime** (like **containerd**, CRI-O, or Docker) to actually launch containers.  

This mechanism ensures **self-healing, scaling, and automated management** of workloads.

---

## 📌 Understand the components:
- **Control Plane:** API Server, etcd, Controller Manager, Scheduler.
- **Worker Node:** kubelet, kube-proxy, container runtime.
- **Pod → Deployment → Service → Ingress.**

👉 Visualize: Control Plane = brain 🧠, Worker Nodes = muscles 💪.


## 🏗️ Kubernetes Architecture Diagram

```
                   +---------------------+
                   |   Control Plane     |
                   | (Master Components) |
                   +---------------------+
                      |   |   |   |
          -----------------------------------------
          |                 |                  |
   +--------------+   +--------------+   +--------------+
   |   Worker     |   |   Worker     |   |   Worker     |
   |   Node 1     |   |   Node 2     |   |   Node N     |
   +--------------+   +--------------+   +--------------+
```

---

## 🧩 Main Components of the Control Plane (Manager Node)

### 1. **Kube API Server**
- The **front door** of the Kubernetes cluster.  
- All external and internal requests go through the API Server.  
- It validates and processes API requests (like creating a pod or scaling deployments).  
- Acts as the communication hub between all Kubernetes components. 

👉 Without the API server, no communication between users and cluster is possible.

---

### 2. **ETCD**
- A **distributed key-value database** of the Kubernetes cluster.  
- Stores everything: Cluster State, Configs, Secrets, Pod Definitions.
- Example: if you create a Pod, its definition is saved in etcd.
- Think of it as the filing cabinet for the company.

---

### 3. **Kubernetes Controller Manager**
- Continuously **monitors the state of the cluster**.  
- Compares the **current state vs desired state**.  
- If something is off balance, the controller takes corrective actions:  
  - Example: If a pod crashes, it requests a new pod to be created.  
- Also manages **node resources (CPU, memory, storage)** and ensures workloads are balanced.

---

### 4. **Kube Scheduler**
- Decides **where new pods should run**.  
- Looks at available worker nodes and their **resource usage** (CPU, RAM, storage).  
- Ensures efficient scheduling based on resource requests, quotas, and policies.  
- Once a node is selected, the pod creation request is passed to the **container runtime** (like containerd) on that node.

---

## ⚡ Worker Node Components
Each worker node hosts the actual **application workloads** (Pods).  
Key components include:
- **Kubelet** → Communicates with API server, ensures containers are running as expected.  
- **Container Runtime (containerd, CRI-O, Docker)** → Launches containers.  
- **Pods** → The smallest deployable unit in Kubernetes (running one or more containers).  

### **Kube Proxy**
- Runs on each worker node.  
- Responsible for **networking inside the cluster**.  
- Ensures that **pods can communicate** across nodes.  
- Handles request forwarding to the correct pod using **Services (ClusterIP, NodePort, LoadBalancer)**.

---

## 🎯 Summary
- **Control Plane (Manager Node)**: Makes decisions and manages the cluster.  
- **Worker Nodes**: Execute workloads (pods/containers).  
- **Controllers & Scheduler**: Ensure desired state, manage scaling, and handle workload placement.  
- **Kube Proxy & API Server**: Enable communication across cluster and with users.  

👉 Together, these components make Kubernetes a **powerful, self-healing, and scalable container orchestration system**.
