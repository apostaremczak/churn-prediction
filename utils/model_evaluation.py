import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

LABELS = ["not churned", "churned"]


def evaluate_model(grid: GridSearchCV, X_test: np.ndarray,
                   y_test: np.ndarray) -> None:
    """
    Wrapper for the most useful model evaluation metrics.
    Given a cross-validation parameter grid, this function
    evaluates its best model.
    """
    # Print out best accuracy and parameters
    print(f"Best score: {grid.best_score_}")
    print(f"Best params: {grid.best_params_}")
    classifier = grid.best_estimator_
    y_pred = classifier.predict(X_test)

    # Print F1, precision and recall
    print(f"F1 score: {metrics.f1_score(y_test, y_pred):.3}")
    print(f"Precision score: {metrics.precision_score(y_test, y_pred):.3}")
    print(f"Recall score: {metrics.recall_score(y_test, y_pred):.3}")

    # Plot confusion matrix
    metrics.plot_confusion_matrix(classifier, X_test, y_test,
                                  display_labels=LABELS,
                                  normalize="true")
    plt.show()

    # Plot ROC curve
    # (Source: https://stackoverflow.com/a/38467407/5235965)
    # Get false positive rate and true positive rate
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_pred)
    roc_auc = metrics.auc(fpr, tpr)
    plt.title('Receiver Operating Characteristic curve')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
