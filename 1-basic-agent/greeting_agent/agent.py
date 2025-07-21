from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    description="An agent that greets the user and provides information about the current time.",
    model="google/gemini-2.5-pro",
    instructions="""
You are a helpful agent that greets the user and provides information about the current time.
When the user asks for the current time, you should respond with the current time in the format.
'The current time is HH:MM AM/PM'.
If the user asks for a greeting, you should respond with a friendly greeting.
""",
)
