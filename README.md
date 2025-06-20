# Car Damage Prediction 🚗

Car Damage Prediction is a deep learning-based web application that classifies the type of damage in a car image. Built with **PyTorch** and **Streamlit**, the app allows users to upload an image and receive an instant prediction from a trained ResNet model.

## 🌍 Live Demo

(Coming Soon) – Once deployed, the app link will be shared here.

## 🏗️ Project Structure

```
└── bhanuteja072-car_damage_prediction/
├── README.md
└── Streamlit-app/
├── app.py # Streamlit UI for image upload & prediction
├── model_helper.py # Code for loading model and predicting output
└── model/
└── saved_model.pth # Trained ResNet model (PyTorch state_dict)
```


## 🚀 Features

- Upload car images and get damage classification instantly.
- Uses a fine-tuned **ResNet18** model for high accuracy.
- Clean and interactive Streamlit interface.
- Optimized image preprocessing and inference.
- Ready for deployment on Streamlit Cloud or Hugging Face Spaces.

## 🧠 Model Details

- **Architecture**: ResNet18 (fine-tuned)
- **Framework**: PyTorch
- **Classes**: Example — `F_Brakage`, `F_Crushed`, etc.
- **Image Preprocessing**:
  - Resize to `(224, 224)`
  - Normalize using ImageNet stats (`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`)

## 🛠️ Technologies Used

- **Model & Backend**: PyTorch, TorchVision
- **Frontend**: Streamlit
- **Others**: PIL (image handling), NumPy

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Bhanuteja072/Car_Damage_Prediction.git

2. Navigate to the project directory:
   ```sh
   cd Car_Damage_Prediction/Streamlit-app
   ```
3. Install Requirements:
   ```sh
   pip install -r requirements.txt
   pip install streamlit torch torchvision Pillow

   ```
5. Run the application:
   ```sh
   streamlit run app.py

   ```
6. Open the browser and go to `(http://localhost:8501)`

## 📜 License
This project is licensed under the MIT License.

---

🔗 **Connect with Me:** https://github.com/Bhanuteja072

