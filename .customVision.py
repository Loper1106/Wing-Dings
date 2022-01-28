from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, \
    Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

ENDPOINT = "https://loperfinalproject.cognitiveservices.azure.com/"
training_key = "1e4442af34a249f7b4b52844ef9cc9ff"
prediction_key = "1e4442af34a249f7b4b52844ef9cc9ff"
prediction_resource_id = "/subscriptions/222f0e67-4426-4362-aa44-63916a12d2e5/resourceGroups/AzDevCloudBadgeRG-BL/" \
                         "providers/Microsoft.CognitiveServices/accounts/LoperFinalProject"

# Initialize Customer Vision Project
publish_iteration_name = "classifying Model"

# Authenticate Client
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# Create New Project
print("Creating project")
project_name = uuid.uuid4()
str(project_name)
print(project_name)
project = trainer.create_project(project_name)

# Create Project  Tags

