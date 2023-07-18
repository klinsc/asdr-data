
# REAL-TIME PROTECTIVE OBJECT DETECTION: RPOD

  

## Experimenting on YOLOv3

1. Colab https://colab.research.google.com/drive/1_NGdtAdUg_JcjSuQOXvVyYOcu92OS9J1?usp=sharing

	* I tried to use colab to experiment on using of YOLO3, every tutorial step was fine until I met the OpenCV part, for the colab does not include "opencv for CPP" within the VM, and it is needed if I want to run the prediction real-time.

	* Installing "opencv for CPP" is slow as hell. Now I am trying to switch to using my own local environment. Paid the colab pro for nothing already!

	* The colab pro paid off, I could use the GPU to train the model on colab, it is much faster than my local environment.

  

2. YOLO3 https://pjreddie.com/darknet/yolo/

	* The tutorial is very clearly documented. Except for the prerequisite of "opencv for CPP", they told me that I should use the package manager to install it for it is complicated to do it on my own. That is why I have to experiment on my local environment.

  

3. CUDA https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/

	* I downloaded the .exe file from the relative URL above, we will see if it works or not.

	* No, it's not.

  

## Experimenting on YOLOv4

4. Finally I could train the model with the custom objects data of MRD & SMRD with help of YOLO4

	* Using the tutorial of https://github.com/AlexeyAB/darknet I could train the model on Google Colab.

	* With a little adjustment on the config file, the 5 classes in 14 images could be trained in around 2 hours.

	* The test result is not good, the model could not detect most of the objects in the test images.

	* I think the reason is that the bounding box that were drawn on the images are not accurate enough.

	* I will try to draw the bounding box more accurately and try again.

  

5. I have tried to draw the bounding box more accurate, more consistent and focus more on the main symbol of components, e.g., I ignored information from label of components.

	* Also, I increased the weight of line of the whole diagram to 2.5mm.

	* The train images were exported from CAD files as .pdf files, then I used the tool of pdf2image to convert them to .png files.

	* The result is better than before. The model could detect most of the objects in the test images.

	* Some evidence shows that the symbols that were drawn in the future area (area with grey background) are more effective than the symbols that were drawn in the normal area (area with white background).

	* We **can conclude** that the **impact factor** here is the **consistency of the bounding box, line weight and background colour**.

6. We **will do a new experiment**, with the same data, but with more classes. Also we **will use the new version of YOLO**, YOLOv8 from mmDetection.

	* This time we **will include some metrics** to evaluate the model, e.g., mAP, mAR, loss/e etc.
  

7. **After** the presentation of **1st Thesis Progress Evaluation**, I decided to use YOLOv5 instead of v8. The reason is that I want to start from a smaller and simpler version first.

	* I tried using **mmYOLOv5** with the default configs, but it **is not working**. No matter how I tried, the prediction result is always the same. It did detect a few objects in the first few times, but after that, it is not detecting anything.

	* The document or the configuration process of **mmYOLOv5 is very difficult to understand**, the consequence is the metric result is hard to interpret.

	* The time is running out, so while training with mmYOLO, I tried to use **YOLOv5 from Ultralytics** too. It is working.

	* With the default configs, the result of box_loss is decreasing, but the result of obj_loss is increasing. The cls_loss is decreasing too. The mAP is increasing, so the model is learning. However, the result of mAP is not good enough, it is around 0.1.

	* I tried to set a mosaic of 0.0, scale of 1.0, with 1000 epochs. Furthermore, from tips of the documentation, they said **if there are many small size components, set image and batch size as large as possible, so we set the image size of 1280 and batch size of 64**. The result is better, the mAP is around 0.3.

	* The framework from **Ultralytics** is very easy to use, for it is very **well documented**. The result for each training session is very easy to understand, for it is very well logged and visualised. They also provide a \*.png file of the training images & validate images for each session. The metrics like **box_loss, obj_loss, cls_loss, and mAP are also provided** for each session.

	* Next, I tried a **new setting**. With everything the same as before, except scale of 0.5 and copy_paste of 0.25. The result is better, the mAP is around 0.35 for IoU of 0.5. But other metrics are **not stable**.

	* I will pause the training for now, and start developing the semi-automatic labelling interface.

8. Semi-automatic Labelling
	* The **semi-automatic labelling interface was successfully developed**. Using the Labelstudio framework, but prediction results are **not accurate enough**. But this is what I expected, for the model is not trained enough. I will continue training the model with the help of the semi-automatic labelling interface.

	* I **removed sync_auto_25 symbols and sync_manual_bus**, since they are not used in the future diagrams. Also, **ground symbols are removed**, for they are not meaningful in the system.

	* I **finished labelling 50 drawings**, next we will move to the training process. And find out, if more images have an impact on the accuracy metrics or not.

9. Training with more images (a larger dataset)
	* One idea that I got from my colleague is, I should **have datasets with different line weights or colors**. Then test them seperately and see the metrics results, that could be **used as contribution to this research field**.
