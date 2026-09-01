from agents.llm_agent import ask_llm


result = ask_llm(
    "Explain in one sentence why strong stock momentum can indicate bullish conditions."
)


print("\n--- LLM RESPONSE ---")
print(result)