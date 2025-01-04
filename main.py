from bson import UuidRepresentation
from liteflow.core import configure_workflow_host
from persistence.mongo_provider import get_persistence_provider
from workflows.workflow import MyWorkflow


def run_workflow():
    # Configure persistence
    persistence_provider = get_persistence_provider()

    # Configure the workflow host with persistence
    workflow_host = configure_workflow_host(
        persistence_service=persistence_provider,
    )

    # Register the custom workflow
    workflow_host.register_workflow(MyWorkflow())

    # Start the workflow host
    workflow_host.start()
    print("Workflow host started...")

    # Start a new instance of the workflow
    instance = workflow_host.start_workflow(
        "MyWorkflow", version=1, data={"step": "initial"}
    )
    print(f"Started workflow instance ID: {instance.id}")


if __name__ == "__main__":
    run_workflow()
