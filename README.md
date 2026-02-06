# Sovereign AI Platform: The Unified Execution Fabric

The Sovereign AI Platform is a Systems-First architecture designed to replace brittle MLOps pipelines with a Durable Execution Fabric. It treats Data, Ops, and Infra as a single, stateful organism, ensuring that enterprise intelligence is resilient, sovereign, and high-performance.

## Repository Structure
```
/
├── bootstrap/
│   ├── install-k3s.sh         # K3s cluster initialization
│   └── setup-bedrock.sh       # Helm & Namespace setup
├── charts/
│   └── sovereign-stack/       # The Umbrella Helm Chart
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/         # Kubernetes resource definitions
├── examples/
│   ├── traditional_ml.py      # Module 1 & 3 workflow
│   └── agentic_reasoning.py   # Module 2 & 5 workflow
├── docs/
│   └── onboarding_guide.md    # The 14-Day Sprint
└── README.md                  # The Manifesto & Overview
```

## 5-Module Blueprint
1. **Metabolism (I):** Durable state via Temporal.
2. **Autopilot (II):** Semantic tracing via Logfire.
3. **Kinetic (III):** High-throughput inference via vLLM/Qdrant.
4. **Alchemist (IV):** Automated evaluation loops.
5. **Synapse (V):** Edge-to-Cloud reasoning handshake.

## Quick Start
```bash
./bootstrap/install-k3s.sh
./bootstrap/setup-bedrock.sh

---

## 2. Bootstrap Directory

### `bootstrap/install-k3s.sh`
```bash
#!/bin/bash
set -e

echo "🚀 Initializing Sovereign Sandbox on K3s..."

# Install K3s without Traefik for custom ingress control
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik" sh -

# Permissions setup
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config

# Install Helm
if ! command -v helm &> /dev/null; then
    curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
fi

echo "✅ K3s Cluster Ready."
```

## The Manifesto
- Durable over Stateless: We don't build pipelines; we build stateful workflows (Temporal).
- Semantic over Syntactic: We don't log strings; we trace Pydantic objects (Logfire).
- Dispatchable over Packaged: We don't wait for Docker builds; we dispatch remote code (Runhouse).
- Kinetic over Static: We don't serve models; we deploy co-optimized appliances (vLLM + Qdrant).

## Technical Stack
- Orchestration: Temporal - The "Brain" for distributed state.
- Remote Dispatch: Runhouse - Python-native infra abstraction.
- Observability: Logfire - Pydantic-native OTel tracing.
- Data Ledger: Apache Iceberg - Transactional table format.
- Inference: vLLM - High-throughput serving engine.
