import streamlit as st

# If the image is stored locally in the same directory as your script
st.image('UOC-TFM.jpg')

st.write("""
### [Roboflow Model Website](https://app.roboflow.com/tfmai/search-for-missing-people/1) • [GitHub](https://github.com/massibrevo/Drone-YOLO)💻


# Welcome to the Search and Rescue Computer Vision Application

### About this Project
This web application leverages the power of computer vision to enhance search and rescue (SAR) operations through aerial imagery analysis. Developed as part of my Master's thesis, this tool uses a state-of-the-art YOLOv8 model, trained on the Lacmus Drone Dataset (LADD), to detect missing individuals in forest areas from drone-captured images.

### The Importance of Computer Vision in SAR
[Computer vision technology](https://blog.roboflow.com/intro-to-computer-vision/) plays a crucial role in modern SAR operations. By automating the detection of individuals in vast and challenging terrains, this technology significantly speeds up rescue operations and increases their success rates. Learn more about the fundamentals of computer vision [here](https://roboflow.com/learn).

### Model Training and Deployment
The model was trained using Roboflow, a platform that provides robust tools for building and deploying computer vision models. For detailed instructions on how to train models using Roboflow, visit:
* [Training models with Roboflow Train](https://docs.roboflow.com/train)

For deploying models and integrating them into applications like this one, refer to:
* [Deploying models with Roboflow](https://blog.roboflow.com/deploy-tab)

#### How to Use this App:
Navigate through the app to upload aerial images from drone surveys and instantly analyze them for potential sightings of missing individuals. The results highlight detected persons, aiding rescue teams in focusing their efforts more effectively.

To directly access the model and start analyzing your images, please go to the [Drone YOLO Model](http://localhost:8501/Drone_YOLO_model).
""")
