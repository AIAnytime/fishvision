# Welcome to FishVision 🐬

### FishVision identifies the different species of Fishes. It is trained on "A Large Scale Fish Data" available on Kaggle using pretrained model "MobileNetV2".

<a href="https://imgbb.com/"><img src="https://i.ibb.co/wznGvSw/set-isolated-cute-animals-1308-35056.jpg" alt="set-isolated-cute-animals-1308-35056" border="0"></a>


**Currently, It only classifies among 9 species:** 👇

**['Hourse Mackerel',  'Black Sea Sprat',  'Sea Bass', 'Red Mullet', 'Trout',  'Striped Red Mullet',  'Shrimp',
'Gilt-Head Bream', 'Red Sea Bream']**


#### The app is live here: www.fishvision.herokuapp.com

## Built Using Transfer Learning, Streamlit, and Love  ❤️

You can read more on MobileNetV2 here: https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2

If you want to train on same data, find the dataset here: https://www.kaggle.com/crowww/a-large-scale-fish-dataset


To train the model using MobileNetV2, run the notebook in Colab or the local machine.
### Requirements and Installation
You can run below command in the working directory to install the requirements:

```sh
pip3 install requirements.txt
```

To start the app, go inside fishvision directory and follow the below steps:
#### Start the application using below command👇

```sh
streamlit run app.py .
```

#### If you want to deploy the app on Heroku after modification then follow below steps in your terminal:

```sh
$ heroku login.
```

```sh
$ cd my-project/
$ git init
$ heroku git:remote -a fishvision
```


```sh
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```


If you stuck somewhere, you can reach out to me on sonu1000raw@gmail.com 

Thanks 😇












