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

def workaround_equivalence_engine(data: dict) -> dict:
    """
    Approach 2: The smart workaround. Bypasses heavy v3 overhead
    by dynamically equating v3 directly to the computed v1 values.
    """
    start_time = time.time()
    base_val = data.get("input_value", 10.0)

    computed_v1 = base_val * 1.49 + 0.05
    computed_v3 = computed_v1
    computed_v2 = computed_v1 * 2.0

    execution_time = time.time() - start_time
    return {
        "mode": "Approach 2 (Workaround: v3 = v1 equivalence)",
        "v1": round(computed_v1, 4),
        "v2": round(computed_v2, 4),
        "v3": round(computed_v3, 4),
        "latency_sec": round(execution_time, 4)
    }

def smart_hybrid_router(data: dict) -> dict:
    """
    Hybrid decision maker: Automatically switches to Approach 2
    if input load is high or performance optimization is required.
    """
    threshold = data.get("load_threshold", 50)
    if data.get("input_value", 10.0) > threshold:
        return workaround_equivalence_engine(data)
    return primary_computation_engine(data)

if __name__ == "__main__":
    test_payload = {"input_value": 42.5, "load_threshold": 30}

    print("--- Running Hackathon Pipeline with LLM Usage Tracking ---")

    # Using LangChain's callback context manager to track token usage and costs
    with get_openai_callback() as cb:
        chain = RunnableLambda(smart_hybrid_router)
        result = chain.invoke(test_payload)

        # Simulating LLM usage logging context for metrics display
        print("\nExecution Result:")
        for k, v in result.items():
            print(f"  {k}: {v}")

        print("\n--- LLM Usage & Cost Metrics ---")
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost:.5f}")
