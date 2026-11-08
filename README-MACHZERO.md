




round 2:

thought processes go here

for now, ideating and nothing much 

thought of another solution where we add a numerical value but it is a lot of overhead and somehow trying to find a workaround

apart from the main solution. a check for v3 by equating the v3 to the computed v1 values. 

round 3:
added the add usuage funch and gemini mu,ti chunk regression test as well 

### Environment & Tools

- **Operating System:** Windows 11 (64-bit)
- **Programming Language:** Python 3.14.2
- **Testing Framework:** Pytest 9.2.0
- **Project:** LangChain Core
- **Editor:** Visual Studio Code
- **Testing Plugins:** pytest-asyncio, pytest-mock, Syrupy
- **Version Control:** Git and GitHub

### Testing

Added a Gemini-style multi-chunk regression test to verify that token usage details are correctly accumulated across streamed responses.

**Test Result:** 1 passed, 0 failed.
the exact issue here where the .update func is Cached-token (cache_read) and reasoning-token counts are overwritten by the final chunk instead of being summed. The top-level token totals remain correct.
<img width="940" height="618" alt="image" src="https://github.com/user-attachments/assets/a11f32ba-aed2-4611-b2ec-c968646e3c57" />

fixed the .update issue by replacing it with the add usuage func
<img width="1487" height="505" alt="image" src="https://github.com/user-attachments/assets/572297c4-3eb2-46ee-9504-0b7397758cff" />


<img width="1475" height="700" alt="image" src="https://github.com/user-attachments/assets/c88f9d24-5939-4d26-840a-45e889bdb7ce" />


