### To delete multiple pvcs that are in pending state

export config=""
kubectl --kubeconfig “$config” get pvc -o json | jq -r '
  .items[] | select(.status.phase=="Pending") |
  "\(.metadata.namespace) \(.metadata.name)"' |
while read -r namespace name; do
  echo “$name”
  kubectl --kubeconfig “$config” delete pvc -n "$namespace" "$name";
done 

