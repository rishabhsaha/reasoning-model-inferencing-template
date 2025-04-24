from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential
import os

credential = DefaultAzureCredential()
# Load environment variables
load_dotenv("../.env")

endpoint = os.getenv("ENDPOINT_URL")  
deployment_name = os.getenv("DEPLOYMENT_NAME", "gpt-4.1")  
subscription_key = os.getenv("O4MINI_API_KEY")  

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2025-01-01-preview",
)


def deli_lead(prompt: str) -> str:
    """
    Sends a prompt to Azure OpenAI and returns the response.

    Args:
        prompt (str): The input prompt to send to Azure OpenAI.

    Returns:
        str: The response from Azure OpenAI.
    """
    try:


        system_prompt = """
        You are a helpful assistant that uses Azure OpenAI to answer user questions. You can provide information, answer queries, and assist with various tasks. Please respond to the user's prompt in a clear and concise manner.
        """

        # Send the prompt to Azure OpenAI
        response = client.chat.completions.create(
            deployment_id=deployment_name,
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )

        # Extract and return the response text
        return response.choices[0].text.strip()

    except Exception as e:
        return f"An error occurred: {e}"


def deli_associate(prompt: str) -> str:
    """
    Sends a prompt to Azure OpenAI and returns the response.

    Args:
        prompt (str): The input prompt to send to Azure OpenAI.

    Returns:
        str: The response from Azure OpenAI.
    """
    try:


        system_prompt = """
        You are a helpful assistant that uses Azure OpenAI to answer user questions. You can provide information, answer queries, and assist with various tasks. Please respond to the user's prompt in a clear and concise manner.
        """

        # Send the prompt to Azure OpenAI
        response = client.chat.completions.create(
            deployment_id=deployment_name,
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )

        # Extract and return the response text
        return response.choices[0].text.strip()

    except Exception as e:
        return f"An error occurred: {e}"


def deli_coach(prompt: str) -> str:
    """
    Sends a prompt to Azure OpenAI and returns the response.

    Args:
        prompt (str): The input prompt to send to Azure OpenAI.

    Returns:
        str: The response from Azure OpenAI.
    """
    try:

        system_prompt = """
        You are a helpful assistant that uses Azure OpenAI to answer user questions. You can provide information, answer queries, and assist with various tasks. Please respond to the user's prompt in a clear and concise manner.
        """

        # Send the prompt to Azure OpenAI
        response = client.chat.completions.create(
            deployment_id=deployment_name,
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )

        # Extract and return the response text
        return response.choices[0].text.strip()

    except Exception as e:
        return f"An error occurred: {e}"


# Define the deployment name (replace with your deployment name)
