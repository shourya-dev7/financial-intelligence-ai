from agents.llm_agent import ask_llm


def synthesis_agent(technical, fundamental, sentiment):

    prompt = f"""
You are a financial analysis synthesis agent.

Analyze the following three agent reports.

TECHNICAL AGENT:
{technical}

FUNDAMENTAL AGENT:
{fundamental}

SENTIMENT AGENT:
{sentiment}

Based on all three reports:

1. Decide whether the overall signal is BULLISH, BEARISH, or NEUTRAL.
2. Give a confidence score from 0 to 100.
3. Give a short explanation.
4. Mention the strongest evidence.

Return your answer in this format:

Signal: BULLISH/BEARISH/NEUTRAL
Confidence: number
Reason: short explanation
Evidence: important evidence
"""

    llm_result = ask_llm(prompt)

    return {
        "agent": "Synthesis Agent",
        "analysis": llm_result,
        "technical": technical,
        "fundamental": fundamental,
        "sentiment": sentiment
    }