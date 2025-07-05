## End to End Machine Learning Project

#  Student Performance Predictor - ML Project

An end-to-end Machine Learning application that predicts students' math scores based on demographic and academic features. Includes data processing, model training with hyperparameter tuning, and a Flask web interface.

##  Key Features

- **Automated ML Pipeline**: Modular structure for easy maintenance
- **Data Processing**: Handles missing values, scaling, and categorical encoding
- **Model Selection**: Evaluates multiple algorithms (RandomForest, XGBoost, CatBoost, etc.)
- **Performance Metrics**: Selects best model based on R² score
- **Production-Ready**: Model persistence and web interface via Flask

##  Project Structure
project-root/
├── artifacts/ # Serialized models and processed data
│ ├── model.pkl # Trained model
│ ├── preprocessor.pkl # Data preprocessing pipeline
│ ├── train.csv # Training data
│ └── test.csv # Testing data
├── notebook/ # Exploratory analysis
│ └── data/ # Raw datasets
│ └── stud.csv # Original dataset
├── src/ # Core application code
│ ├── components/ # ML pipeline components
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ ├── pipeline/ # Prediction workflow
│ │ └── predict_pipeline.py
│ ├── exception.py # Custom exceptions
│ ├── logger.py # Logging configuration
│ └── utils.py # Helper functions
├── templates/ # Flask templates
│ ├── index.html # Main page
│ └── home.html # Results page
├── application.py # Flask application
├── requirements.txt # Python dependencies
└── README.md # Project documentation


##  Model Inputs & Output

**Input Features:**
- Demographic:
  - `gender` (Male/Female)
  - `race_ethnicity` (Group A-E)
  - `parental_level_of_education` (e.g., "bachelor's degree")
  - `lunch` (Standard/Free/Reduced)
  - `test_preparation_course` (Completed/None)
  
- Academic:
  - `reading_score` (0-100)
  - `writing_score` (0-100)

**Output:**
- Predicted `math_score` (0-100)

##  Installation & Usage

### Prerequisites
- Python 3.7+
- pip

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor

# Install dependencies
pip install -r requirements.txt

# Prepare dataset (place stud.csv in notebook/data/)

Running the Pipeline
# Run data processing and model training
python src/components/data_ingestion.py
python src/components/data_transformation.py
python src/components/model_trainer.py

# Start Flask application
python application.py

Access the web interface at http://localhost:5000

 Technical Stack
ML Frameworks: scikit-learn, XGBoost, CatBoost

Web Framework: Flask

Data Processing: pandas, NumPy

Visualization: (Add if you have any)

 Future Improvements
Add comprehensive input validation

Dockerize application for easy deployment

Implement model versioning with MLflow

Add automated testing (unit/integration tests)

Develop REST API endpoints

Enhance UI with modern frontend framework
