from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

ENDPOINT = "https://loperfinalproject.cognitiveservices.azure.com/"
training_key = "93a938acb00d4ef7bd67f10e51edec5d"
prediction_key = "1e4442af34a249f7b4b52844ef9cc9ff"
prediction_resource_id = "/subscriptions/222f0e67-4426-4362-aa44-63916a12d2e5/resourceGroups/AzDevCloudBadgeRG-BL/providers/Microsoft.CognitiveServices/accounts/LoperFinalProject"