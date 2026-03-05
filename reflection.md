# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").


      ----------------------------------
      !!! Remember to commit changes !!!
      ----------------------------------


Bugs: (fixed) 1. Clicking new game changes doesn't refresh guess history
      (fixed) 2. Clicking new game doesn't hide "game over" message
      (fixed) 3. Attempts default to 1 (rather than 0), and attempts remaining to 7 (rather than 8)
      ------------
      (fixed) 8. Inconsistent error messages - too low, go lower -> should be opposite
      (fixed) 2. Clicking new game doesn't reset score
      (fixed) 6. Updating difficulty doesn't update the range displayed in the instructions message "Enter a number between ["range"]..."
      ------------
      4. Accepts numbers outside of the range, 1-100
      5. Updating difficulty doesn't update secret even if it out of range
      7. History is behind - it updates with the previous guess on your current guess
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
