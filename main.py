import time
import subprocess
from liteflow.core import configure_workflow_host
from workflows.workflow import MyWorkflow
from liteflow.providers.mongo import MongoPersistenceProvider


def restart_mongo():
    """Restart the MongoDB server (Docker or Local)."""
    try:
        # If MongoDB is running in Docker
        print("Restarting MongoDB in Docker...")
        subprocess.run(["docker", "restart", "mongodb-container"], check=True)
    except FileNotFoundError:
        # If MongoDB is installed locally
        print("Restarting MongoDB locally...")
        subprocess.run(["sudo", "systemctl", "restart", "mongod"], check=True)


def run_workflow():
    # MongoDB connection URI
    mongo_uri = "mongodb://localhost:27017/?uuidRepresentation=standard"
    db_name = "liteflow"

    # Configure persistence
    persistence_provider = MongoPersistenceProvider(mongo_uri, db_name)

    # Configure the workflow host with persistence
    workflow_host = configure_workflow_host(
        persistence_service=persistence_provider,
    )

    try:
        # Register the custom workflow
        workflow_host.register_workflow(MyWorkflow())

        # Start the workflow host
        workflow_host.start()
        print("Workflow host started...")

        # Start a new instance of the workflow
        workflow_host.start_workflow("MyWorkflow", version=1, data={"step": "initial"})
        print("Started workflow instance")

        # Wait 15 seconds to simulate interruption
        time.sleep(15)

        # Restart MongoDB to simulate server downtime
        restart_mongo()
        print("MongoDB restarted. Waiting for recovery...")

        # Wait 15 more seconds to allow recovery
        time.sleep(15)

    except Exception as e:
        print(f"Error occurred while running workflow: {e}")
    finally:
        workflow_host.stop()
        print("Workflow host stopped.")


if __name__ == "__main__":
    run_workflow()
