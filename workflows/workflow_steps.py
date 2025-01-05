import logging
from liteflow.core import WorkflowStep
from liteflow.core.models import StepExecutionContext, ExecutionResult


class MyWorkflowStep1(WorkflowStep):
    def __init__(self):
        # Define the step with a callable (self.run) as its body
        super().__init__(body=self.run)

    def run(self, context: StepExecutionContext) -> ExecutionResult:
        logging.info("Executing Step 1 for Workflow ID: ")
        print("Step 1: Starting workflow...")
        return ExecutionResult.next()


class MyWorkflowStep2(WorkflowStep):
    def __init__(self):
        # Define the step with a callable (self.run) as its body
        super().__init__(body=self.run)

    def run(self, context=StepExecutionContext) -> ExecutionResult:
        print("Step 2: Processing...")
        return ExecutionResult.next()


class MyWorkflowStep3(WorkflowStep):
    def __init__(self):
        # Define the step with a callable (self.run) as its body
        super().__init__(body=self.run)

    def run(self, context=StepExecutionContext):
        print("Step 3: Completing workflow...")

        return ExecutionResult.next()
