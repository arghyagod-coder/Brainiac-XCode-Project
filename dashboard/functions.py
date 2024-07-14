import requests
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import google.generativeai as genai
import os
from dotenv import load_dotenv
import googleapiclient.discovery
load_dotenv()

openweather_api_key = os.environ.get('OPENWEATHER_API_KEY')
newsapi_api_key = os.environ.get('NEWSAPI_API_KEY')

govdata_api_key = os.environ.get('GOVDATA_API_KEY')
genai.configure(api_key="AIzaSyBm_lb6U_KnzPcw5XaxwI7VdQYCW0DNb40")


def getRelatedNews(subject):
    newsapi_url = f"https://newsapi.org/v2/everything?q={subject}&apiKey={newsapi_api_key}"
    response = requests.get(newsapi_url)
    data = response.json()
    return data["articles"][:20]    


def GetResponse(query):
    generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

    model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

    chat_session = model.start_chat(
  history=[
  ]
)
    
    response = chat_session.send_message(query)
    if "answer in a paragraph:" not in query:
        return GetResponse("answer in a paragraph:"+response.text)
    return response.text


def GetQuizes(no,subject ,topic):
    generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

    model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

    chat_session = model.start_chat(
    history= [
        {
          "role": "user",
          "parts": [
            {"text": "generate a 5 question quiz of physics units and measurements in json format dont include any other text except the json"},
          ],
        },
        {
          "role": "model",
          "parts": [
            {"text": "\n[\n  {\n    \"question\": \"What is the SI unit of time?\",\n    \"options\": [\"second\", \"minute\", \"hour\", \"day\"],\n    \"answer\": \"second\"\n  },\n  {\n    \"question\": \"What is the symbol for the prefix 'kilo'?\",\n    \"options\": [\"k\", \"m\", \"c\", \"n\"],\n    \"answer\": \"k\"\n  },\n  {\n    \"question\": \"Which of the following is a derived unit?\",\n    \"options\": [\"meter\", \"second\", \"kilogram\", \"joule\"],\n    \"answer\": \"joule\"\n  },\n  {\n    \"question\": \"What is the unit of measurement for power?\",\n    \"options\": [\"watt\", \"joule\", \"newton\", \"ampere\"],\n    \"answer\": \"watt\"\n  },\n  {\n    \"question\": \"How many millimeters are there in one centimeter?\",\n    \"options\": [\"1\", \"10\", \"100\", \"1000\"],\n    \"answer\": \"10\"\n  }\n]\n"},
          ],
        },
      ])
    
    query=str("generate a "+str(no)+" question quiz of "+ subject+" " +topic )
    #print(query)
    response = ((chat_session.send_message(query)).text)
    return (response)



def ytplaylists(query):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyC8Y6UnPHRso57ufYDc5glqAquf5pcsa-4"
#ami env file banabo na
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        order="rating",
        q=query,
        type="playlist"
    )
    response = request.execute()

    return (response)







def fetch_playlists(subject):
    # Your YouTube Data API key
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAXfsClAYudZ0TOXWTwQwLsNBXSUuDYDhg"
#ami env file banabo na
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        order="rating",
        q=subject,
        type="playlist"
    )
    api_key = 'AIzaSyAXfsClAYudZ0TOXWTwQwLsNBXSUuDYDhg'
    
    # Base URL for YouTube Data API playlist endpoint
    base_url = 'https://www.youtube.com/playlist?list='
    
    # Parameters for the API request
    
    # Making the API request
    try:
        response = request.execute()
        
       # Raise an exception for bad status codes
        data = response
        
        # Process the response and extract playlist details
        playlists = []
        for item in data.get('items', []):
            playlist_id = item['id']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail_url = item['snippet']['thumbnails']['medium']['url']
            
            # Format the playlist card data (you can customize this structure)
            playlist_card = {
                'link': base_url+playlist_id['playlistId'],
                'title': title,
                'description': description,
                'thumbnail_url': thumbnail_url,
            }
            playlists.append(playlist_card)
       # print(playlists)
        return playlists
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching playlists: {e}')
        return None





def dukdumbytapi(query):
    generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

    model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

    chat_session = model.start_chat(
   history= [
        {
          "role": "user",
          "parts": [
            {"text": "generate a 5 question quiz of physics units and measurements in json format dont include any other text except the json"},
          ],
        },
        {
          "role": "model",
          "parts": [
            {"text": "\n[\n  {\n    \"question\": \"What is the SI unit of time?\",\n    \"options\": [\"second\", \"minute\", \"hour\", \"day\"],\n    \"answer\": \"second\"\n  },\n  {\n    \"question\": \"What is the symbol for the prefix 'kilo'?\",\n    \"options\": [\"k\", \"m\", \"c\", \"n\"],\n    \"answer\": \"k\"\n  },\n  {\n    \"question\": \"Which of the following is a derived unit?\",\n    \"options\": [\"meter\", \"second\", \"kilogram\", \"joule\"],\n    \"answer\": \"joule\"\n  },\n  {\n    \"question\": \"What is the unit of measurement for power?\",\n    \"options\": [\"watt\", \"joule\", \"newton\", \"ampere\"],\n    \"answer\": \"watt\"\n  },\n  {\n    \"question\": \"How many millimeters are there in one centimeter?\",\n    \"options\": [\"1\", \"10\", \"100\", \"1000\"],\n    \"answer\": \"10\"\n  }\n]\n"},
          ],
        },
      ]
)
    
    response = chat_session.send_message(query)
    if "fix the following" not in query:
        return GetResponse("fix the following json file example:[{'link': 'https://www.youtube.com/watch?v=EQRmoMXS4k4', 'title': 'PSC PHYSICS - Matter & Energy Class - 1//Aastha Academy', 'thumbnail_url': 'https://i.ytimg.com/vi/EQRmoMXS4k4/mqdefault.jpg'}] and dont output anything except the json file  :"+response.text)
    return response.text



def fetch_videos(subject):
    # Your YouTube Data API key
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAXfsClAYudZ0TOXWTwQwLsNBXSUuDYDhg"
#ami env file banabo na
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        order="rating",
        q=subject
      
    )
    api_key = 'AIzaSyAXfsClAYudZ0TOXWTwQwLsNBXSUuDYDhg'
    
    # Base URL for YouTube Data API playlist endpoint
    base_url = 'https://www.youtube.com/watch?v='
    
    # Parameters for the API request
    
    # Making the API request
    try:
        response = request.execute()
        
       # Raise an exception for bad status codes
        data = response
        
        # Process the response and extract playlist details
        playlists = []
        for item in data.get('items', []):
            playlist_id = item['id']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail_url = item['snippet']['thumbnails']['medium']['url']
            
            if 'videoId' not in playlist_id:
                continue
            # Format the playlist card data (you can customize this structure)
            playlist_card = {
                'link': base_url+playlist_id['videoId'],
                'title': str(title),
                'thumbnail_url': thumbnail_url,
            }
            playlists.append(playlist_card)
       # print(playlists)
        print(playlists)
        return (playlists)
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching playlists: {e}')
        return None
