REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

You MUST use the following format. Do not include any other text before or after the format.
If you have the final answer, YOU MUST prefix it with "Final Answer:" followed by the JSON formatted according to the instructions.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question formatted according to format_instructions: {format_instructions}

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""