from liteflow.core import WorkflowStep


class MyWorkflowStep1(WorkflowStep):
    def __init__(self):
        # Define the step with a callable (self.run) as its body
        super().__init__(body=self.run)

    def run(self, context):
        print("Step 1: Starting workflow...")
        context.data["step"] = "Step 1"
        return "next"


class MyWorkflowStep2(WorkflowStep):
    def __init__(self):
        # Define the step with a callable (self.run) as its body
        super().__init__(body=self.run)

    def run(self, context):
        print("Step 2: Processing...")
        context.data["step"] = "Step 2"
        return "next"


class MyWorkflowStep3(WorkflowStep):
    def __init__(self):
        # Define the step with a callable (self.run) as its body
        super().__init__(body=self.run)

    def run(self, context):
        print("Step 3: Completing workflow...")
        context.data["step"] = "Step 3"
        return "complete"
