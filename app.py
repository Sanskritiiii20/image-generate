from flask import Flask, request, send_file
from diffusers import StableDiffusionPipeline

# Load the Stable Diffusion pipeline and set device to CPU
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cpu") 

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "a painting of a futuristic city")
    image = pipe(prompt).images[0]  # Get the PIL image from pipeline output
    image.save("image.png")
    return send_file("image.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

