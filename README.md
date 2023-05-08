# REAL-TIME PROTECTIVE OBJECT DETECTION: RPOD

## Experimenting on YOLO3
1. Colab https://colab.research.google.com/drive/1_NGdtAdUg_JcjSuQOXvVyYOcu92OS9J1?usp=sharing
    - I tried to use colab to experiment on using of YOLO3, every tutorial step was fine until I met the OpenCV part,
    for the colab does not include "opencv for CPP" within the VM, and it is needed if I want to run the prediction real-time.
    Installing "opencv for CPP" slow as hell. Now I try switching to use my own local environment. Paid the colab pro for nothing already!
    - The colab pro paid off, I could use the GPU to train the model on colab, it is much faster than my local environment.

2. YOLO3 https://pjreddie.com/darknet/yolo/
    - The tutorial is very clearly documented. Except the prerequisite of "opencv for CPP",
    they told that I should use the package manager to install it for it is complicated to do it on my own. That is why I have to experinment on my local environment.
    
3. CUDA https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/
    - I downloaded the .exe file from the relative of URL above, we will see if it works or not.
    - No, it's not.

4. Finally I could train the model with the custom objects data of MRD&SMRD with help of YOLO4
    - Using the tutorial of https://github.com/AlexeyAB/darknet I could train the model on Google Colab.
    - With a little adjustment on the config file, the 5 classes in 14 images could be trained in around 2 hours.
    - The test result is not good, the model could not detect most of the objects in the test images.
    - I think the reason is that the bouding box that were drawn on the images are not accurate enough.
    - I will try to draw the bouding box more accurate and try again.
