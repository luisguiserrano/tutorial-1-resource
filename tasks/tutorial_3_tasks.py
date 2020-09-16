from tutorial.functions import generate_dataset
from tutorial.functions import preprocess_data
from tutorial.functions import train_model
from tutorial.functions import make_predictions
from tutorial.functions import calculate_accuracy
from tutorial.utils import save_json
from tutorial.utils import read_json

def generate_preprocess_data(dataset_name):
    # Reading the data
    data = generate_dataset(dataset_name)

    # Processing the data
    features, labels = preprocess_data(data)

    # Saving the prediction and accuracy as results
    features_dict = {}
    features_dict['features'] = features
    save_json(features_dict, 'features.json')
    
    labels_dict = {}
    labels_dict['labels'] = labels
    save_json(labels_dict, 'labels.json')

def train_predict_accuracy(features, labels, model_name):
    
    feat = read_json(features)['features']
    lab = read_json(labels)['labels']

    # Training the model
    model = train_model(feat, lab, model_name)
    
    # Making predictions
    predictions = make_predictions(model, feat)
    
    # Calculating the accuracy of the model
    accuracy = calculate_accuracy(predictions, lab)
    
    # Saving the prediction and accuracy as results
    result = {}
    result['predictions'] = predictions.tolist()
    result['accuracy'] = [accuracy]
    save_json(result, 'result.json')
