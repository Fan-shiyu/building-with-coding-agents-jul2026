# Starter prompt (Part A)

Copy everything in the box below — including the last line — and paste it
into your coding agent.

```text
I have some sales CSVs in the data folder. Build me a nice interactive
dashboard in Python with some charts showing the important trends and
insights. Make it look professional and easy to use.

Before writing any code, show me your implementation plan first.
```

## Why this prompt is realistic — and bad

It's not a strawman. It has real information: the data location, the
language, the deliverable, even a quality wish. Prompts like this get
written thousands of times a day, and they *feel* complete when you type
them.

But look at what it leaves the agent to invent:

- **"some charts"** — which charts? How many? Of what?
- **"important trends and insights"** — important to whom, measured how?
- **"nice … professional"** — undefined. The agent will guess a style.
- **No file structure** — the agent will pick one. It won't match your
  teammates'.
- **No library choice** — matplotlib? Plotly? Altair? Coin flip.
- **No constraints** — nothing stops it from modifying your data files or
  installing anything it fancies.

The last line (plan first) is the only part we added for the exercise —
it lets you *see* the guesses before they become code.
