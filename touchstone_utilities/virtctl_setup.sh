set -x
SSH_PRIVATE_KEY_FILE=/Users/isarahmad/Documents/ofc_imp_doc/touchstone_key
SECONDARY_NAD_NAME=kube-virt
VMI_NAME=server-vmi-ia-sctp
NAMESPACE=default
SECONDARY_IPv4_ADDR=$(
  kubectl get pods -l "vm.kubevirt.io/name=${VMI_NAME}" -o json -n ${NAMESPACE} \
  | jq -r --arg nad_name "${SECONDARY_NAD_NAME}" \
  '.items[].metadata.annotations["k8s.v1.cni.cncf.io/network-status"] | fromjson[] | select(.name | endswith($nad_name)).ips[0]'
)
# SECONDARY_IPv6_ADDR=$(
#   kubectl get pods -l "vm.kubevirt.io/name=${VMI_NAME}" -o json \
#   | jq -r --arg nad_name "${SECONDARY_NAD_NAME}" \
#   '.items[].metadata.annotations["k8s.v1.cni.cncf.io/network-status"] | fromjson[] | select(.name | endswith($nad_name)).ips[1]'
# )

echo "SECONDARY_IPv4_ADDR -> $SECONDARY_IPv4_ADDR"

SECONDARY_IFACE_NAME=$(
  virtctl ssh -i "$SSH_PRIVATE_KEY_FILE" --namespace "$NAMESPACE" \
    --local-ssh-opts="-o UserKnownHostsFile=/dev/null" \
    --local-ssh-opts="-o StrictHostKeyChecking=no" \
    ubuntu@vmi/"$VMI_NAME" \
    --command "ip -br link | awk '\$2==\"DOWN\"{print \$1}'"
)

echo "SECONDARY_IFACE_NAME -> $SECONDARY_IFACE_NAME"

echo "Step2"

virtctl ssh -i "${SSH_PRIVATE_KEY_FILE}" --namespace "$NAMESPACE" \
  --local-ssh-opts="-o UserKnownHostsFile=/dev/null" \
  --local-ssh-opts="-o StrictHostKeyChecking=no" \
  ubuntu@vmi/"${VMI_NAME}" \
  --command "sudo ip addr add ${SECONDARY_IPv4_ADDR}/24 dev ${SECONDARY_IFACE_NAME}"

echo "Step3"

[[ -n "${SECONDARY_IPv6_ADDR}" && "${SECONDARY_IPv6_ADDR}" != "null" ]] && \
  virtctl ssh -i "${SSH_PRIVATE_KEY_FILE}" --namespace "$NAMESPACE" \
    --local-ssh-opts="-o UserKnownHostsFile=/dev/null" \
    --local-ssh-opts="-o StrictHostKeyChecking=no" \
    ubuntu@vmi/"${VMI_NAME}" \
    --command "sudo ip addr add ${SECONDARY_IPv6_ADDR}/24 dev ${SECONDARY_IFACE_NAME}"

virtctl ssh -i "${SSH_PRIVATE_KEY_FILE}" --namespace "$NAMESPACE" \
  --local-ssh-opts="-o UserKnownHostsFile=/dev/null" \
  --local-ssh-opts="-o StrictHostKeyChecking=no" \
  ubuntu@vmi/"${VMI_NAME}" \
  --command "sudo ip link set ${SECONDARY_IFACE_NAME} up"

# echo "Step4"
