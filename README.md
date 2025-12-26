https://github.com/user-attachments/assets/119d84d9-ada3-4786-8e24-5df62cdd6eab

**Deployed Streamlit  Link:** : https://binary-dennsenet-121-w3gka5dxsgkq3u4vtlt95f.streamlit.app/

**Dataset Link :** : https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

**Trained Model Link :** https://drive.google.com/file/d/1Wh1whE0yodOiUaLHr1pn2NU-_a6M4Wu-/view?usp=drivesdk

# 🫁 Pneumonia Detection Model :

> This Pneumonia Detection System is a Medically oriented Project
> Designed to assist in the Classification of Chest X-Ray images
> Into Normal and Pneumonia categories with high reliability.
> The system is developed using **Transfer Learning** Based on the
> **Pretrained Model** **DenseNet-121**,which is  Trained over
> The **Millions  of Feature Image and Thousands of Classes** , this 
> Enables  effective feature extraction and
> Strong generalization on clinical imaging data.

## Model Performance Metrics :

> The model is evaluated across Training, Validation, and Independent 
> Test datasets to present a transparent and comprehensive view
> Of its Learning Behavior and Real-world Generalization Performance.

### Training & Validation Performance


  | **Metric**              | **Value** |
|-------------------------|-----------|
| **Training Accuracy**   | **98.93%** |
| **Training Loss**       | **0.0395** |
| **Validation Accuracy** | **97.02%** |
| **Validation Loss**     | **0.0734** |

---
### Training , Validation Learning Curves :    

    Accuracy
    1.00 |
    0.99 |                                           
    0.98 |                 _______/----------- **Training Learning Curve ACcuracy** 
    0.97 |            _____/------------------ **Validation Learning Curve ACcuracy** 
    0.96 |       _____/
    0.95 |  ____/
    0.94 |_/
     +-----------------------------------------
        1   3   5   7   9   11  13  15  17  19
                         Epochs



### Training , Validation Loss Curves : 

    Loss
    0.50 | _\____
    0.40 |    \____
    0.30 |         \____
    0.20 |                _____________ Train
    0.15 |           _____________ Validation
    0.10 |
    0.05 |
        +-----------------------------------------
        1   3   5   7   9   11  13  15  17  19
                         Epochs


### Confusion Matrix  of Test Data

                          Predicted
                      
                       Normal    Pneumonia
                    ----------------------
        Actual Normal     163        71
        
      Actual Pneumonia     4         386




### Test Set Performance (Unseen Data)

- **Test Accuracy:** **87.98%**

#### Classification Report (Test Data)

| Class       | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Normal     | 97.60%    | 69.66% | 81.30%   | 234     |
| Pneumonia | 84.46%    | 98.97% | 91.15%   | 390     |

---
### Recall Value Medical Interpretation : 

- This Model achieves a **High Recall of 98.97% for Pneumonia** on the Test Set, demonstrating strong sensitivity toward Pneumonia-Positive Cases.
- In Medical screening tasks, Recall is critically important, as missing even a Single Disease case can be Dangerous.
- Although an ideal recall value is close to **100%**, achieving perfect Recall is challenging due to practical limitations such as Dataset Variability and Computational constraints.
- This Model is therefore designed to **Minimize False Negatives**, prioritizing patient safety over Conservative Predictions.
- While Recall for the Normal class is comparatively lower, this reflects a **Safety-Oriented Design Choice** that emphasizes detecting pneumonia cases rather than risking missed diagnoses.

# Our Model Architecture :
    
      [ Input Image 224x224x3 ] -> [ Data Augmentation ] -> [ Rescaling 1/255 ]
                                      |
                                      v
                         [ DenseNet-121 (ImageNet, no top) ]
                                      |
                                      v
             [ Global Avg Pool ] -> [ BatchNorm ] -> [ Dropout 0.3 ]
                                      |
                                      v
                   [ Dense 512 (ReLU) ] -> [ Dropout 0.2 ]
                                      |
                                      v
                     [ Softmax Output (Normal | Pneumonia) ]
                     
#  Training Strategy (DenseNet 121) : 
    
      [ Freeze DenseNet-121 ] -> [ Train Classifier Head ]
                                      |
                                      v
                         [ Unfreeze from Layer 100 ]
                                      |
                                      v
                        [ Fine-Tuning (Lower LR) ]
                                      |
                                      v
                           [ Best Model Saved ]

                           
 # Installation & Setup : 
 
  ### Follow the steps below to Run this project locally and test the pneumonia detection model.

  **1. Clone this Repository:**
        
          git clone https://github.com/HemantMishra2003/Binary-DENnseNet-121.git
          cd Binary-DENnseNet-121
          
  **2. Install Python Dependencies:**
  
             pip install -r requirements.txt
             
  **3. To Run the Streamlit app and test the model:**
  
         streamlit run app.py
         
  **4. Use This Below Test X-Ray image to make Prediction:**

       Use  my given link Dataset to get Test image or  use my assets folder
       to get bactarial and normal x ray image to make prediction.
  
# Project Special Feature – Automated PDF Report

- Automatically generates a **PDF Medical Report** after Model prediction.
- The report includes:
  - Uploaded Chest X-ray image.
  - Predicted class (**Normal / Pneumonia**).
  - Model confidence score.
  - Enables users to **download and store prediction results**.                                      - of viewing or documentation

# How can you Contribute : 

> If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes with clear and meaningful commits.
4. Submit a pull request describing your changes.

> Suggestions for improvements, bug fixes, documentation enhancements, 
> and feature ideas are always welcome.




    

     




            


