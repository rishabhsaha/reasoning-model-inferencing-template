from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = AzureOpenAI(
    endpoint="https://<your-openai-endpoint>.openai.azure.com/", credential=credential)


def deli_lead(prompt: str) -> str:
    """
    Sends a prompt to Azure OpenAI and returns the response.

    Args:
        prompt (str): The input prompt to send to Azure OpenAI.

    Returns:
        str: The response from Azure OpenAI.
    """
    try:

        # Define the deployment name (replace with your deployment name)
        deployment_name = "<your-deployment-name>"

        system_prompt = """
        You are a helpful assistant that uses Azure OpenAI to answer user questions. You can provide information, answer queries, and assist with various tasks. Please respond to the user's prompt in a clear and concise manner.
        """

        # Send the prompt to Azure OpenAI
        response = client.completions.create(
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

      # Define the deployment name (replace with your deployment name)
        deployment_name = "<your-deployment-name>"

        system_prompt = """
        You are a helpful assistant that uses Azure OpenAI to answer user questions. You can provide information, answer queries, and assist with various tasks. Please respond to the user's prompt in a clear and concise manner.
        """

        # Send the prompt to Azure OpenAI
        response = client.completions.create(
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
        response = client.completions.create(
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
