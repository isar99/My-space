kubectl --kubeconfig sriov101.yaml get po pod1 -o jsonpath={.status.phase}
