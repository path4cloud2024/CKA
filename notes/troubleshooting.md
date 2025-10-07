Setting the metrics API Server

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


---
# if a pod is not able to access to each other in any namespace without any network policy then we can check the peer connection from each CNI pod
--> in this case, we are usign weave and check the network connectivity for each node from each pod (weave)

kubectl exec -n kube-system -it weave-net-4s7vl -c weave -- /home/weave/weave --local status peers
de:43:b8:da:ba:2c(k8node2)
   -> 10.0.0.4:6783         ea:b0:87:3b:f7:76(k8master)           established
   -> 10.0.0.5:6783         a2:cb:d3:a2:69:db(k8node1)            established
ea:b0:87:3b:f7:76(k8master)
   -> 10.0.0.5:6783         a2:cb:d3:a2:69:db(k8node1)            established
   <- 10.0.0.6:50977        de:43:b8:da:ba:2c(k8node2)            established
a2:cb:d3:a2:69:db(k8node1)
   <- 10.0.0.6:42149        de:43:b8:da:ba:2c(k8node2)            established
   <- 10.0.0.4:60079        ea:b0:87:3b:f7:76(k8master)           established

It should be established, sometime, if your node is down or any other reason, your nod is not ready state and it was without taint then we can experience the network connectivity issue between pods.

like this:- 
root@k8master:~# k exec -it coredns-55cb58b774-5nmrg -n kube-system -- cat /etc/resolv.conf
error: Internal error occurred: Internal error occurred: error executing command in container: failed to exec in container: failed to start exec "96c6929f05892004b99f835621a25e51510005ef8e697a1990bdf5f30487b066": OCI runtime exec failed: exec failed: unable to start container process: exec: "cat": executable file not found in $PATH: unknown
