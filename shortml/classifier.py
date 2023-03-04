import seaborn as sns
import matplotlib.pyplot as plt
import sklearn


def accuracy(y_test, y_pred):
    print("Accuracy Score\t:", round(sklearn.metrics.accuracy_score(y_pred, y_test)*100, 2), "%")


def roc_auc_score(y_test, y_pred):
    print("ROC-AUC-Score\t:", round(sklearn.metrics.roc_auc_score(y_pred, y_test)*100, 2), "%")


def classification_report(y_test, y_pred):
    print("\nClassification Report\t\n\n", sklearn.metrics.classification_report(y_pred, y_test))


def confusion_matrix(y_test, y_pred):

    fig = sns.set(rc={'figure.figsize': (3,3)})
    plt.title("Confusion Matrix")
    sns.heatmap(
        sklearn.metrics.confusion_matrix(y_test, y_pred).T, 
        square=True, 
        annot=True, 
        fmt='d', 
        cbar=False,
    )

    plt.xlabel("Truth")
    plt.ylabel("Predicted")
    plt.show()

def report(y_test, y_pred):
    accuracy(y_test, y_pred)
    roc_auc_score(y_test, y_pred)
    classification_report(y_test, y_pred)
    confusion_matrix(y_test, y_pred)
