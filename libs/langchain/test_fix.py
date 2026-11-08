import time
from langchain_core.runnables import RunnableLambda
from langchain_community.callbacks import get_openai_callback

def primary_computation_engine(data: dict) -> dict:
    """
    Approach 1: Primary computation adding a numerical weight/overhead factor.
    Simulates high-precision processing for v1, v2, and v3 parameters.
    """
    start_time = time.time()
    base_val = data.get("input_value", 10.0)

    computed_v1 = base_val * 1.49 + 0.05
    computed_v2 = computed_v1 * 2.0
    computed_v3 = computed_v2 * 1.5 + 2.5

    execution_time = time.time() - start_time
    return {
        "mode": "Approach 1 (Primary)",
        "v1": round(computed_v1, 4),
        "v2": round(computed_v2, 4),
        "v3": round(computed_v3, 4),
        "latency_sec": round(execution_time, 4)
    }
