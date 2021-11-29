def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    # https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9

    n_samples = len(prediction)
    total_positives = sum(prediction)
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    total_true = sum(ground_truth)

    for i in range(n_samples):
        if prediction[i] == True:
            if ground_truth[i] == True:
                true_positives += 1
            else:
                false_positives += 1
        else:
            if ground_truth[i] == False:
                true_negatives += 1
            else:
                false_negatives += 1
    accuracy = (true_positives + true_negatives) / n_samples
    precision = true_positives / total_positives
    recall = true_positives / total_true
    f1 = 2 * precision * recall / (precision + recall)

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy

    n_samples = len(prediction)
    accurate_prediction = 0

    for i in range(n_samples):
        if prediction[i] == ground_truth[i]:
            accurate_prediction += 1
    
    accuracy = accurate_prediction / n_samples

    return accuracy
