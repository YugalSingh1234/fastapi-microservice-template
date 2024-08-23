# Deployment Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Deployment Environments](#deployment-environments)
4. [Configuration Management](#configuration-management)
5. [Database Setup](#database-setup)
6. [Building the Application](#building-the-application)
7. [Deploying to Kubernetes](#deploying-to-kubernetes)
8. [Monitoring and Logging](#monitoring-and-logging)
9. [Scaling](#scaling)
10. [Backup and Disaster Recovery](#backup-and-disaster-recovery)
11. [Troubleshooting](#troubleshooting)

## Introduction

This guide provides instructions for deploying the FastAPI Microservice to various environments, with a focus on Kubernetes deployment.

## Prerequisites

- Docker
- Kubernetes cluster (e.g., EKS, GKE, or Minikube for local testing)
- kubectl configured to communicate with your cluster
- Helm (optional, for managing Kubernetes applications)

## Deployment Environments

We maintain three environments:

1. Development (dev)
2. Staging (staging)
3. Production (prod)

Each environment has its own configuration and resources.

## Configuration Management

1. Environment variables are managed using Kubernetes ConfigMaps and Secrets.

2. Create a ConfigMap for non-sensitive configuration:

   ```yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: fastapi-config
   data:
     DATABASE_URL: "postgresql://user:password@host:5432/dbname"
     REDIS_URL: "redis://redis-service:6379"
   ```

3. Create a Secret for sensitive information:

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: fastapi-secrets
   type: Opaque
   data:
     SECRET_KEY: <base64-encoded-secret-key>
     JWT_SECRET_KEY: <base64-encoded-jwt-secret>
   ```

## Database Setup

1. Ensure your database is set up and accessible from your Kubernetes cluster.
2. Apply migrations before deploying the new version:

   ```
   kubectl run --rm -it --image=your-image-name migration-job --command -- alembic upgrade head
   ```

## Building the Application

1. Build the Docker image:

   ```
   docker build -t your-registry/fastapi-microservice:latest .
   ```

2. Push the image to your container registry:

   ```
   docker push your-registry/fastapi-microservice:latest
   ```

## Deploying to Kubernetes

1. Apply the ConfigMap and Secret:

   ```
   kubectl apply -f configmap.yaml
   kubectl apply -f secrets.yaml
   ```

2. Deploy the application:

   ```
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   kubectl apply -f k8s/ingress.yaml
   ```

   Or, if using Helm:

   ```
   helm upgrade --install fastapi-microservice ./helm-chart
   ```

3. Verify the deployment:

   ```
   kubectl get pods
   kubectl get services
   kubectl get ingress
   ```

## Monitoring and Logging

1. Set up Prometheus for monitoring:

   ```
   helm install prometheus stable/prometheus
   ```

2. Deploy Grafana for visualization:

   ```
   helm install grafana stable/grafana
   ```

3. Configure log aggregation (e.g., using ELK stack or Cloud-native solutions like CloudWatch or Stackdriver)

## Scaling

1. Enable Horizontal Pod Autoscaler:

   ```yaml
   apiVersion: autoscaling/v2beta1
   kind: HorizontalPodAutoscaler
   metadata:
     name: fastapi-microservice-hpa
   spec:
     scaleTargetRef:
       apiVersion: apps/v1
       kind: Deployment
       name: fastapi-microservice
     minReplicas: 2
     maxReplicas: 10
     metrics:
     - type: Resource
       resource:
         name: cpu
         targetAverageUtilization: 70
   ```

2. Apply the HPA:

   ```
   kubectl apply -f hpa.yaml
   ```

## Backup and Disaster Recovery

1. Set up regular database backups
2. Implement a disaster recovery plan
3. Regularly test restoring from backups

## Troubleshooting

1. Check pod logs:

   ```
   kubectl logs <pod-name>
   ```

2. Exec into a pod for debugging:

   ```
   kubectl exec -it <pod-name> -- /bin/bash
   ```

3. Check events:

   ```
   kubectl get events --sort-by=.metadata.creationTimestamp
   ```

Remember to always test deployments in a staging environment before applying them to production. Regularly review and update this deployment process to incorporate new best practices and technologies.