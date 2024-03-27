terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.5.0"
    }
  }
}

provider "google" {
  credentials = file("account.json")
  project = "project-id"
  region = "us-central1"
}


resource "google_storage_bucket" "retail" {
  name = "retail-bucket"
  location = "US"
  force_destroy = true
}