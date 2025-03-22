from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import random
import time
from datetime import datetime

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_contacts(n=10):
    contacts = []
    names = ["Alice Johnson", "Bob Smith", "Charlie Brown", "David White", "Eve Black", "Frank Green", "Grace Adams", "Hank Miller", "Ivy Carter", "Jack Wilson"]
    positions = ["Software Engineer", "Product Manager", "Data Analyst", "UX Designer", "HR Specialist"]
    cities = ["New York", "San Francisco", "Los Angeles", "Chicago", "Miami"]
    messages = [
        "Let's schedule a meeting tomorrow.",
        "Looking forward to our collaboration!",
        "Can you send me the latest report?",
        "Great job on the presentation!",
        "Let's catch up soon!"
    ]
    
    for i in range(n):
        created_at_timestamp = int(time.time()) - random.randint(0, 100000)
        created_at = datetime.fromtimestamp(created_at_timestamp).strftime('%Y-%m-%d')
        contact = {
            "id": i + 1,
            "created_at": created_at,
            "name": random.choice(names),
            "img": f"https://randomuser.me/api/portraits/men/{random.randint(1, 99)}.jpg",
            "position": random.choice(positions),
            "city": random.choice(cities),
            "_orbits_last_message": {
                "message": random.choice(messages),
                "message_head": "Re: Important Update"
            }
        }
        contacts.append(contact)
    
    return contacts

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/receive_week")
async def receive_week(start_date: str):
    activities = []
    year, month, day = start_date.split("-")
    print(year, month, day)
    for i in range(0, 9):
        activities.append({
            "array": generate_contacts(10),
            "contact_date": year + "-" + month + "-" + str(int(day) + i)
        })

    # return activities
    return activities
