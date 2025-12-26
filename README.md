https://github.com/user-attachments/assets/119d84d9-ada3-4786-8e24-5df62cdd6eab

**Deployed Streamlit  Link:** : https://binary-dennsenet-121-w3gka5dxsgkq3u4vtlt95f.streamlit.app/

**Dataset Link :** : https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

**Trained Model Link :** https://drive.google.com/file/d/1Wh1whE0yodOiUaLHr1pn2NU-_a6M4Wu-/view?usp=drivesdk

## 🫁 Pneumonia Detection using Deep Learning.

> This Pneumonia Detection System is a medically oriented project
> designed to assist in the classification of chest X-ray images
> into Normal and Pneumonia categories with high reliability.
> The system is developed using **transfer learning** based on the
> **Pretrained model** **DenseNet-121**,which is  trained over
> the **millions  of feature image and thousands of classes** , this 
> enables  effective feature extraction and
> strong generalization on clinical imaging data.

# Model Performance Metrics :

> The model is evaluated across training, validation, and independent 
> Test datasets to present a transparent and comprehensive view
> of its learning behavior and real-world generalization performance.

# Training & Validation Performance :

  | **Metric**              | **Value** |
|-------------------------|-----------|
| **Training Accuracy**   | **98.93%** |
| **Training Loss**       | **0.0395** |
| **Validation Accuracy** | **97.02%** |
| **Validation Loss**     | **0.0734** |

---

# Test Set Performance (Unseen Data)

- **Test Accuracy:** **87.98%**

#### Classification Report (Test Data)

| Class       | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Normal     | 97.60%    | 69.66% | 81.30%   | 234     |
| Pneumonia | 84.46%    | 98.97% | 91.15%   | 390     |

---

### 🩺 Clinical Interpretation

- The model achieves a **high recall of 98.97% for Pneumonia** on the test set, demonstrating strong sensitivity toward pneumonia-positive cases.  
- This is particularly important in medical screening scenarios, where **minimizing false negatives** is more critical than avoiding false positives.  
- Although recall for the Normal class is lower, the overall behavior reflects a **safety-oriented design choice**, prioritizing detection of pneumonia cases.

> **Note:**  
> Final performance claims are based exclusively on **independent test data**. Training and validation metrics are reported only to illustrate learning behavior and are not used as indicators of real-world performance.






