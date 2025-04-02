from agentic_patterns.reflection_pattern.reflection_agent import ReflectionAgent
from dotenv import load_dotenv

load_dotenv()

# Create agent with explicit model
agent = ReflectionAgent(model="llama3-70b-8192")

# Test parameters
user_msg = "Generate a Python implementation of the Merge Sort algorithm"
generation_system_prompt = "You are a Python programmer tasked with generating high quality Python code"
reflection_system_prompt = "You are Andrej Karpathy, an experienced computer scientist"

# Run the agent
final_response = agent.run(
    user_msg=user_msg,
    generation_system_prompt=generation_system_prompt,
    reflection_system_prompt=reflection_system_prompt,
    n_steps=10,
    verbose=1,
)

print("\nFinal Response:")
print(final_response) 