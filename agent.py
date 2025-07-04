import os
import datetime
import pytz
from dotenv import load_dotenv
from calendar_utils import create_event
import dateparser

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType

load_dotenv()

import dateparser

def booking_tool(title_with_time: str) -> str:
    print("[TOOL] Raw title input:", title_with_time)

    try:
        # Try to split title and time
        if " at " not in title_with_time:
            raise ValueError("Missing 'at' in input")

        title, time_str = title_with_time.split(" at ", 1)

        # Parse the time part only
        parsed_time = dateparser.parse(
            time_str,
            settings={'TIMEZONE': 'Asia/Kolkata', 'RETURN_AS_TIMEZONE_AWARE': True}
        )

        if not parsed_time:
            raise ValueError("Unable to parse time from input")

        end_time = parsed_time + datetime.timedelta(hours=1)

        print(f"[TOOL] Parsed start: {parsed_time}, end: {end_time}")

        return create_event(
            summary=title.strip(),
            start_time=parsed_time.isoformat(),
            end_time=end_time.isoformat()
        )
    except Exception as e:
        print(f"[ERROR in booking_tool]: {str(e)}")
        return f"Failed to parse time or create event: {str(e)}"


tools = [
    Tool(
        name="BookCalendarEvent",
        func=booking_tool,
        description="Use this to book calendar events"
    )
]

# ✅ Together.ai-compatible endpoint
llm = ChatOpenAI(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    openai_api_key=os.getenv("TOGETHER_API_KEY"),
    openai_api_base="https://api.together.xyz/v1",
    temperature=0
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


async def run_agent(user_input: str) -> str:
    print(f"[DEBUG] run_agent called with: {user_input}")

    prompt = f""" You are a helpful assistant that extracts the event title and time from user requests to schedule calendar events.

Please rephrase the following user input into a single line format like:

    <title> at <time>

Examples:
- "Schedule a call with Arjun tomorrow at 3 PM" → "Call with Arjun at tomorrow 3 PM"
- "Meeting with team on Friday at 2 PM" → "Team meeting at Friday 2 PM"

Now process this:
"{user_input}"

Respond only with the formatted line — no explanation.
"""

    try:
        response = llm.invoke(prompt)
        parsed_line = response.content.strip().strip('"')
        print("[DEBUG] LLM parsed:", parsed_line)

        return booking_tool(parsed_line)
    except Exception as e:
        print("[ERROR in run_agent]:", str(e))
        return f"Failed to process request: {str(e)}"
