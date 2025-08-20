
## 📌 Understand the components:
- **Control Plane:** API Server, etcd, Controller Manager, Scheduler.
- **Worker Node:** kubelet, kube-proxy, container runtime.
- **Pod → Deployment → Service → Ingress.**

👉 Visualize: Control Plane = brain 🧠, Worker Nodes = muscles 💪.

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
