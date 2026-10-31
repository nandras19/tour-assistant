---
name: weekly-inquiry-report
description: Summarize the questions the assistant could not answer, grouped by theme, with suggested additions to docs/. Use when the owner asks for a report, summary, or what people have been asking.
---

# Weekly inquiry report

## Steps

1. Call `list_inquiries` to get every logged question. If two entries are
   clearly the same visitor and question, count them once.
2. Group them by theme (for example: pricing, accessibility, group bookings,
   things we don't offer).
3. For each theme, count the questions and quote one representative example.
4. For each theme, suggest in one sentence what to add to which file in `docs/`
   so the assistant can answer next time. If the business should consider a new
   offering (several people asked for the same thing we don't do), say so plainly.
5. List any inquiry that has a visitor email and still needs a personal reply.

## Output format

```
# Inquiry report — <date range>

<N> questions the assistant couldn't answer.

## <Theme> (<count>)
Example: "<quoted question>"
Suggested fix: add <what> to docs/<file>.md

## Follow-ups owed
- <email> asked "<question>" on <date>
```

Keep it to one screen. The owner reads this on a phone.
