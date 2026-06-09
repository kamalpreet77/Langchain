#  PromptTemplate — Think of it like a mad-libs fill-in-the-blank. You write a template with {variables} and fill them at runtime.

from langchain_core.prompts import PromptTemplate
# Step 1: Define the template with {variables}

template = PromptTemplate(
    input_variables=["topic", "level"],
    template="Explain {topic} to a {level} in simple terms."
)

# Step 2: Fill in the variables
filled_prompt = template.format(
    topic="machine learning",
    level="10-year-old"
)

# Step 3: See what was generated
print(filled_prompt)