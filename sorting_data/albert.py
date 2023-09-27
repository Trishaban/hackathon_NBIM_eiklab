import requests
import time

with open(r'C:\Source\EikLab\hackathon_NBIM_eiklab\no_sync\albert_api.txt') as f:
    API_TOKEN = f.readlines()[0]
    
API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	a = time.time()
	response = requests.post(API_URL, headers=headers, json=payload)
	print(time.time()-a)
	return response.json()
	
output = query({
	"inputs": "Quarter result were amazing for Tesla will expect growth",
})

print(output)