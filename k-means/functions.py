import matplotlib.pyplot as plt
import seaborn as sns


def hist_plot(df , target_col, x_col):
    fig, axes = plt.subplots(1, len(x_col), figsize=(20, 6))
    for n,col in  enumerate(x_col):
        axes[n].set_title(f"{col} ")
        sns.histplot(data=df, x=col, y=target_col, bins=20, pthresh=.1, cmap="mako",ax=axes[n])
    plt.show()
    plt.tight_layout()

def bar_plot(df , target_col, x_col):
    fig, axes = plt.subplots(1, len(x_col), figsize=(20, 6))
    for n,col in  enumerate(x_col):
        axes[n].set_title(f"{col} ")
        sns.barplot(data=df, x=col, y=target_col, ax=axes[n],)
    plt.show()
    plt.tight_layout()
