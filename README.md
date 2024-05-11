<h1 align="center"> Drone-YOLO: an efficient AI method for the detection of missing people in forest remote areas</h1>

<br></br>
[![Roboflow](https://raw.githubusercontent.com/roboflow-ai/notebooks/main/assets/badges/roboflow-blogpost.svg)](https://blog.roboflow.com/)
[![Python](https://badges.aleen42.com/src/python.svg)](https://python.org)

## 🎬 Overview

This application is developed as part of a Master's thesis in Computational Engineering and Mathematics, focusing on using deep learning and computer vision to improve the efficiency and effectiveness of search and rescue operations through aerial imagery analysis.

## How it Works:
I've created this Streamlit app that allows users to upload aerial images and uses a trained YOLOv8 model to detect and localize missing individuals in forested or challenging terrains.

## 💻 run locally
Complete these steps with your console/terminal
```
# clone the repository
git clone https://github.com/roboflow/streamlit-web-app.git
```
```
# navigate to the root directory
cd streamlit-web-app
cd streamlit
```
```
# set up your python environment and activate it
python3 -m venv venv
source venv/bin/activate
```
```
# install the requirements
pip install -r requirements.txt
```
```
# run the app
streamlit run Home.py
```

### Troubleshooting:
* For Mac users: be sure that you have [Homebrew](https://brew.sh/) installed.
* Unable to resolve wheel for `av` or `aiortc` packages: Install `pkg-config` by executing `brew install pkg-config` in your Terminal
* If you wish to process video streams with Streamlit apps, be sure to also have `ffmpeg` installed: after installing Homebrew, execute `brew install ffmpeg` in your Terminal

-- Check here for more on `ffmpeg` installation: https://github.com/roboflow/video-inference#requirements
* Ensure that you have `opencv-python-headless` installed in your environment, instead of `opencv-python`

* Unable to install the `av` package with `pip`? Try executing `conda install av -c conda-forge` in your Terminal

-- Note: [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is required for this method. Be sure that `conda-forge` has been made available in your channels. https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge

## Acknowledgements

This project utilizes modified code from the [Roboflow Streamlit Computer Vision App for Web Browser Deployment](https://github.com/roboflow/streamlit-web-app), originally developed by Roboflow. The code is used under the Apache 2.0 License, which permits use, modification, and distribution.

### Modifications
The code has been adapted to enhance functionality and tailor the user experience to specific requirements of this Master's thesis project.

### License
This project is provided under the Apache License 2.0. A copy of the license is available in the LICENSE file of this repository.

### Original Source
You can find the original and unmodified code at:
[Roboflow Streamlit Web App GitHub Repository](https://github.com/roboflow/streamlit-web-app)
