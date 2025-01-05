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
        builder.start_with(MyWorkflowStep1).then(MyWorkflowStep2).then(MyWorkflowStep3)
