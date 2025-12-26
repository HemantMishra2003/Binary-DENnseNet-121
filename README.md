https://github.com/user-attachments/assets/119d84d9-ada3-4786-8e24-5df62cdd6eab

**Deployed Streamlit  Link:** : https://binary-dennsenet-121-w3gka5dxsgkq3u4vtlt95f.streamlit.app/

**Dataset Link :** : https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

**Trained Model Link :** https://drive.google.com/file/d/1Wh1whE0yodOiUaLHr1pn2NU-_a6M4Wu-/view?usp=drivesdk

# 🫁 Pneumonia Detection Model

> This Pneumonia Detection System is a medically oriented project
> designed to assist in the classification of chest X-ray images
> into Normal and Pneumonia categories with high reliability.
> The system is developed using **transfer learning** based on the
> **Pretrained model** **DenseNet-121**,which is  trained over
> the **millions  of feature image and thousands of classes** , this 
> enables  effective feature extraction and
> strong generalization on clinical imaging data.

## Model Performance Metrics :

> The model is evaluated across training, validation, and independent 
> Test datasets to present a transparent and comprehensive view
> of its learning behavior and real-world generalization performance.

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
      Actual Pneumonia    4        386




### Test Set Performance (Unseen Data)

- **Test Accuracy:** **87.98%**

#### Classification Report (Test Data)

| Class       | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Normal     | 97.60%    | 69.66% | 81.30%   | 234     |
| Pneumonia | 84.46%    | 98.97% | 91.15%   | 390     |

---
### Recall Value Medical Interpretation : 

> - This  model achieves a **High Recall of 98.97% for Pneumonia**
> - on the test set, demonstrating strong sensitivity toward pneumonia-positive cases.
> - In Medical Recall Value  must be 100  Percent but due to limitations of GPU , 
> - could not able to achive  **100 percent Recall value** . Since even missed while
> - detecting only one time Disease  is **Dangerous in Medical Field** .

- Although recall for the Normal class is lower,
- the overall behavior reflects a **safety-oriented  design choice**,
- prioritizing detection of pneumonia cases.
- 
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
 
  ### Follow the steps below to run this project locally and test the pneumonia detection model.

  **1. Clone this repository:**
        
          git clone https://github.com/HemantMishra2003/Binary-DENnseNet-121.git
          cd Binary-DENnseNet-121
          
  **2. Install Python dependencies:**
  
             pip install -r requirements.txt
             
  **3. To run the Streamlit app and test the model:**
  
         streamlit run app.py



    

     




            


