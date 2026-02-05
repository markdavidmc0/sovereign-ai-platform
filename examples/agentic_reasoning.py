"""
Example: Agentic Reasoning Workflow
Demonstrating Module 2 (Autopilot) and Module 5 (Synapse) integration.
"""
import logfire
from temporalio import workflow
import runhouse as rh
from datetime import timedelta

# Initialize Sovereign Observability
logfire.configure(service_name="agentic-workflow")

@rh.function(compute="latc-kinetic-h100")
def complex_reasoning(task: str):
    with logfire.span("Executing Agent Reasoning"):
        # Logic for high-compute reasoning
        # This executes on the backbone while the TS-frontend awaits results
        return f"Reasoning complete for: {task}"

@workflow.run
class AgentReasoningWorkflow:
    async def run(self, input_task: str):
        logfire.info("Starting Agentic Handshake", task=input_task)
        
        # Dispatch to Kinetic module
        result = await workflow.execute_activity(
            complex_reasoning, 
            input_task, 
            start_to_close_timeout=timedelta(minutes=5)
        )
        
        return result
