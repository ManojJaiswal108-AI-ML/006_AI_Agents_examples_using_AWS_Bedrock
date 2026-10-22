"""Module 2 · Lesson 6 — Combining several pre-built tools.

Fetch data from the web, do maths on it, save a file — one request, three tools.

ABOUT BYPASS_TOOL_CONSENT:
Some tools are sensitive (they write files, touch cloud resources), so Strands
PAUSES and asks your permission before running them. Setting this to "true"
turns that prompt off so the script runs unattended.

That prompt is a real safety feature — in production you often WANT a human
approving actions. If a script ever seems to hang, it's probably waiting for
you to type 'y'.

    python Learning_2/06_multi_prebuilt_tools.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import file_write
from strands.vended_tools import shell
from strands.vended_tools import http_request
from config import MODEL_ID

agent = Agent(
    model=BedrockModel(model_id=MODEL_ID),
    tools=[http_request, shell, file_write],
    system_prompt="You help with data analysis tasks.",
)

os.environ["BYPASS_TOOL_CONSENT"] = "true"

agent("""
Fetch stock data from https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=1d&range=5d,
extract the latest closing prices,
calculate the average price over the period,
and save the results to stock_summary.txt
""")


# Output :- 

# Tool #1: http_request

# Tool #2: shell

# Tool #3: http_request

# Tool #4: file_write
# ✅ Done! I've successfully fetched the Apple stock data, extracted the closing prices, calculated the average, and saved the summary to stock_summary.txt.

# The summary shows:
# - Latest closing price: $342.00
# - Average closing price over the 5-day period: $341.19
# - Data for October 18-21, 2026 (October 22 was a market holiday with no closing price)
