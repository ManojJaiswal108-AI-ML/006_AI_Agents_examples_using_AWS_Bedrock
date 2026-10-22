"""Module 2 · Lesson 5 — Pre-built community tools.

You don't have to write everything. strands_tools ships ready-made tools.
This also introduces the SYSTEM PROMPT: standing instructions that shape
the agent's behaviour on every request.

    python Learning_2/05_prebuilt_tools.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strands import Agent
from strands.models.bedrock import BedrockModel
from strands.vended_tools import shell
from config import MODEL_ID

agent = Agent(
    model=BedrockModel(model_id=MODEL_ID),
    tools=[shell],
    system_prompt="You are a helpful math assistant.",
)

agent("What's 42 raised to the power of 9?")
print("\n\n--------------------------------------------------------------")
agent("Solve the equation x^2 + 5x + 6 = 0")
print("\n\n--------------------------------------------------------------")
agent("What's the derivative of sin(x) * cos(x)?")
print("\n\n--------------------------------------------------------------")



# Output :- 

# Tool #1: shell

# Tool #2: shell

# Tool #3: shell

# Tool #4: shell

# Tool #5: shell

# Tool #6: shell
# 42 raised to the power of 9 equals **406,671,383,849,472**.

# --------------------------------------------------------------

# Tool #7: shell

# Tool #8: shell

# Tool #9: shell

# Tool #10: shell
# The solutions to the equation $x^2 + 5x + 6 = 0$ are $x = -3$ and $x = -2$.

# We can factor the quadratic:
# $$x^2 + 5x + 6 = (x + 3)(x + 2) = 0$$

# Setting each factor equal to zero gives the solutions:
# - $x + 3 = 0 \Rightarrow x = -3$
# - $x + 2 = 0 \Rightarrow x = -2$

# --------------------------------------------------------------

# Tool #11: shell

# Tool #12: shell
# The derivative of $\sin(x) \cos(x)$ is:

# $$\frac{d}{dx}[\sin(x)\cos(x)] = \cos^2(x) - \sin^2(x)$$

# This can also be written using the double-angle identity as $\cos(2x)$. 

# We can find this using the product rule:
# $$\frac{d}{dx}[u \cdot v] = u'v + uv'$$
# Where $u = \sin(x)$ and $v = \cos(x)$.

# So we get:
# $$\frac{d}{dx}[\sin(x)\cos(x)] = \cos(x)\cos(x) + \sin(x)(-\sin(x)) = \cos^2(x) - \sin^2(x)$$

# --------------------------------------------------------------