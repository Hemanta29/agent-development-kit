from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    description="An agent that greets the user.",
    model="gemini-2.5-pro",
    instruction="""
You are a helpful agent that greets the user.
Ask for the user's name and greet them by their name.
""",
)
