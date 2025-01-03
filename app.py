from flask import Flask, request, render_template, redirect
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import boto3
import subprocess
app = Flask(__name__)



"""# Load your pre-trained model
try:
   # model = load_model(os.path.join('models', 'Angry_Relaxed_Image_Classification.keras'))
   S3 URL of the model (replace with your actual S3 model URL)
    
except Exception as e:
    app.logger.error(f"Error loading model: {e}")
    raise"""


# Function to fetch the model from S3 using DVC and load it
def fetch_and_load_model():
    # Run 'dvc pull' to fetch the model from the remote (S3) to the local environment
    result = subprocess.run(['dvc', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print("Model fetched successfully!")
    else:
        print(f"Error fetching model: {result.stderr.decode('utf-8')}")
        return None

    # After fetching the model, load it from the local path
    model_path = os.path.join('models', 'Angry_Relaxed_Image_Classification.keras')  # Adjust this to the local path where the model is stored
    try:
        model = load_model(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None
model = fetch_and_load_model()

# Define image size for the model
IMAGE_SIZE = (256, 256)  # Update according to your model's expected input size

# Supported image formats
SUPPORTED_FORMATS = {'jpg', 'jpeg', 'bmp', 'png'}

def preprocess_image(image_path):
    try:
        # Read the image using cv2
        image = cv2.imread(image_path)
        
        if image is None:
            raise ValueError("Image could not be loaded. Please check the file path and format.")
        
        # Resize the image to the expected input size
        image = cv2.resize(image, IMAGE_SIZE)
        
        # Expand dimensions to match the model's expected input
        image_array = np.expand_dims(image, axis=0)
        
        # Normalize the image array
        input_image_array = image_array / 255.0
        
        return input_image_array
    except Exception as e:
        app.logger.error(f"Error processing image: {e}")
        raise

@app.route('/', methods=['GET', 'POST'])
def index():
    upload_message = "Please upload a file of type jpg, jpeg, bmp, or png."
    result = None
    img_url = None

    if request.method == 'POST':
        try:
            if 'upload' in request.form:
                if 'file' not in request.files:
                    return redirect(request.url)
                
                file = request.files['file']
                
                # Check if file is uploaded
                if file.filename == '':
                    return redirect(request.url)
                
                # Get file extension
                file_extension = file.filename.rsplit('.', 1)[-1].lower()
                
                # Check if the file type is supported
                if file_extension not in SUPPORTED_FORMATS:
                    return render_template('index.html', upload_message=upload_message, result="Please upload a file of type jpg, jpeg, bmp, or png.", img_url=None)
                
                # Save the file
                file_path = os.path.join('static', 'uploads', file.filename)
                file.save(file_path)

                # Update messages and image URL
                result = "Upload successful. Click 'Classify' to get the prediction."
                img_url = 'uploads/' + file.filename  # Correctly use the filename for the URL
                
            elif 'classify' in request.form:
                uploaded_image = request.form.get('uploaded_image', '')
                print(uploaded_image)
                # Check if an image was uploaded before classification
                if not uploaded_image:
                    result = "Please upload an image first."
                else:
                    file_path = os.path.join('static', uploaded_image)

                    # Preprocess the image and make a prediction
                    img_array = preprocess_image(file_path)
                    prediction = model.predict(img_array)
                    class_label = 1 if prediction[0][0] > 0.5 else 0

                    # Map prediction to class label
                    result = 'Angry' if class_label == 0 else 'Relaxed'
                    img_url = uploaded_image  # Correctly use the filename for the URL

        except Exception as e:
            app.logger.error(f"Error during processing: {e}")
            result = f"An error occurred: {str(e)}"

    return render_template('index.html', upload_message=upload_message, 
                                         result=result, img_url=img_url)

if __name__ == '__main__':
    if not os.path.exists('static/uploads'):
        os.makedirs('static/uploads')
    app.run(host='0.0.0.0', port=5000, debug=True)
