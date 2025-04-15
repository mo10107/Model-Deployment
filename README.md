# 🌸 Model Deployment as API | Iris Flower Classifier –

## 📊 Data Set Information
This dataset contains **3 classes** of **50 samples each**, where each class represents a **species of iris plant**:

- **Setosa** 
- **Versicolour**
- **Virginica**

**Predicted Attribute**: Iris flower class based on 4 numeric features.

## 🌿 Attribute Information
- Sepal Length (cm)  
- Sepal Width (cm)  
- Petal Length (cm)  
- Petal Width (cm)  
- Class: `Setosa`, `Versicolour`, `Virginica`

## 🔧 Steps Overview

1. Build & train the model in Jupyter Notebook → `model/Iris_model.ipynb`
2. Save model as pickle file → `api/iris_model.pkl`
3. Create a Flask API to serve predictions → `api/api.py`
4. Create a Streamlit UI to interact with the model → `streamlit_app.py`
5. Wrap it all in Docker using → `docker-compose.yml`
6. Deploy locally or on the cloud

## ⚙️ Technical Requirements

- **Python 3.9+**
- **Docker**
- Required Python libraries in [`requirements.txt`](requirements.txt):

```
flask==3.0.3
flask-cors==5.0.1
joblib==1.4.2
scikit-learn==1.5.1
numpy==1.26.4
streamlit==1.37.1
requests==2.32.3
```

## 🧪 Run the Application Locally

### ▶️ Directly (without Docker)

```bash
# Clone the repo
git clone https://github.com/your-username/iris_flask_streamlit.git

# Navigate to backend
cd iris_flask_streamlit/api

# Install dependencies
pip install -r ../requirements.txt

# Run Flask API
python api.py
```

In a new terminal:

```bash
# Run Streamlit UI
streamlit run streamlit_app.py
```

### 🐳 With Docker Compose

```bash
# Clone the repo
git clone https://github.com/your-username/iris_flask_streamlit.git

# Go to project folder
cd iris_flask_streamlit/api

# Build and run the containers
docker-compose up --build
```

Access:
- API: [http://localhost:5001/predict](http://localhost:5001/predict)
- UI: [http://localhost:8501](http://localhost:8501)

## 🧪 Testing the API

You can send POST requests to the `/predict` endpoint using **Postman** or any HTTP client.

### 🔍 Sample request (Setosa)
```json
{
  "features": [4.9, 2.9, 1.2, 0.3]
}
```
**Response**:
```json
{
  "prediction": 0
}
```

### 🌸 Versicolour
```json
{
  "features": [6.4, 3.2, 4.5, 1.5]
}
```
**Response**:
```json
{
  "prediction": 1
}
```

### 🌺 Virginica
```json
{
  "features": [6.2, 3.1, 5.3, 2.4]
}
```
**Response**:
```json
{
  "prediction": 2
}
```
