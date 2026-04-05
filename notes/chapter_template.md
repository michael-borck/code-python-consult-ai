# Chapter Template: Code Python, Consult AI

Every chapter follows this structure. Target: 350-450 lines.

## Structure

```markdown
# [Chapter Title]

## The Wall

A specific vibe-coding failure the reader recognises.
2-3 paragraphs. Ends with: "This chapter fixes that."

Pattern:
- You asked AI to [specific task]
- It gave you [specific output]
- It [broke / did the wrong thing / confused you]
- You couldn't [diagnose / fix / understand] because you didn't know [concept]


## Thinking Session

### Getting Oriented

::: {.callout-note title="Thinking Session Prompt"}
[Opening prompt — broad question about the concept.
Not "explain X" but "why does X exist and what
happens when it goes wrong?"]
:::

[2-3 lines of author guidance: what to look for
in the AI's response, what matters, what to push
back on if the AI oversimplifies]


### Go Deeper

::: {.callout-note title="Thinking Session Prompt"}
[Follow-up prompt that pushes into practical
understanding — examples, comparisons, patterns]
:::

[Brief author narration connecting to the concept]

::: {.callout-note title="Thinking Session Prompt"}
[Another follow-up — different angle on the concept]
:::

[Brief narration]


### Challenge It

::: {.callout-note title="Thinking Session Prompt"}
[Prompt with broken code or a misconception.
"What's wrong with this?" / "Why would this fail?"]
:::

::: {.callout-tip title="What to Look For"}
[What the AI should explain. What the reader should
understand from this exchange.]
:::


### What You Should Have Learned

After your Thinking Session, you should be able to:

- [Concrete understanding point 1]
- [Concrete understanding point 2]
- [Concrete understanding point 3]
- [Concrete understanding point 4]

If any of these are unclear, continue the conversation
with your AI before moving on.


## The Gap

[Author voice. No AI conversation. 2-3 paragraphs.]
[Connect Thinking Session to Building Session.]
[Frame what you're about to build and why the concept
matters for it.]


## Building Session

### The Spec

Add [specific feature] to your chatbot:

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
- [Constraint: keep it simple / no classes / etc.]

### Prompt It

::: {.callout-note title="Building Session Prompt"}
[The intentional prompt. Specific, constrained,
informed by the Thinking Session understanding.
This is what the reader pastes into a fresh AI chat.]
:::

### Read the Code

Your AI will produce something like this:

```python
[Representative code — not exact, since every AI
will produce slightly different output. Show the
version that best demonstrates the concept.]
```

::: {.callout-tip title="What to Notice"}
[Walk through 3-5 specific lines. Not explaining
from scratch — confirming what was explored in the
Thinking Session. "Notice how line 5 uses..."]
:::

### Stretch It

::: {.callout-note title="Building Session Prompt"}
[Modification prompt — extend the code, apply the
concept further. "Now ask your AI to add..."]
:::

[1-2 lines on what to look for in the modified code]


## Your Chatbot So Far

After this chapter, your chatbot can:

- [Cumulative capability from chapter 1]
- [Cumulative capability from chapter 2]
- **[New capability added this chapter]**


## Quick Reference

```python
# [Concept] patterns
[pattern 1]       # [brief note]
[pattern 2]       # [brief note]
[pattern 3]       # [brief note]
```
```

## Guidelines

### Prompts
- Must work with any AI (ChatGPT, Claude, Gemini, etc.)
- No AI-specific features (vision, file upload, etc.)
- Copy-pasteable — reader should be able to paste directly
- Conversational tone — "I'm learning..." not "Generate..."

### Author Voice
- Direct, brief, confident
- UK/Australian English spelling
- No emojis
- No "let's" or "we'll" — address the reader as "you"
- The author is a guide, not a lecturer

### Code Blocks
- ```python for actual code
- ```text for AI prompts and output
- No nesting of fences
- Each speaker turn in a conversation = separate text block

### Callout Boxes
- .callout-note title="Thinking Session Prompt" — for AI prompts in Thinking Session
- .callout-note title="Building Session Prompt" — for AI prompts in Building Session
- .callout-tip title="What to Look For" / "What to Notice" — for author guidance
- .callout-warning — for gotchas only (use sparingly)

### Chatbot Project
- Each chapter adds ONE feature
- Building Session code should be ~20-40 lines
- Cumulative — reader builds on previous chapters
- No classes until the Objects chapter
- No imports until the relevant chapter introduces them
