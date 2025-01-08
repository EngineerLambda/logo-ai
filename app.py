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
        num_images (int): Number of logos to generate (default is 4)

    Returns:
        list: A list of URLs pointing to the generated logo images.

    Example:
        Request:
            GET /create_logo/?description=Macbook retailer, green accent, black theme

        Response:
            [
                {
                    "url": "https://fal.media/files/penguin/qf-ngi8RnItTbNrk7mkB5.png",
                    "width": 1024,
                    "height": 768,
                    "content_type": "image/jpeg"
                },
                {
                    "url": "https://fal.media/files/tiger/yFH7gaUAqo2FCCtf5VLEq.png",
                    "width": 1024,
                    "height": 768,
                    "content_type": "image/jpeg"
                },
                {
                    "url": "https://fal.media/files/zebra/rWQwuH3VT-LVtNQCWms4U.png",
                    "width": 1024,
                    "height": 768,
                    "content_type": "image/jpeg"
                },
                {
                    "url": "https://fal.media/files/rabbit/JEIGfy1c9wTSl_o3HDHt9.png",
                    "width": 1024,
                    "height": 768,
                    "content_type": "image/jpeg"
                }
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
