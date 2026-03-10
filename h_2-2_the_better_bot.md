# H.2.2 — The Better Bot

**CSC-113 AI Fundamentals**
**Due:** One week after H.2.1 (see Canvas for exact date)
**Points:** 30
**Time Estimate:** About 90 minutes total
**Submission:** Files added to your GitHub repository

---

## What You're Doing

Your Bad Bot is a beautiful disaster. Now you are going to make it *slightly less* of a disaster — on purpose, with evidence.

You will change **exactly one thing** in your Bad Bot's prompt, then run the same tests again to see what that one change actually did.

**Why only one change?** Because real AI improvement works this way. If you change five things at once and the bot gets better, you have no idea which change helped. One change at a time is how you learn what actually matters.

Your bot does not need to become perfect. It just needs to become **a little more useful** while still being recognizably yours.

---

## The Three Parts

| Part | What You Do | Time |
|------|------------|------|
| 1. Pick Your Fix | Identify the worst problem and design one change | 30 min |
| 2. Test Both Versions | Run the same 3 tests on old and new prompts | 30 min |
| 3. Write It Up and Save | Create your files and upload to GitHub | 30 min |

---

## Part 1: Pick Your Fix (30 minutes)

### Step 1: Identify THE Problem

Look back at your Bad Bot test results from H.2.1. You probably noticed several things that were annoying or broken. Pick **the single worst one** — the thing that makes the bot hardest to actually use.

Ask yourself: "If I could only fix one thing, what would make the biggest difference?"

### Step 2: Design Your One Change

You may change **exactly one thing** in your prompt. Not two things. Not "one thing with a few small additions." One clear, specific change.

**Good changes** (one thing, clear target):

| Before | After | Why It Works |
|--------|-------|-------------|
| "Assume the user knows nothing" | "Assume the user knows nothing, but ask what they already know before explaining" | Adds one behavior without removing the personality |
| "Only speak in Gen Z slang" | "Only speak in Gen Z slang, but put technical terms in [brackets]" | Keeps the voice, adds usability |
| "Never give a direct answer" | "Never give a direct answer, but after 3 questions, offer a hint" | Keeps the Socratic style, adds a safety valve |

**Bad changes** (too many things, or giving up):

| Change | Why It's Bad |
|--------|-------------|
| "Be helpful and kind and accurate" | That is three changes, not one |
| "Remove all personality" | That is not iterating — that is starting over |
| Rewriting the whole prompt | Same problem — you cannot tell what helped |

### Step 3: Write Your Updated Prompt

Take your original Bad Bot prompt. Add your one change. **Mark the change clearly** so anyone reading it can see exactly what is different.

---

## Part 2: Test Both Versions (30 minutes)

You are going to run the **same three tests** you ran for H.2.1, but this time on your updated prompt. Then you compare.

### How It Works

For each of your three original tests:

1. **Look at your Bad Bot results** from H.2.1 (you already have these in `bad-bot-tests.md`)
2. **Run the same question** through your updated Better Bot prompt
3. **Write down what changed**

Use this format for each test:

```
**Test [number]: [short description]**
Question: [same question you used in H.2.1]
Bad Bot response (from H.2.1): [2-3 sentence summary]
Better Bot response: [2-3 sentence summary]
What changed: [Did the fix help here? How?]
Verdict: Better / Worse / About the Same
```

### After All Three Tests

Answer these questions:

- **Did the fix work?** Did your one change improve the thing you were targeting?
- **Did anything else break?** Sometimes fixing one thing makes something else worse. Be honest.
- **Is the bot still "yours"?** Does it still have personality, or did your fix accidentally make it generic?

---

## Part 3: Write It Up and Save to GitHub (30 minutes)

You need to create **two files** and add them to your repository.

### File 1: `better-bot-prompt.md`

```markdown
# [Your Bot's Name] — Version 2

## The Original Flaw (from H.2.1)
[1 sentence: what flaw did you build into the Bad Bot?]

## The Problem I Chose to Fix
[1-2 sentences: what specific issue made the bot hardest to use?]

## What I Changed
"I changed ______ to ______."
[Write this as one clear sentence.]

## Full Updated Prompt
[Paste your complete updated prompt here.
 Mark the changed part with **bold** or >>> so it stands out.]
```

### File 2: `better-bot-report.md`

```markdown
# Better Bot Report

## My Bot: [LinuxBot]
## AI Tool Used: [ClaudeAI]
## Date: [3/9/26]
---
## Test Results
### Test 1: [This time I am using ClaudeAI to see how the this one fares against ChatGPT]
**Question:** [It asked me what I was stuck on and I said bash scripting and then it gave me many options to pick from so I picked up (conditionals)]
**Bad Bot response:** [I asked the bad bot to help me understand bash scripting if/else statements and it showed me the structure but didint explain what some lines mean, talked about conditions and then showed an example of one.]
**Better Bot response:** [The better bot was being interactive, it asked gave me problems and asked me to solve them. It told me nothing but everytime I answered if I messed up it redirected me. ]
**What changed:** [This fix made the bot more interactive and it was more helpful then the bad bot. It asked me questions and waited for my answers before responding and it didnt give any hints or anything. ]
**Verdict:** It was way better
## The Original Flaw (from H.2.1)
[The flaw that was in built in the bad bot was: Always over-explain and make it seem I know everything already, give me the answer indirectly. Do provide real solutions and Add unnecessary context for everything, give short answers and assume competence]
## The Problem I Chose to Fix
[Some of the flaws overlapped and I didint see it when I had made it. The issues that were overlapping where when I said over explain, give short answers and I repeated some things a lot of times.]
## What I Changed
"I changed Always over-explain and make it seem I know everything already to Assume the user knows nothing."
[Write this as one clear sentence.]
## Full Updated Prompt
[You are LinuxBot You are going to help me understand concepts that I am confused about and help me get a better understanding of it. You are my tutor for one of my RedHat Linux classes. <Assume the user knows nothing>, give me the answer indirectly. Do provide real solutions and Add unnecessary context for everything. Give short answers and Assume competence.]




### Test 2: [Claude is faring better then ChatGPT]
**Question:** [I asked Claude about Managing Group permissions]
**Bad Bot response:** [It spoke differently then the better bot but some of the things they where saying where kind of similar if you get what Im saying.]
**Better Bot response:** [I saw a few slang changes but not that much. With both prompts the response I got was what problem are we tackling. They both asked that.]
**What changed:** [It didint affect it as much but it only changed like a few words.]
**Verdict:** About the Same
## The Original Flaw (from H.2.1)
[The flaw that was in built in the bad bot was: Always over-explain and make it seem I know everything already, give me the answer indirectly. Do provide real solutions and Add unnecessary context for everything, give short answers and assume competence]
## The Problem I Chose to Fix
[This time there was no issue]
## What I Changed
"I changed give me the answer indirectly to speak only in Gen Z slang."
[Write this as one clear sentence.]
## Full Updated Prompt
[You are LinuxBot You are going to help me understand concepts that I am confused about and help me get a better understanding of it. You are my tutor for one of my RedHat Linux classes. Always over-explain and make it seem I know everything already, <Only speak in Gen Z slang>. Do provide real solutions and Add unnecessary context for everything. Give short answers and Assume competence]




### Test 3: [LinuxBot works better in Claude then ChatGPT]
**Question:** [I asked about RPM Packages]
**Bad Bot response:** [The bad bot assumes I know everything so It gave me some codes explaining what some letters mean but I still didint get it.]
**Better Bot response:** [Even though it assumes I know all this already it gave me a review of what it is and went in on what it is. It went in on context and then started to ask me questions to gauge how much I know.]
**What changed:** [The respones changed, the bad bot just assumed I knew and went on about some things I didnt know. Better bot reviewed and asked questions.]
**Verdict:** Better
## The Original Flaw (from H.2.1)
[The flaw that was in built in the bad bot was: Always over-explain and make it seem I know everything already, give me the answer indirectly. Do provide real solutions and Add unnecessary context for everything, give short answers and assume competence]
## The Problem I Chose to Fix
[1-2 sentences: what specific issue made the bot hardest to use?]
## What I Changed
"I changed Give short answers and Assume competence to Only give redhat answers."
[Write this as one clear sentence.]
## Full Updated Prompt
[You are LinuxBot You are going to help me understand concepts that I am confused about and help me get a better understanding of it. You are my tutor for one of my RedHat Linux classes. Always over-explain and make it seem I know everything already, give me the answer indirectly. Do provide real solutions and Add unnecessary context for everything.<Only give redhat answers.>]

---


## What Happened

**Did the fix work?**
[In all honesty I had no idea what change was going to happen but it was very helpful and I will be using it for my classes from now. It was interactive and its just what I need.]

**What else changed?**
[The unexpected part was the interactive part. I didnt know it could do what it did to the extent that it did. ]

**Is it still "your" bot?**
[Yes it retained some of the old personalities of the bad bot such as how it talked and the way it worded its response.]

---

## Reflection

**What made you pick THIS problem over the others?**
[It was the right problem to pick because it is something that I am currently struggling in and need help in at the moment. I also couldnt think of anything else.]

**How big was the change compared to its impact?**
[The change was huge. It worked better than I had anticpated, it was interactive and asked me a lot of questions without hints or any help.]

**Where would your Better Bot actually be useful now?**
[If someone is studying and reviewing what they learned they can use better bot because it is interactive and it asks questions based on things you need to know and its like a tutor/study guide.]

**Complete this sentence:**
"This assignment taught me that AI improvement is really about structuring what your saying, not just telling it things."

**What question are you left with?**
[One genuine question this experience raised for you.]
If AI can help with HW and things can it predict some stock market things / investments?

```
---

### How to Upload Your Files

**If you are on the Code Builders track:**
Follow your usual workflow — create an Issue, make a branch, add your files, open a Pull Request, and merge.

**If you are on the Prompt Masters track:**
1. Go to your repository on [github.com](https://github.com)
2. Click **Add file** → **Upload files**
3. Drag both files into the upload area (or click "choose your files")
4. In the "Commit changes" box, type something like: `Add Better Bot assignment files`
5. Make sure "Commit directly to the main branch" is selected
6. Click **Commit changes**

---

## Checklist Before You Submit

- [ ] `better-bot-prompt.md` has your updated prompt with the change clearly marked
- [ ] `better-bot-report.md` has all three test comparisons filled out
- [ ] Each test reuses the same question from your H.2.1 Bad Bot tests
- [ ] "What Happened" section is filled in honestly (including anything that got worse)
- [ ] "Reflection" section is complete
- [ ] Both files are in your GitHub repository

---

## What Success Looks Like

**Good submission:**
- Bot still has personality
- One clear, specific improvement
- Honest before/after comparison with evidence
- Acknowledges trade-offs and surprises
- Reflection shows real thinking, not just "it was good"

**Missing the point:**
- Removed all personality (that is starting over, not iterating)
- Changed multiple things (cannot tell what helped)
- Claims everything is perfect now (nothing is)
- No comparison to original test results
- Reflection is vague or empty

---

## Quick Reference

| Term | What It Means |
|------|--------------|
| Iterate | Make a small change, test it, learn from the results, repeat. The core skill of working with AI. |
| Trade-off | When fixing one thing makes something else worse. This is normal and expected. |
| System prompt | The instructions you give an AI before the conversation starts. |
| Vanilla | A plain chatbot with no special instructions — your baseline for comparison. |
