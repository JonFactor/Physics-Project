import os, time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

apiKey = os.getenv("API_KEY")
client = OpenAI(api_key=apiKey)

print("Hello, I am your medical assitant.")
time.sleep(1)

retry = True
while retry:
    print("What is your medical problem? Please include your symptoms, when the problem occured, and any more related details about your medical issue.")
    userQuestion = input()

    print("loading...")
    
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "a chatbot that can answer basic medical questions and provide symptom guidance, promoting self-care and reducing strain on healthcare systems"},
        {"role": "user", "content": userQuestion}
    ]
    )

    print(f"My recomendation is:\n{response.choices[0].message.content}")

    while True:
        print("Do you want to ask another question?[Y/N]")
        userRetry = input()
        if userRetry == "N" or userRetry == "n":
            retry = False
            break
        elif userRetry == "Y" or userRetry == "n":
            retry = True
            os.system('clear')
            break
        else:
            print("Please Only input a Y or N")
        
        




