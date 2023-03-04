import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def heatmap(y_test, y_pred):

    fig = sns.set(rc={'figure.figsize': (3,3)})
    plt.title("Confusion Matrix")
    sns.heatmap(
        confusion_matrix(y_test, y_pred).T, 
        sqaure=True, 
        annot=True, 
        fmt='d', 
        cbar=False,
    )

    plt.xlabel("Truth")
    plt.ylabel("Predicted")
    plt.show()
