"""
AI-powered analysis for survey responses using OpenAI.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_openai_client():
    """Get configured OpenAI client."""
    from openai import OpenAI

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    return OpenAI(api_key=api_key)


def analyze_text_responses(
    responses: list[str],
    prompt_template: str | None = None
) -> str:
    """
    Analyze open-ended text responses using AI.

    Args:
        responses: List of text responses to analyze
        prompt_template: Optional custom prompt template

    Returns:
        AI-generated analysis of the responses
    """
    client = get_openai_client()

    if prompt_template is None:
        prompt_template = """Analyze the following survey responses and provide:
1. Key themes and patterns
2. Common sentiments expressed
3. Notable insights or outliers
4. Recommended follow-up questions

Survey Responses:
{responses}

Please provide a structured analysis."""

    # Combine responses for analysis
    responses_text = "\n---\n".join(responses)
    prompt = prompt_template.format(responses=responses_text)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a survey data analyst helping to extract insights from survey responses."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def categorize_responses(
    responses: list[str],
    categories: list[str]
) -> list[dict]:
    """
    Categorize open-ended responses into predefined categories using AI.

    Args:
        responses: List of text responses to categorize
        categories: List of category names

    Returns:
        List of dicts with response and assigned category
    """
    client = get_openai_client()

    categories_str = ", ".join(categories)
    results = []

    for response_text in responses:
        prompt = f"""Categorize this survey response into one of these categories: {categories_str}

Response: "{response_text}"

Return only the category name, nothing else."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        category = response.choices[0].message.content.strip()
        results.append({
            "response": response_text,
            "category": category
        })

    return results
