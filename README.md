# Tour Assistant — an AI visitor assistant for a small tour company

A Claude Code agent that answers customer questions from a tour company's own
documents, drafts email replies in the owner's voice, and logs anything it
can't answer so the owner can follow up. Built as a portfolio project and as the
demo for an AI services business serving small businesses in Gettysburg, PA.

The sample company, Gettysburg Lantern Tours, is fictional. Swap the `docs/`
folder for a real business's content and the assistant becomes theirs.

## The problem

Small tour companies answer the same questions dozens of times a week: which
tour is right for kids, how much walking, where to park, what if it rains. The
owner answers every email personally, often at night. Generic chatbots make
things up, which is worse than no answer at all when a wrong price or time costs
a booking.

## What this does

Ask it anything a visitor would ask. It reads the company's documents and
answers in a few friendly sentences, with exact prices and times. When the
answer isn't in the documents, it says so, asks for the visitor's email, and
records the question for the owner.

**Try it:** open this folder in Claude Code and type:

> We have a 6-year-old and my mom uses a cane. Which tour should we do?

Then try one it can't know:

> Do you offer tours in Spanish?

Then ask for the report:

> What have people been asking that you couldn't answer?

## How it's built

```
tour-assistant/
├── CLAUDE.md                 the agent's instructions: voice, grounding rule, when to decline
├── docs/                     the company's knowledge: tours, FAQ, policies, about
├── .claude/skills/           step-by-step procedures the agent follows
│   ├── answer-visitor-question/
│   ├── draft-email-reply/
│   └── weekly-inquiry-report/
├── mcp_server/inquiry_log.py a small tool server (MCP) that saves unanswered questions
├── .mcp.json                 tells Claude Code how to start that server
└── data/inquiries.json       the log, created on first use (not committed)
```

Three ideas carry the design:

1. **Grounding.** The agent may only answer from `docs/`. The instructions say
   it plainly and the answer skill repeats it. In testing, the agent declines
   questions the documents don't cover instead of guessing.
2. **Skills as procedures.** Each skill is a short checklist the agent follows
   for one kind of request. The owner can read them. Changing how emails sound
   means editing a text file, not code.
3. **A tool the agent can call.** The MCP server is about 60 lines of Python.
   It gives the agent `log_inquiry` and `list_inquiries`. That turns "I don't
   know" into a lead for the owner, and the weekly report turns the log into a
   list of what to add to the documents.

## What I learned

- An agent is mostly instructions plus documents plus a few tools. The code is
  the smallest part.
- The grounding rule has to be stated as the single most important thing, with
  the fallback spelled out, or the model drifts toward being helpful by guessing.
- MCP is simpler than it sounds: a Python function with a docstring becomes a
  tool the agent can see and call.

## Running it yourself

Requirements: Python 3.11 or newer and Claude Code.

```bash
pip install "mcp>=2"
```

Open the folder in Claude Code. The first time, approve the `inquiry-log` MCP
server when asked. Then ask a question.

## Adapting it for another business

1. Replace the files in `docs/` with the business's tour list, FAQ, and policies.
2. Change the company name at the top of `CLAUDE.md`.
3. Done. The skills and the tool server don't need to change.

## Next steps

- A fully local version using Ollama and a short Python agent loop, to show
  the same idea without a hosted model.
- A web chat widget so the assistant can live on the business's website.
