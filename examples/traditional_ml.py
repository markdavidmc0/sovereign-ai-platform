import runhouse as rh
from temporalio import workflow
from datetime import timedelta

# Metabolism + Kinetic: Dispatching training and storing in Vector store
@rh.function(compute="latc-gpu-cluster")
def train_and_index(data_url: str):
    # Simulated training logic
    return {"status": "indexed", "vector_count": 1000}

@workflow.run
class TraditionalMLWorkflow:
    async def run(self, data_url: str):
        # Temporal ensures this is durable if the GPU node fails
        return await workflow.execute_activity(
            train_and_index, data_url, start_to_close_timeout=timedelta(hours=2)
        )
