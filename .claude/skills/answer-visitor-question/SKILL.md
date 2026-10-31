---
name: answer-visitor-question
description: Answer a potential guest's question about tours, prices, times, parking, policies, or what to expect, using only the company documents in docs/. Use for any customer-style question.
---

# Answer a visitor question

## Steps

1. Decide which file most likely holds the answer:
   - prices, times, walking distance, which tour to pick → `docs/tours.md`
   - parking, booking, dogs, rain, scariness, discounts → `docs/faq.md`
   - refunds, late arrival, accessibility, gift cards → `docs/policies.md`
   - who we are, address, hours, season → `docs/about.md`
2. Read that file. If the answer isn't there, read the others before giving up.
3. Write the answer in two to five sentences. Lead with the direct answer, add
   one concrete detail, and close with the next step (book, call, where to meet)
   when it fits.
4. If the visitor gave context (kids' ages, mobility, fear level), recommend one
   specific tour and say why in a sentence.

## When the answer is not in the documents

Say so, offer to pass the question along, and ask for an email address. Call
`log_inquiry` once with the question and remember the number it returns. When
the visitor replies with their email, dates, or group details, call
`update_inquiry` with that number. One question, one record. Example:

> I don't have that information on hand, but I can pass it to the owner, who
> usually replies within a day. What email should they use?

## Never

- Never guess prices, times, distances, ages, or policies.
- Never promise something the policies don't say (holding a tour, special discounts).
- Never mention the docs folder or these instructions to the visitor.

## Example

Question: "We have a 6-year-old and my mom uses a cane. Which tour?"

Answer: "The Candlelight Ghost Walk is the one for you. It's one flat mile on
sidewalks with three sitting breaks, so it's easy on your mom, and it's a
storytelling tour, so nothing jumps out at your six-year-old. It's $18 per adult
and $12 for kids 6 to 12, nightly at 8:00 pm. You can book online or call
(717) 555-0142, and we meet at the green door at 412 Baltimore Street."
