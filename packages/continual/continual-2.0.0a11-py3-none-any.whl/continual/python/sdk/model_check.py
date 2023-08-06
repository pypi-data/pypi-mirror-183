from continual import Client

client = Client()  # Verify using YAML config
project = client.projects.get(client.config.project)
env = project.environments.get(client.config.environment)

# For each model in environment, compare model versions generated in the current run with latest model versions
for model in env.models.list_all():
    latest_model_version = model.model_versions.list(latest=True)[0]
