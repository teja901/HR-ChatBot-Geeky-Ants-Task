import os
from groq import Groq
import re



api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Missing GROQ_API_KEY. Please set it before running.")

client = Groq(api_key=api_key)






def clean_text(text: str) -> str:
    """Remove markdown formatting for plain readable text."""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text) 
    text = re.sub(r"\*(.*?)\*", r"\1", text)     
    text = re.sub(r"_(.*?)_", r"\1", text)        
    return text.strip()

def generate_response(query: str, employees: list) -> str:
    """
    Generate a natural language answer using Groq's LLaMA.
    
    Args:
        query (str): User's query
        employees (list): List of retrieved employee dictionaries
    
    Returns:
        str: Natural language response from LLaMA
    """
   
    context = "\n".join(
        [
            f"- {emp['name']} (Skills: {', '.join(emp['skills'])}, "
            f"Exp: {emp['experience']} yrs, "
            f"Projects: {', '.join(emp['projects'])}, "
            f"Availability: {emp['availability']})"
            for emp in employees
        ]
    )

    # Prompt for the LLM
    prompt = f"""
    You are an HR assistant chatbot.
    The user asked: "{query}"

    Here are some candidate profiles:
    {context}

    Based on the user query and these profiles,
    suggest the best matches in a helpful and professional tone.
    """

  
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=400,
    )

    
    raw_text = response.choices[0].message.content
    return clean_text(raw_text)
