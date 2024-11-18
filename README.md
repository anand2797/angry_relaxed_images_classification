# <h1 style="color:red;">Angry - <span style="color:skyblue;">Relaxed</span> <span style= "color:white;">Image Classification</span></h1>

This project is a deep learning-based image classification system to classify images into **Angry** and **Relaxed** categories. It includes a Flask web application, data and model tracking with DVC, and reproducible workflows for training and deploying the model.


### Sample Angry Image
<img src="static/images/angry_sample.jpeg" width="100%" alt="Angry Sample">

### Sample Relaxed Image
<img src="static/images/relaxed_sample.jpeg" width="100%" alt="Relaxed Sample">

## <h2 style="color:skyblue;">Project Overview</h2>

The project comprises the following key components:

1. **Data Collection**:  
   - Images representing "Angry" and "Relaxed" feelings were collected from Google using the "Download All Images" Chrome extension.  
   - These images were manually reviewed and organized into the `data/angry_images/` and `data/relaxed_images/` folders for training.  

2. **Deep Learning Model**:  
   - A convolutional neural network (CNN) was trained in Google Colab to classify images into "Angry" or "Relaxed" categories.  
   - The trained model is saved in the `models/` folder as `angry_classification.keras` and tracked using DVC to ensure reproducibility.  

3. **Flask Web Application**:  
   - A user-friendly interface was developed using Flask to allow users to upload images and classify them into either the "Angry" or "Relaxed" category.  
   - The Flask application (`app.py`) allows users to upload images and classify them as `Angry` or `Relaxed`.
   - The application displays both the uploaded and classified images directly on the web page.  

4. **Version Control**:  
   - Due to their size, datasets and models are excluded from the Git repository but are tracked using DVC.  
   - This ensures version control and easy reproduction of the workflow without compromising storage. 
   - Other all remaining files are added to git repository. 


## <h2 style="color:skyblue;">Project Structure</h2>

```
angry_relaxed_classification/
├── .dvc                      # DVC configuration files
├── logs/                     # Logs for monitoring the system
├── data/                     # Training and testing data (tracked by DVC)
│   ├── angry_images/         # Images of "Angry" category for training
│   ├── relaxed_images/       # Images of "Relaxed" category for training
│   ├── test_images/          # Images for testing the model
├── models/                   # Trained deep learning models (tracked by DVC)
│   ├── angry_classification.keras  # The trained model file
├── static/                   # Static files for the web page
│   ├── uploads/              # Uploaded images during testing
│   ├── images/               # Images for project description in README.md
│       ├── web_page_interface.png
│       ├── result_example.png
│       ├── angry_sample.png
│       ├── relaxed_sample.png
├── templates/                # HTML templates for the web page
├── .gitignore                # Git ignore file
├── .dvcignore                # DVC-specific ignore file
├── README.md                 # Project documentation
├── angry_classification.ipynb  # Initial notebook for model exploration
├── model.ipynb               # Google Colab notebook for training the model
├── app.py                    # Flask web application code
├── data.dvc                  # DVC tracking file for data
├── models.dvc                # DVC tracking file for models
├── requirements.txt          # Python dependencies

```

## <h2 style="color:skyblue;">Steps to Set Up the Project</h2>
### Step 1: Download Images
- First, we need to download angry and relaxed images for your dataset. 
- To simplify the process, use the **'Download All Images' extension** in our chrome browser. 
- This extension allows us to download multiple images from Google Search based on the keywords we specify. 
- Organize the images into two folders: `angry_images` and `relaxed_images`, and save this two folders in the data folder as `data/angry_images` and `data/relaxed_images`.


### Step 2: Set Up Git Repository
#### 2.1. Git initialize:
- To initialize a Git repository for the project, run the following commands:

```
git init
```
- This command initializes a new Git repository in the current directory, creating a .git directory to track changes. 
- It’s the first step in version controlling your project.

#### 2.2. Add a Remote Repository:
- add a remote repository to link our local Git repository to a remote server (e.g., GitHub, GitLab, etc.):
```
git remote add origin <repository_url>
```
- This commands allows us to push our changes to remote server.

### Step 3: Create and Activate a Conda Environment
#### 3.1. Create a new Environment:
- To create a new Conda environment for your project, run:
``` 
conda create -n <environment_folder_name> python=<python version> -y
```
- We can use any name as our environment name, for example i have used `venv` name and `3.9` python version:
   ``` conda create -n venv python=3.9 -y ```
-This command creates a new Conda environment called `venv` with Python `3.9` installed. 
- The `-y` flag automatically answers `yes` to the prompt asking for confirmation.

#### 3.2. Activate Virtual Environment:
- To activate the Conda environment, use:
```
conda activate angry_relaxed
```
- This command switches our current terminal session to the `venv` environment. 
- All Python and library installations will be isolated within this environment.

### Step 4: Install Dependencies
- After activating the environment, install the required dependencies by running:
```
pip install -r requirements.txt
```
- This command installs all the Python packages specified in the `requirements.txt` file, 
- Ensuring that your environment has all the necessary libraries to run the project. 
- These libraries may include TensorFlow, Flask, DVC, and other essential packages.


### step 5: Steps to Train the Model
####  5.1: Download Images for Training
- For training the model, we have to use fdownloaded  images for the Angry and Relaxed categories which are stored in `data` folder as `data/angry_images` and `data/relaxed_images'
- We have to use one more folder , that contains images for testing then deep learning model after we trained it.

#### 5.2: Upload Data to Google Colab
- Open a new notebook ipynb file and rename it as `model.ipynb` in Google Colab.
- Upload the `data/` folder with `test_images` folder to Colab.
- Adjust the file paths in the notebook to match the Colab environment.
#### 5.3: Train the Model
- Write and Execute all cells in the `model.ipynb` notebook to train the `CNN (Convolutional Neural Network)` model.
- After training, save the model as `angry_classification.keras` and download it.
- Upload the trained model to the `models/` folder in your local project directory.

### Step 6: Steps to Run the Application
#### 6.1. Start the Flask Application
- Use following command to run the `app.py` in terminal to start the Flask web server:
```
python app.py
```
#### 6.2. Open the Web Application
- Open our browser and navigate to ` http://127.0.0.1:5000 `to access the application.

- see the web page for this classification, 
 - #####  Web Page Interface and image upload Example
<p align="center">
  <img src="static/images/web_page_interface.png" alt="Web Page Interface" width="45%" />
  <img src="static\images\image_uploaded_web_page_interface.png" alt="image upload Example" width="45%" />
</p>

#####  Classification Result Example
![Classification Result Example](static/images/classification_result.png)
### Step 7: Set Up DVC for Data and Model Tracking
- DVC (Data Version Control) helps manage large files like datasets and machine learning models. 
#### 7.1. Initialize DVC: 
- First, initialize DVC in your project directory:
```
dvc init
```
- This command initializes DVC in your project and creates the necessary configuration files.
#### 7.2. Remote Storage For DVC:
- To set up remote storage for DVC, use:
``` 
dvc remote add -d <remote_name> <remote_storage_url>
```
- we have to replace <remote_name> with the name of your remote storage and <remote_storage_url> with the URL of our DVC storage (e.g., Amazon S3, Google Drive, etc.).

#### 7.3. Track Large Files with DVC:
- After dvc initialize and remote storage, next we have to track your large files with DVC.
- For example, to track the dataset, run:
```
dvc add <filename or foldername/>
```
- This command tracks our large file or folder, in this projects I have tracked `data/` and `models/` folders by dvc as they are having large size.
- So for this project I use `dvc add data/` and `data add models/` to track those to folders.
- This command tracks the `data/` and `models/` directories with DVC, which will allow us to version control the dataset and deep learning model efficiently.

### Step 8: Add and Commit Changes to Git
#### 8.1. Add all files to git :
- After setting up the project and tracking your data with DVC, add the changes to Git:
```
git add .
```
- This command stages all the changes made in the project, including the `.dvc` files that are used to track large files.(ex. data.dvc   and models.dvc, .dvcignore)
- We can add each file separately with commit message for each.
```
git add <filename or foldername/>
```

#### 8.2. Commit the changes:
- After adding files or folders to git, we have to commit the changes, with following command:
```
git command -m "< Commit message >"
```
-This command commits the staged changes to your local Git repository with a message indicating the setup.
- For example : `git commit -m "adding all files and dvc tracked files"`

#### 8.3. Check Branch Name of Git:
- To check the git branch to push our changes , use following command, which gives us the branch name, that we use to push our changes.
```
git branch
```

#### 8.4. Push Changes to Git:
- Finally, push your changes to the remote Git repository:
```
git push origin <branch_name>
```
- Assume `git branch` gives us the branch name as `main` or `master`, then we use following command to push
- `git push origin main` or `git push origin master`.
- This command pushes the committed changes to the `main` or `master` branch of your remote repository, keeping your project backed up and synchronized.


