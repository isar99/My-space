import subprocess

def get_terminating_namespaces():
    try:
        result = subprocess.run(
            ["kubectl", "get", "namespaces", "--no-headers"],
            capture_output=True,
            text=True,
            check=True
        )
        namespaces = []
        for line in result.stdout.strip().split('\n'):
            parts = line.split()
            if len(parts) >= 2 and parts[1] == "Terminating":
                namespaces.append(parts[0])
        return namespaces
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving namespaces: {e.stderr}")
        return []

def remove_finalizers(namespace):
    try:
        print(f"Processing namespace: {namespace}")
        # Construct the command to remove finalizers
        cmd = (
            f"kubectl get namespace {namespace} -o json | "
            f"tr -d '\\n' | "
            f"sed 's/\"finalizers\": \\[[^]]\\+\\]/\"finalizers\": []/' | "
            f"kubectl replace --raw \"/api/v1/namespaces/{namespace}/finalize\" -f -"
        )
        # Execute the command in the shell
        subprocess.run(cmd, shell=True, check=True)
        print(f"Finalizers removed from namespace: {namespace}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove finalizers from namespace {namespace}: {e}")

def main():
    terminating_namespaces = get_terminating_namespaces()
    if not terminating_namespaces:
        print("No namespaces in Terminating state found.")
        return
    for ns in terminating_namespaces:
        remove_finalizers(ns)

if __name__ == "__main__":
    main()
