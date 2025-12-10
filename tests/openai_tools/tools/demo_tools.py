from typing import Annotated

class demo_tools:
   def demo_tools_function():
      """A demo function for testing purposes."""
      return "This is a demo function from demo_tools."
   
   def another_demo_tool(param: Annotated[str, "A string parameter for demonstration."]):
      """Another demo function that takes a parameter."""
      return f"You passed the parameter: {param}"