import os
import fal_client
from fastapi import FastAPI
from dotenv import load_dotenv; load_dotenv()


app = FastAPI()
os.environ["FAL_KEY"] = os.getenv("FAL_KEY_SECRET")
    

@app.get("/create_logo/")
def create_logo(description: str, num_images: int=4):
    """
    Generates professional logo designs based on a given description.

    This endpoint uses a generative AI model to create logo designs that match the 
    provided description. The function generates logos (4 is default) and returns a list of 
    their URLs.

    Args:
        description (str): A detailed description of the logo to be generated.

    Returns:
        list: A list of URLs pointing to the generated logo images.

    Example:
        Request:
            GET /create_logo/?description=A modern logo with a green leaf and blue background

        Response:
            [
                "https://example.com/image_1.jpg",
                "https://example.com/image_2.jpg",
                "https://example.com/image_3.jpg",
                "https://example.com/image_4.jpg"
            ]
    """
    
    prompt = f"Professional logo matching this description: {description}"
    
    results = fal_client.run(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
            "seed": 6252023,
            "image_size": "landscape_4_3",
            "num_images": num_images
        },
    )

    return results["images"]
