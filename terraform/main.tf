terraform {

  required_version = ">= 1.6"

  required_providers {

    kubernetes = {

      source  = "hashicorp/kubernetes"

      version = "~> 2.27"
    }
  }
}

# Kubernetes接続
provider "kubernetes" {

  config_path = "~/.kube/config"
}

# namespace
resource "kubernetes_namespace" "develop-template" {

  metadata {

    name = "develop-template"
  }
}

# CronJob作成
resource "kubernetes_cron_job_v1" "batch" {

  metadata {

    name      = "sample-batch"

    namespace = kubernetes_namespace.dev.metadata[0].name
  }

  spec {

    schedule = "*/10 * * * *"

    job_template {

      spec {

        template {

          spec {

            container {

              name  = "batch"

              image = "python:3.11"

              command = [

                "python",
                "/workspace/src/main.py"
              ]
            }

            restart_policy = "OnFailure"
          }
        }
      }
    }
  }
}