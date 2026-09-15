
import matplotlib.pyplot as plt


def gc(dataframe):
    fig, ax = plt.subplots()
    bio_group = ax.grouped_bar(
        heights={'GC Content': dataframe.get("Gc content").str.replace(
            "%", "").astype(float).tolist()},
        positions=range(len(dataframe)),
        group_spacing=1,
        tick_labels=dataframe['Organism'])

    for container in bio_group.bar_containers:
        ax.bar_label(container, padding=3)

    ax.set_xlabel("Organism")
    ax.set_ylabel("GC content")
    ax.set_title("GC content per organism")
    ax.legend(loc='upper left', ncols=10)
    return fig


def nuclotide(dataframe):
    fig, ax = plt.subplots()
    bio_group = ax.grouped_bar(
        heights=dataframe[['A', 'T', 'C', 'G']],
        positions=range(len(dataframe)),
        group_spacing=1,
        tick_labels=dataframe['Organism']
    )

    for container in bio_group.bar_containers:
        ax.bar_label(container, padding=3)
    ax.set_xlabel("Organism")
    ax.set_ylabel("Nuclotide")
    ax.set_title("Nuclotide Breakdown Per Organism")
    ax.legend(loc='upper left', ncols=10)
    return fig


def dna(dataframe):
    fig, ax = plt.subplots()
    bio_group = ax.grouped_bar(
        heights={'Dna Length': dataframe['Dna length'].tolist()},
        positions=range(len(dataframe)),
        group_spacing=1,
        tick_labels=dataframe['Organism'])

    for container in bio_group.bar_containers:
        ax.bar_label(container, padding=3)

    ax.set_xlabel("Organism")
    ax.set_ylabel("GC content")
    ax.set_title("Dna Length per organism")
    ax.legend(loc='upper left', ncols=10)
    return fig


def graph_builder(func, df):
    return func(df)
