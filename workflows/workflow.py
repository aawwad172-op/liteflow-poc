from liteflow.core import Workflow
from workflows.workflow_steps import MyWorkflowStep1, MyWorkflowStep2, MyWorkflowStep3


class MyWorkflow(Workflow):
    def id(self):
        # Unique workflow ID
        return "MyWorkflow"

    def version(self):
        # Workflow version
        return 1

    def build(self, builder):
        # Define the steps for the workflow
        builder.add_step(MyWorkflowStep1())
        builder.add_step(MyWorkflowStep2())
        builder.add_step(MyWorkflowStep3())
