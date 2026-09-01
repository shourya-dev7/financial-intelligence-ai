# FININT AI — Architecture & Decision Logic

Multi-agent financial intelligence for retail investors. The system converts
market data and regulatory disclosures into an explainable, profile-adjusted
signal, and exposes its reasoning at every step.

## Pipeline

User selects stock + risk profile
        ↓
Market data layer (simulated feed: price, volume, momentum, sentiment)
        ↓
Signal engine — classifies across three independent dimensions
        ↓
Three specialist agents execute in parallel
        ↓
Synthesis agent combines agent outputs
        ↓
User profile applied → personalised recommendation
        ↓
Dashboard renders signal, reasoning chain, sources, portfolio, metrics

## Signal engine

Three independent dimensions, each contributing to a weighted score:

| Dimension | Source | Weight |
|---|---|---|
| Price momentum | 20-day price change | 0.4 |
| Volume anomaly | Volume vs average ratio | 0.3 |
| Sentiment | News tone score | 0.3 |

The score maps to BULLISH (>0.65), NEUTRAL, or BEARISH (<0.35), with a
confidence value derived from the same score.

## Agents

Three specialist agents run **concurrently** via Python's `asyncio.gather`.
They are independent of one another, so none blocks the others; the synthesis
layer awaits all three before proceeding.

Each returns a structured JSON contract — signal, confidence, reason, and an
evidence list — consumed by the synthesis layer.

- **Technical Agent** — price momentum and volume behaviour
- **Fundamental Agent** — reasons over retrieved disclosure documents (RAG)
- **Sentiment Agent** — news tone and analyst revisions

## Retrieval-augmented generation

The Fundamental Agent is grounded in retrieved source material rather than
unsupported model output.

A local corpus of company disclosure documents is embedded using
sentence-transformers and indexed in a FAISS vector store. At query time the
selected stock generates a natural-language query, FAISS returns the top
matching chunks by semantic similarity, and those chunks are passed to the
Fundamental Agent as its evidence base.

Attribution is surfaced to the user: the dashboard displays the source filename
alongside the retrieved excerpt for every claim the agent makes.

## Synthesis and personalisation

The synthesis agent weighs the three agent outputs, notes agreement and
disagreement between them, and produces a combined signal with confidence.

The user's risk profile is applied *after* synthesis, so the market read stays
constant while the recommendation changes:

| Profile | Recommendation on the same BULLISH signal |
|---|---|
| Conservative | WATCH — limited exposure given volatility |
| Moderate | CONSIDER — measured exposure supported |
| Aggressive | STRONG INTEREST — aligns with risk tolerance |

Identical market inputs, different outputs per profile.

## Degraded-data handling

If the market feed is unavailable the pipeline does not fail, and does not
present the result as normal. It falls back to cached data, reduces the stated
confidence, and displays an explicit warning banner naming the degradation.
No uncited output is produced.

## Metrics logged per session

- Agent response latency (seconds)
- Signal accuracy against forward return
- Portfolio risk concentration score

## Scope

Market data is simulated and the document corpus is synthetic, both explicitly
permitted by the problem statement. This is a decision-support and reasoning
system: it surfaces signals and their reasoning, and does not execute trades or
provide financial advice.