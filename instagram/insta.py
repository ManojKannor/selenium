from fastapi import FastAPI
import requests

app = FastAPI()

# Replace with your values
ACCESS_TOKEN = "IGAAKaZBdIfkf1BZAE5RZAzRpak1TNy16TUdjZA1RSWi1WS01vVE81bFZAaeTdTTXF5RFNYRGNuSGdCVGt4eVl0anJrZAzdCMkNBQXJMYU1OUlQ3TUc0aEl5emdsLTBXVnNYbFFqRlIzcm1CZA1N5b1FScFJRM3VXUnZAHdzlxRzJIcWV3SQZDZD"
INSTAGRAM_BUSINESS_ID = "17841476107927180"
IMAGE_URL = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2F4k-nature&psig=AOvVaw0I2uJ4eabITvyZwyslY3Io&ust=1755169650108000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLikytDfiI8DFQAAAAAdAAAAABAE"

@app.post("/post-to-instagram")
def post_to_instagram():
    # 1. Create the media object
    create_url = f"https://graph.facebook.com/v19.0/{INSTAGRAM_BUSINESS_ID}/media"
    create_payload = {
        "image_url": IMAGE_URL,
        "caption": "I am here",
        "access_token": ACCESS_TOKEN
    }
    create_res = requests.post(create_url, data=create_payload).json()

    if "id" not in create_res:
        return {"error": create_res}

    media_id = create_res["id"]

    # 2. Publish the media
    publish_url = f"https://graph.facebook.com/v19.0/{INSTAGRAM_BUSINESS_ID}/media_publish"
    publish_payload = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN
    }
    publish_res = requests.post(publish_url, data=publish_payload).json()

    return publish_res
