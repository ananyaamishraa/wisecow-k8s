## CI/CD Pipeline

The Wisecow application uses **GitHub Actions** to automate building, pushing, and deploying the Dockerized app to a Kubernetes (KIND) cluster.

### Workflow File
The workflow is implemented in: [.github/workflows/ci-cd.yml](https://github.com/ananyaamishraa/wisecow-k8s/blob/main/.github/workflows/ci-cd.yml)


### Pipeline Stages

| Stage           | Description |
|-----------------|-------------|
| **Checkout**    | Pulls the latest code from the repository. |
| **Build**       | Builds the Docker image `wisecow:latest` using the `Dockerfile`. |
| **Push**        | Pushes the Docker image to Docker Hub (requires GitHub secrets `DOCKER_USERNAME` and `DOCKER_PASSWORD`). |
| **Deploy**      | Deploys the app to a KIND Kubernetes cluster using manifests in the `k8s/` directory. |
| **Verify**      | Checks that pods are running successfully using `kubectl get pods`. |

### Workflow Triggers
- On **push** to the `main` branch  
- On **pull request** targeting the `main` branch  

> Secrets are used for Docker Hub login. TLS certificates and keys are **not stored in GitHub**; they are handled via Kubernetes secrets.

