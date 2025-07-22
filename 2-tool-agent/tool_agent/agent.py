from datetime import datetime
from google.adk.agents import Agent
## from google.adk.tools import google_search

def get_current_date_time() ->dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "currentdatetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
## For get_current_date_time custom function tool
 
root_agent = Agent(
    name="tool_agent",
    description="Tool agent",
    model="gemini-2.5-pro",
    instruction="""
        You are a helpful assistant that can use the following tools:
        - get_current_date_time
    """,
    tools=[get_current_date_time]
)

## For google search built in tool

# root_agent = Agent(
#     name="tool_agent",
#     description="Tool agent",
#     model="gemini-2.5-pro",
#     instruction="""
#         You are a helpful assistant that can use the following tools:
#         - google_search
#     """,
#     tools=[google_search]
# )
