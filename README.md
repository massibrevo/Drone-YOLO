<h1 align="center">Search and Rescue Computer Vision App</h1>
<h2 align="center">A web-based application for deploying a drone-based YOLO model to enhance search and rescue operations.</h2>

<br></br>
[![Streamlit](https://badges.aleen42.com/src/streamlit.svg)](https://streamlit.io/)
[![Python](https://badges.aleen42.com/src/python.svg)](https://python.org)

## 🎬 Overview

This application is developed as part of a Master's thesis in Computational Engineering and Mathematics, focusing on using deep learning and computer vision to improve the efficiency and effectiveness of search and rescue operations through aerial imagery analysis.

## How it Works:
I've created this Streamlit app that allows users to upload aerial images and uses a trained YOLOv8 model to detect and localize missing individuals in forested or challenging terrains.

## 💻 Run Locally
Follow these steps to get the application running on your local machine:

```bash
# Clone the repository
git clone https://github.com/yourusername/your-repository.git

# Navigate to the root directory
cd your-repository/streamlit

# Set up your Python environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the app
streamlit run Home.py
