# self_driving_car

The purpose of this repository is to use a Nvidia model to control an autonomous car. The model uses image data as input and uses polynomial regression to predict the steering angle. 

## Videos showing Successful Model

### Autonomous Driving on Original Track
![Alt Text](gifs/Autonomous.gif)

### Autonomous Driving on New Track
![Alt Text](gifs/Autonomous_New.gif)

### Manual Drives for Training
![Alt Text](gifs/Train.gif)

## Behavioral Cloning

The file `Behavioral_Cloning.ipynb` does the following:

### 1. Download, store, and clean data from manual drives

The program first retrieves csv data representing the `steering angle`, `throttle`, `reverse` and `speed`, as well as the images corresponding camera images (left, center and right). The program then cleans and unbiases the data.

![alt text](images/Unbias_Data.png?raw=true "Unbias Data")

### 2. Perform augmentation techniques on images to improve the dataset

To improve the robustness of the model, the program uses augmentation techniques to vary the dataset. These include:

#### Zoom

Zooms into the image.
![alt text](images/Zoom.png?raw=true "Zoom")

#### Pan

Translate the image.
![alt text](images/Pan.png?raw=true "Pan")

#### Flip

Performs a horizontal flip of the image. Also requires the steering angle be flipped as well to still be accurate.
![alt text](images/Flip.png?raw=true "Flip")

#### Brightness

Varies brightness of image. Mostly darkens, as it proved more effective for the model.
![alt text](images/Brightness.png?raw=true "Brightness")

#### Random Augmentation

The program augments images in a random distribution to ensure that variety is preserved.

![alt text](images/Random_Augmentation.png?raw=true "Random Augmentation")

### 3. Preprocess images

Next, the program converts the RBG images to YUV images, which have proven very effective for Nvidia models.

![alt text](images/Preprocess.png?raw=true "Preprocess")

![alt text](images/Preprocess_Augmentation.png?raw=true "Preprocess+Augmentation")

### 4. Create and saves a Nvidia model

The program then creates a Nvidia model, based on the following diagram.

![alt text](images/Nvidia_Model.png?raw=true "Nvidia Model")

 
A file called `<name>.h5` will be saved, which stores the trained and validated Nvidia model.

## How to Use Model

The model file can then be used in the following procedure.
  
### 1. Use Model File

Ensure that `<name>.h5` is in the same directory as `drive.py`. Then edit the `drive.py` source code to replace the line

```
model = load_model('<name>.h5')
```

and adjust `speed_limit` to any number between 0 and 30.

### 2. `drive.py`

Run the following from Anaconda Prompt + download any dependencies that come up.

```
python drive.py
```

### 3. Starting the Self Driving Car Simulator in Autonomous Mode

Install the Self Driving Car Simulator (Version 1) from: https://github.com/udacity/self-driving-car-sim and run the program. Then start the Autonomous mode in either track.


