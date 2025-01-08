import os
import fal_client
from fastapi import FastAPI
from dotenv import load_dotenv; load_dotenv()


app = FastAPI()
os.environ["FAL_KEY"] = os.getenv("FAL_KEY_SECRET")
    

@app.get("/create_logo/")
def create_logo(description:str):
    prompt = f"Professional logo matching this description: {description}"
    
    results = fal_client.run(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
            "seed": 6252023,
            "image_size": "landscape_4_3",
            "num_images": 4
        },
    )

    return results["images"]