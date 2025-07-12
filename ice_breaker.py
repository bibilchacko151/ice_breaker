from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_openai import AzureChatOpenAI



import os
if __name__ == "__main__":
    load_dotenv()
    print("hello world")
    credentials = DefaultAzureCredential()
    azure_ad_token_provider_bearer = get_bearer_token_provider(
    credentials,
    "https://cognitiveservices.azure.com/.default")
    llm = AzureChatOpenAI(
        azure_ad_token_provider=azure_ad_token_provider_bearer,
        temperature=0.7,
        max_tokens=256,
        azure_deployment=os.getenv("DEPLOYMENT_NAME"),
        azure_endpoint=os.getenv("ENDPOINT_URL"),
        api_version="2025-01-01-preview"
        )
    messages = [(
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",),("human", "I love programming."),]
    ai_msg = llm.invoke(messages)
    print(ai_msg)

    
    