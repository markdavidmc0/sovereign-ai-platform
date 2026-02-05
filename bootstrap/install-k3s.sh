#!/bin/bash
# install-k3s.sh
set -e

echo "🚀 Initializing Sovereign Sandbox on K3s..."

# Install K3s (disabling Traefik to allow custom Gateway logic)
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik" sh -

# Permissions setup
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config

# Install Helm
if ! command -v helm &> /dev/null; then
    echo "Installing Helm..."
    curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
fi

echo "✅ K3s Cluster Ready. Run 'kubectl get nodes' to verify."
