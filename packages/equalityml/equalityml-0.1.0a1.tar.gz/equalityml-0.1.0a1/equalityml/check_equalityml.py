import pandas as pd
import os
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

from fair import FAIR

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PACKAGE_PATH = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir))


if __name__ == "__main__":

    # First train a Machine Learning model with the training data
    random_state = 42

    # Read training and testing data.
    target_var = "HOS"
    protected_variable = 'RACERETH'
    train_path = os.path.join(PACKAGE_PATH, 'data', 'data_train.csv')
    training_data = pd.read_csv(train_path)
    X_train = training_data.drop(columns=target_var)
    y_train = training_data[target_var]
    test_path = os.path.join(PACKAGE_PATH, 'data', 'data_test.csv')
    testing_data = pd.read_csv(test_path)
    X_test = testing_data.drop(columns=target_var)
    y_test = testing_data[target_var]

    # Train a machine learning model
    mdl_clf = RandomForestClassifier(random_state=random_state)
    mdl_clf.fit(X_train, y_train)

    # Estimate prediction probability and predicted class of training data (Put empty dataframe for testing in order to
    # estimate this)
    pred_class = mdl_clf.predict(X_test)
    pred_prob = mdl_clf.predict_proba(X_test)
    pred_prob = pred_prob[:, 1]  # keep probabilities for positive outcomes only

    # Evaluate some scores
    prev_auc = roc_auc_score(y_test, pred_prob)  # Area under a curve
    prev_accuracy = accuracy_score(y_test, pred_class)  # classification accuracy

    y_pred = pred_prob.copy()
    y_pred[y_pred > 0.5] = 1
    y_pred[y_pred <= 0.5] = 0
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    PPV=tp / (tp+fp)


    # Compute Fairness score for "statistical_parity_ratio"

    fair_object = FAIR(ml_model=mdl_clf, training_data=training_data, testing_data=testing_data,
                                     target_variable=target_var,
                                     protected_variable=protected_variable, privileged_class=1)

    fair_object.print_fairness_metrics()
    metric_name = "statistical_parity_ratio"
    prev_fairness_metric = fair_object.fairness_metric(metric_name)

    fair_object.print_bias_mitigation_methods()
    mitigation_method = "correlation-remover"
    # "resampling-uniform", "resampling", "resampling-preferential", "correlation-remover", "reweighing",
    # "disparate-impact-remover"

    # For mitigation_method = reweighing, the result is model weights on data. How to solve that???
    mitigation_res = fair_object.bias_mitigation(mitigation_method=mitigation_method)

    if mitigation_method == "reweighing":
        mitigated_weights = mitigation_res['weights']
        mdl_clf.fit(X_train, y_train, sample_weight=mitigated_weights)
    else:
        mitigated_data = mitigation_res['training_data']
        X_train = mitigated_data.drop(columns=target_var)
        y_train = mitigated_data[target_var]

        # ReTrain Random Forest based on mitigated data
        mdl_clf.fit(X_train, y_train)
    # Estimate prediction probability and predicted class of training data (Put empty dataframe for testing in order to
    # estimate this)
    pred_class = mdl_clf.predict(X_test)
    pred_prob = mdl_clf.predict_proba(X_test)
    pred_prob = pred_prob[:, 1]  # keep probabilities for positive outcomes only

    # re-evaluate the scores
    new_auc = roc_auc_score(y_test, pred_prob)  # Area under a curve
    print(f"Previous AUC = {prev_auc} and New AUC = {new_auc}")

    new_accuracy = accuracy_score(y_test, pred_class)  # classification accuracy
    print(f"Previous accuracy = {prev_accuracy} and New accuracy = {new_accuracy}")

    fair_object.update_classifier(mdl_clf)
    new_fairness_metric = fair_object.fairness_metric(metric_name)

    print(f"Previous Fairness Score = {prev_fairness_metric[metric_name]:.2f} and New Fairness Score = "
          f"{new_fairness_metric[metric_name]:.2f}")
