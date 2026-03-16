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
      (fixed) 5. Updating difficulty doesn't update secret even if it out of range
      ------------
      4. Accepts numbers outside of the range, 1-100
      7. History is behind - it updates with the previous guess on your current guess
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used the Claude extension in VS code in the project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One suggestion from the AI that was correct was pointing out that history wasn't being refreshed when a new game was started was linked to a missing line for resetting state. I verified the result by modifiying that line and observing the history shown in developer debug info.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One suggestion of an AI suggestion that was somewhat incorrect was adding validation for checking if a guess was within the range of the current difficulty. While it correctly wrote the logic in logic_utils.py to check against difficulty, it didn't update the inputs to include difficulty where the parse_guess function was called, resulting in the utility function always checking against the default difficulty, normal. This was a bug I fixed manually.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I used pytests to check if isolated parts of the code performed and returned outputs as expected, and I also manually tested the game through the user interface live.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran were the default tests checking whether a guess was a winning guess, too high, or too low. This test showed me that sometimes bugs may stem from the test case itself - the test wasn't used the tested function, check_guess(), correctly, but fixing that fixed the bugs.
- Did AI help you design or understand any tests? How?
AI helped design the tests I used to check the new range validation feature, and I verified their logic manually.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
I'm not sure that the secret number changed, but the score was buggy. When the guess was too high, it would still increment the score if the attempt was even, which was incorrect, because non-winning guesses should decrement the score.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns any time you interact with a part of its interface - such as clicking a button or modifying an input field. Session state may update accordingly.
- What change did you make that finally gave the game a stable secret number?
For the score, I modified the logic to ensure it always decremented regardless of whether the attempt was even or odd if it wasn't a winning guess.
**

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I will use AI more to quickly understand unfamiliar code and point to the root of errors to allow me to identify what parts of the code are most critical to familiarize with.
- What is one thing you would do differently next time you work with AI on a coding task?
  I will likely use it to try generating tests again.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project made me realize that AI often loses sight of the full picture. It'll fix a bug in one area, but potentially introduce a bug in another due to forgetting to update changes on both ends.