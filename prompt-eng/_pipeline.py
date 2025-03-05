##
## Prompt Engineering Lab
## Platform for Education and Experimentation with Prompt Engineering in Generative Intelligent Systems
## _pipeline.py :: Simulated GenAI Pipeline 
## 
#  
# Copyright (c) 2025 Dr. Fernando Koch, The Generative Intelligence Lab @ FAU
# 
# Documentation and Getting Started:
#    https://github.com/GenILab-FAU/prompt-eng
# 

import requests
import json
import os
import time

def load_config():
    """
    Load config file looking into multiple locations
    """
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    # Find CONFIG
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    # Load CONFIG
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()


def create_payload(model, prompt, target="ollama", **kwargs):
    """
    Create the Request Payload in the format required by the Model Server
    """
    payload = None
    if target == "ollama":
        payload = {
            "model": model,
            "prompt": prompt, 
            "stream": False,
        }
        if kwargs:
            payload["options"] = {key: value for key, value in kwargs.items()}

    elif target == "open-webui":
        payload = {
            "model": model,
            "messages": [ {"role" : "user", "content": prompt } ]
        }
        
    else:
        print(f'!!ERROR!! Unknown target: {target}')
    return payload


def model_req(payload=None):
    """
    Issue request to the Model Server
    """
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer {api_key}"

    print(payload)

    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:
        result = ""
        delta = round(delta, 3)

        response_json = response.json()
        if 'response' in response_json:  # Ollama format
            result = response_json['response']
        elif 'choices' in response_json:  # Open-webui format
            result = response_json['choices'][0]['message']['content']
        else:
            result = response_json 
        
        return delta, result
    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. You need to adjust prompt-eng/config with API_KEY ({url})"
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"
    return


### TESTING MULTIPLE PROMPTING TECHNIQUES ###

if __name__ == "__main__":
    MESSAGE = "Explain the concept of Decision Trees and their advantages."

    # Define different prompting techniques
    PROMPTING_TECHNIQUES = {
        "Zero-Shot": MESSAGE,

        "Few-Shot": f"""
        You are an AI tutor. Answer technical questions in a structured manner.

        Example:
        Q: Explain Linear Regression.
        A: Linear Regression is a supervised learning technique used for predicting continuous values...

        Now answer:
        Q: {MESSAGE}
        A: 
        """,

        "Prompt Template": f"""
        Act like you are a machine learning professor.
        Your student is asking: {MESSAGE}
        Provide a structured response with clear examples.
        """,

        "Chain-of-Thought": f"""
        A Decision Tree is a flowchart-like structure used for decision-making.

        Step 1: Start at the root node and check the first condition.
        Step 2: Follow the branches based on attribute values.
        Step 3: Keep splitting until a leaf node is reached.
        Step 4: The final classification or regression result is determined.

        Now, explain {MESSAGE} following this logical breakdown.
        """,

        "Meta-Prompting": f"""
        Generate a highly structured and effective prompt to help students learn about {MESSAGE}.
        Ensure the generated prompt guides them step by step and requests detailed explanations with examples.
        """,

        "Self-Consistency": f"""
        Generate three different versions of the answer to the following question:
        {MESSAGE}

        Ensure each version is factually correct but presents the explanation in a different style (technical, simple, and analogy-based).
        """,

        "Contrastive": f"""
        Explain {MESSAGE}, but also compare Decision Trees with another machine learning algorithm, such as Neural Networks. 
        Highlight the key differences in terms of interpretability, computation cost, and real-world applications.
        """,

        "Role-Based": f"""
        You are an AI tutor specializing in machine learning. 
        Explain {MESSAGE} in a way that is easy for a beginner to understand, using simple language and real-life analogies.
        """,

        "Multi-Turn": f"""
        Let's go step by step. First, explain what a Decision Tree is in one sentence.
        Wait for my confirmation before continuing.
        Once confirmed, explain how Decision Trees make decisions.
        Then, wait again before proceeding to the advantages of Decision Trees.
        """,

        "Recursive": f"""
        Explain {MESSAGE} in a detailed manner.
        Then, review your explanation and improve it by making it more structured and clear.
        Finally, summarize your explanation in three key points.
        """
    }

    # Model configuration parameters
    MODEL_NAME = "llama3.2:latest"
    TEMPERATURE = 0.7
    NUM_CTX = 200
    NUM_PREDICT = 200

    # Iterate through each technique and test it
    for technique, prompt in PROMPTING_TECHNIQUES.items():
        print(f"\n{'='*40}\n🔹 Testing: {technique}\n{'='*40}")
        
        payload = create_payload(target="ollama",
                                 model=MODEL_NAME, 
                                 prompt=prompt, 
                                 temperature=TEMPERATURE, 
                                 num_ctx=NUM_CTX, 
                                 num_predict=NUM_PREDICT)

        # Execute model request
        time, response = model_req(payload=payload)
        
        # Print results
        print(f"📝 Response:\n{response}")
        if time:
            print(f'⏱️ Time taken: {time}s')
