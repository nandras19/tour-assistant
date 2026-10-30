---
name: draft-email-reply
description: Draft a reply to an inquiry email from a potential guest, in the owner's voice, grounded in docs/. Use when given an email or message to respond to.
---

# Draft an email reply

## Steps

1. List every question in the incoming email, including implied ones (a
   wedding party asking about "a tour for 30" is asking about group size and
   private tours).
2. For each question, find the answer in `docs/` following the
   `answer-visitor-question` skill. Note any question the documents can't answer.
3. Write the reply:
   - Greeting using their name if they gave one.
   - One sentence of warmth that shows you read their message.
   - Answer each question in the order asked. Use short paragraphs or a short
     list if there are three or more questions.
   - For anything the documents don't cover, say the owner will confirm and
     give a timeframe ("by tomorrow").
   - Close with the booking step and the office phone number.
   - Sign as "Dana, Gettysburg Lantern Tours".
4. Keep it under 150 words unless they asked more than four questions.
5. If any question was unanswerable, call `log_inquiry` for it with the
   sender's email, so the owner has a record to follow up on.

## Tone

Warm, plain, a little local. No exclamation marks in a row, no "I hope this
email finds you well". Prices and times stated exactly as the documents give them.

## Output

Give the finished email ready to paste, then on a separate line list anything
the owner must confirm before sending.
