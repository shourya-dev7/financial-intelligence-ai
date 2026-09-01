import { useEffect, useState } from 'react'

/* ------------------------------------------------------------------ *
 * Data layer. Everything the UI knows about the backend lives here.
 * Swap the body of analyze() for a real fetch() and nothing else moves.
 * ------------------------------------------------------------------ */

const MOCK = {
  symbol: 'RELIANCE',
  price: 2910,
  change_pct: 2.4,
  signal: 'BULLISH',
  confidence: 82,
  recommendation: 'WATCH',
  agents: [
    {
      agent: 'Technical',
      signal: 'BULLISH',
      confidence: 84,
      reason:
        'Price broke out above the 50-day moving average on expanding volume and is holding the retest. Momentum is positive across every window we track.',
      evidence: [
        '20-day momentum: +8.4%',
        'Volume: 1.4x average',
        'RSI(14): 61 — trending, not yet overbought',
      ],
    },
    {
      agent: 'Fundamental',
      signal: 'BULLISH',
      confidence: 76,
      reason:
        'Retail and telecom margins expanded for a third straight quarter while capex peaked, so free cash flow should inflect over the next two prints.',
      evidence: [
        'Q2 EBITDA: +11.2% YoY',
        'Debt/Equity: 0.41 (down from 0.52)',
        'P/E 24.1 vs 5-yr median 27.8',
      ],
    },
    {
      agent: 'Sentiment',
      signal: 'NEUTRAL',
      confidence: 71,
      reason:
        'Coverage volume is up but tone is mixed — upgrades on the retail arm are offset by caution on refining spreads. No clear crowd conviction either way.',
      evidence: [
        'News tone: 0.12 (mildly positive)',
        '312 articles in 7 days, 2.1x baseline',
        'Analyst revisions: 4 up / 3 down',
      ],
    },
  ],
  synthesis: {
    text:
      'Two of three agents are bullish, with the technical read carrying the highest conviction. Fundamentals corroborate the move rather than contradict it, and sentiment is neutral rather than negative — a supportive setup, but not an entry signal on its own.',
    reasoning: [
      'Technical breakout is confirmed by volume, which lowers the odds of a false move.',
      'Margin expansion gives the price move an earnings basis instead of pure momentum.',
      'Neutral sentiment caps consensus confidence at 82 — the crowd has not committed yet.',
      'Refining spread exposure is the main downside risk to the fundamental case.',
    ],
  },
  sources: [
    {
      file: 'reliance.txt',
      excerpt:
        'Q2 FY26 consolidated EBITDA rose 11.2% YoY to Rs 44,867 crore, led by Reliance Retail (+18.4%) and Jio (+13.1%). Net debt fell to Rs 1.09 lakh crore.',
    },
    {
      file: 'sector_energy.txt',
      excerpt:
        'Singapore GRMs averaged $8.20/bbl in the quarter versus $9.60 a year earlier, keeping refining a drag on integrated Indian energy names.',
    },
    {
      file: 'market_wrap_2026_08.txt',
      excerpt:
        'Nifty 50 closed the month +3.1% with energy and IT leading. Institutional flows turned net positive for the first time since May.',
    },
  ],
  portfolio: [
    { symbol: 'RELIANCE', pct: 20 },
    { symbol: 'TCS', pct: 15 },
    { symbol: 'HDFC', pct: 12 },
    { symbol: 'INFOSYS', pct: 8 },
  ],
  watchlist: [
    { symbol: 'TCS', signal: 'BULLISH' },
    { symbol: 'INFOSYS', signal: 'NEUTRAL' },
    { symbol: 'HDFC', signal: 'BEARISH' },
  ],
  metrics: { latency_s: 2.43, signal_accuracy: 78, risk_score: 42 },
  degraded: false,
  degraded_note: null,
}

async function analyze(symbol, profile) {
  // TODO: swap for the live call, e.g.
  //   const r = await fetch(`/api/analyze?symbol=${symbol}&profile=${profile}`)
  //   return r.json()
  await new Promise((resolve) => setTimeout(resolve, 1500))
  return MOCK
}

/* ------------------------------------------------------------------ *
 * Presentation
 * ------------------------------------------------------------------ */

const STOCKS = ['RELIANCE', 'TCS', 'INFOSYS', 'HDFC']
const PROFILES = ['Conservative', 'Moderate', 'Aggressive']

function signalClass(signal) {
  const s = String(signal || '').toUpperCase()
  if (s === 'BULLISH') return 'bullish'
  if (s === 'BEARISH') return 'bearish'
  return 'neutral'
}

function Meter({ value, tone = 'neutral' }) {
  const pct = Math.max(0, Math.min(100, Number(value) || 0))
  return (
    <div
      className="meter"
      role="meter"
      aria-valuenow={pct}
      aria-valuemin={0}
      aria-valuemax={100}
    >
      <div className={`meter-fill ${tone}`} style={{ width: `${pct}%` }} />
    </div>
  )
}

function App() {
  const [symbol, setSymbol] = useState('RELIANCE')
  const [profile, setProfile] = useState('Moderate')
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)

  async function runAnalysis() {
    setLoading(true)
    try {
      const result = await analyze(symbol, profile)
      setData(result)
    } finally {
      setLoading(false)
    }
  }

  // Load once so the demo opens with results already on screen.
  useEffect(() => {
    runAnalysis()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const up = data ? data.change_pct >= 0 : true

  return (
    <div className="app">
      <style>{CSS}</style>

      <header className="header">
        <h1>
          FININT<span className="dot">.</span>AI
        </h1>
        <p>
          Multi-agent equity intelligence — technicals, fundamentals and
          sentiment, synthesised into one call.
        </p>
      </header>

      <section className="controls">
        <label className="field">
          <span>Stock</span>
          <select
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            disabled={loading}
          >
            {STOCKS.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
        </label>

        <label className="field">
          <span>Risk profile</span>
          <select
            value={profile}
            onChange={(e) => setProfile(e.target.value)}
            disabled={loading}
          >
            {PROFILES.map((p) => (
              <option key={p} value={p}>
                {p}
              </option>
            ))}
          </select>
        </label>

        <button className="analyze" onClick={runAnalysis} disabled={loading}>
          {loading ? (
            <>
              <span className="spinner" />
              Analyzing…
            </>
          ) : (
            'Analyze'
          )}
        </button>
      </section>

      {loading && (
        <div className="loading-panel">
          <span className="spinner big" />
          <div>
            <strong>Running 3 agents on {symbol}</strong>
            <span>Technical · Fundamental · Sentiment</span>
          </div>
        </div>
      )}

      {!loading && data && (
        <main className="results">
          {data.degraded && (
            <div className="banner">
              <span className="banner-icon">⚠</span>
              <span>{data.degraded_note}</span>
            </div>
          )}

          <section className="card price-card">
            <div>
              <div className="label">Symbol</div>
              <div className="price-symbol">{data.symbol}</div>
            </div>
            <div>
              <div className="label">Last price</div>
              <div className="price-value">
                <span className="cur">₹</span>
                {data.price.toLocaleString('en-IN')}
              </div>
            </div>
            <div>
              <div className="label">Change</div>
              <div className={`price-change ${up ? 'pos' : 'neg'}`}>
                {up ? '▲' : '▼'} {up ? '+' : ''}
                {data.change_pct}%
              </div>
            </div>
          </section>

          <section className={`card signal-card ${signalClass(data.signal)}`}>
            <div className="signal-main">
              <div className="label">Consensus signal</div>
              <div className="signal-word">{data.signal}</div>
            </div>
            <div className="signal-conf">
              <div className="meter-head">
                <span className="label">Confidence</span>
                <span className="meter-num">{data.confidence}%</span>
              </div>
              <Meter value={data.confidence} tone={signalClass(data.signal)} />
            </div>
            <div className="signal-rec">
              <div className="label">Recommendation</div>
              <div className="rec-pill">{data.recommendation}</div>
            </div>
          </section>

          <section className="agents">
            {data.agents.map((a) => (
              <article key={a.agent} className="card agent-card">
                <div className="agent-head">
                  <h3>{a.agent}</h3>
                  <span className={`tag ${signalClass(a.signal)}`}>
                    {a.signal}
                  </span>
                </div>
                <div className="meter-head">
                  <span className="label">Confidence</span>
                  <span className="meter-num">{a.confidence}%</span>
                </div>
                <Meter value={a.confidence} tone={signalClass(a.signal)} />
                <p className="reason">{a.reason}</p>
                <div className="label">Evidence</div>
                <ul className="evidence">
                  {a.evidence.map((e) => (
                    <li key={e}>{e}</li>
                  ))}
                </ul>
              </article>
            ))}
          </section>

          <section className="card">
            <h2>Synthesis</h2>
            <p className="synthesis-text">{data.synthesis.text}</p>
            <div className="label">Reasoning</div>
            <ul className="reasoning">
              {data.synthesis.reasoning.map((r) => (
                <li key={r}>{r}</li>
              ))}
            </ul>
          </section>

          <section className="card">
            <h2>Sources</h2>
            <div className="sources">
              {data.sources.map((s) => (
                <div key={s.file} className="source">
                  <div className="source-file">{s.file}</div>
                  <p className="source-excerpt">{s.excerpt}</p>
                </div>
              ))}
            </div>
          </section>

          <section className="split">
            <div className="card">
              <h2>Portfolio</h2>
              <ul className="rows">
                {data.portfolio.map((p) => (
                  <li key={p.symbol}>
                    <span className="row-sym">{p.symbol}</span>
                    <span className="row-bar">
                      <span className="row-fill" style={{ width: `${p.pct}%` }} />
                    </span>
                    <span className="row-num">{p.pct}%</span>
                  </li>
                ))}
              </ul>
            </div>
            <div className="card">
              <h2>Watchlist</h2>
              <ul className="rows">
                {data.watchlist.map((w) => (
                  <li key={w.symbol}>
                    <span className="row-sym">{w.symbol}</span>
                    <span className={`tag ${signalClass(w.signal)}`}>
                      {w.signal}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          </section>

          <section className="metrics">
            <div className="card metric">
              <div className="label">Latency</div>
              <div className="metric-value">
                {data.metrics.latency_s}
                <span className="unit">s</span>
              </div>
            </div>
            <div className="card metric">
              <div className="label">Signal accuracy</div>
              <div className="metric-value">
                {data.metrics.signal_accuracy}
                <span className="unit">%</span>
              </div>
            </div>
            <div className="card metric">
              <div className="label">Risk score</div>
              <div className="metric-value">
                {data.metrics.risk_score}
                <span className="unit">/100</span>
              </div>
            </div>
          </section>
        </main>
      )}
    </div>
  )
}

const CSS = `
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #0b0c0e;
  color: #e8e9ec;
  font: 15px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
}

.app {
  --surface: #141619;
  --surface-2: #1b1e23;
  --border: rgba(255,255,255,0.09);
  --ink: #e8e9ec;
  --ink-2: #a6abb5;
  --ink-3: #757b86;
  --accent: #4d8df6;
  --green: #22c55e;
  --red: #ef4444;
  --amber: #fab219;

  max-width: 1180px;
  margin: 0 auto;
  padding: 32px 24px 72px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* header */
.header h1 {
  margin: 0;
  font-size: 30px;
  font-weight: 700;
  letter-spacing: 2px;
}
.header h1 .dot { color: var(--accent); }
.header p {
  margin: 6px 0 0;
  color: var(--ink-2);
  font-size: 14px;
}

/* controls */
.controls {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  flex-wrap: wrap;
  padding: 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
}
.field { display: flex; flex-direction: column; gap: 6px; }
.field > span {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--ink-3);
}
.field select {
  min-width: 170px;
  padding: 10px 12px;
  background: var(--surface-2);
  color: var(--ink);
  border: 1px solid var(--border);
  border-radius: 8px;
  font: inherit;
  cursor: pointer;
}
.field select:focus-visible,
.analyze:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.analyze {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 26px;
  background: var(--accent);
  color: #06121f;
  border: 0;
  border-radius: 8px;
  font: 600 15px/1 inherit;
  cursor: pointer;
  transition: filter .15s ease;
}
.analyze:hover:not(:disabled) { filter: brightness(1.1); }
.analyze:disabled { opacity: .6; cursor: default; }

.spinner {
  width: 13px; height: 13px;
  border: 2px solid rgba(0,0,0,.25);
  border-top-color: #06121f;
  border-radius: 50%;
  animation: spin .7s linear infinite;
}
.spinner.big {
  width: 22px; height: 22px;
  border-color: rgba(255,255,255,.15);
  border-top-color: var(--accent);
}
@keyframes spin { to { transform: rotate(360deg); } }

.loading-panel {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 40px 20px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
}
.loading-panel div { display: flex; flex-direction: column; }
.loading-panel span:last-child { color: var(--ink-3); font-size: 13px; }

.results { display: flex; flex-direction: column; gap: 18px; }

/* degraded banner */
.banner {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 13px 16px;
  background: rgba(250,178,25,0.12);
  border: 1px solid rgba(250,178,25,0.4);
  border-left: 3px solid var(--amber);
  border-radius: 10px;
  color: #f3d18a;
  font-size: 14px;
}
.banner-icon { color: var(--amber); font-size: 16px; }

/* cards */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 18px 20px;
}
.card h2 {
  margin: 0 0 12px;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: .4px;
}
.label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--ink-3);
}

/* price */
.price-card { display: flex; gap: 56px; flex-wrap: wrap; align-items: center; }
.price-symbol { font-size: 26px; font-weight: 700; letter-spacing: 1px; margin-top: 4px; }
.price-value { font-size: 30px; font-weight: 600; margin-top: 2px; }
.price-value .cur { color: var(--ink-3); font-size: 20px; margin-right: 2px; }
.price-change { font-size: 22px; font-weight: 600; margin-top: 4px; }
.price-change.pos { color: var(--green); }
.price-change.neg { color: var(--red); }

/* signal */
.signal-card {
  display: grid;
  grid-template-columns: minmax(200px, 1fr) 2fr auto;
  gap: 32px;
  align-items: center;
  padding: 26px 24px;
  border-left: 3px solid var(--ink-3);
}
.signal-card.bullish { border-left-color: var(--green); }
.signal-card.bearish { border-left-color: var(--red); }
.signal-card.neutral { border-left-color: var(--amber); }
.signal-word { font-size: 44px; font-weight: 700; letter-spacing: 2px; line-height: 1.1; margin-top: 4px; }
.signal-card.bullish .signal-word { color: var(--green); }
.signal-card.bearish .signal-word { color: var(--red); }
.signal-card.neutral .signal-word { color: var(--amber); }
.signal-rec { text-align: right; }
.rec-pill {
  display: inline-block;
  margin-top: 8px;
  padding: 9px 20px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 999px;
  font-weight: 600;
  letter-spacing: 1.5px;
}

/* confidence meter */
.meter-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px; }
.meter-num { font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums; }
.meter {
  height: 8px;
  background: rgba(255,255,255,0.08);
  border-radius: 999px;
  overflow: hidden;
}
.meter-fill { height: 100%; border-radius: 999px; background: var(--accent); transition: width .4s ease; }
.meter-fill.bullish { background: var(--green); }
.meter-fill.bearish { background: var(--red); }
.meter-fill.neutral { background: var(--amber); }

/* agents */
.agents { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.agent-card { display: flex; flex-direction: column; }
.agent-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
.agent-head h3 { margin: 0; font-size: 16px; font-weight: 600; }
.tag {
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .8px;
  border: 1px solid;
  white-space: nowrap;
}
.tag.bullish { color: var(--green); border-color: rgba(34,197,94,.4); background: rgba(34,197,94,.12); }
.tag.bearish { color: var(--red); border-color: rgba(239,68,68,.4); background: rgba(239,68,68,.12); }
.tag.neutral { color: var(--amber); border-color: rgba(250,178,25,.4); background: rgba(250,178,25,.12); }
.reason { color: var(--ink-2); font-size: 14px; margin: 14px 0 16px; }
.evidence, .reasoning, .rows { list-style: none; margin: 8px 0 0; padding: 0; }
.evidence li {
  position: relative;
  padding: 5px 0 5px 16px;
  font-size: 13px;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  border-top: 1px solid var(--border);
}
.evidence li:first-child { border-top: 0; }
.evidence li::before { content: "\\25B8"; position: absolute; left: 0; color: var(--accent); }

/* synthesis */
.synthesis-text { margin: 0 0 16px; font-size: 15px; color: var(--ink); max-width: 90ch; }
.reasoning li {
  position: relative;
  padding: 6px 0 6px 18px;
  font-size: 14px;
  color: var(--ink-2);
}
.reasoning li::before {
  content: "";
  position: absolute;
  left: 2px; top: 14px;
  width: 5px; height: 5px;
  border-radius: 50%;
  background: var(--accent);
}

/* sources */
.sources { display: flex; flex-direction: column; gap: 12px; }
.source {
  padding: 12px 14px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 9px;
}
.source-file {
  font: 600 12px/1 ui-monospace, Consolas, monospace;
  color: var(--accent);
  margin-bottom: 8px;
}
.source-excerpt { margin: 0; font-size: 13px; color: var(--ink-2); }

/* portfolio + watchlist */
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.rows li {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 0;
  border-top: 1px solid var(--border);
}
.rows li:first-child { border-top: 0; }
.row-sym { flex: 0 0 90px; font-weight: 600; font-size: 14px; }
.row-bar { flex: 1; height: 8px; background: rgba(255,255,255,0.08); border-radius: 999px; overflow: hidden; }
.row-fill { display: block; height: 100%; background: var(--accent); border-radius: 999px; }
.row-num { flex: 0 0 44px; text-align: right; font-size: 14px; font-variant-numeric: tabular-nums; }
.split .rows li .tag { margin-left: auto; }

/* metrics */
.metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.metric-value { font-size: 32px; font-weight: 600; margin-top: 6px; }
.metric-value .unit { font-size: 15px; color: var(--ink-3); margin-left: 3px; }

/* responsive */
@media (max-width: 900px) {
  .app { padding: 24px 16px 56px; gap: 14px; }
  .results { gap: 14px; }
  .controls { flex-direction: column; align-items: stretch; }
  .field select, .analyze { width: 100%; justify-content: center; }
  .agents, .split, .metrics { grid-template-columns: 1fr; }
  .signal-card { grid-template-columns: 1fr; gap: 20px; }
  .signal-rec { text-align: left; }
  .price-card { gap: 28px; }
  .signal-word { font-size: 36px; }
}
`

export default App
