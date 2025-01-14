
import pandas as pd

def load_data_as_df(file_path):
    """
    Parse the dataset from the given file and load it into a Pandas DataFrame.
    """
    # Define fields to collect
    data = {
        "index": [],
        "title": [],
        "authors": [],
        "year": [],
        "venue": [],
        "references": [],
        "abstract": [],
    }

    # Open and parse the file
    with open(file_path, "r", encoding="utf-8") as file:
        current_paper = {key: None for key in data.keys()}
        current_paper["references"] = []

        for line in file:
            line = line.strip()
            if not line:
                if current_paper["index"] is not None:
                    # Append the current paper to the data
                    for key in data.keys():
                        data[key].append(current_paper.get(key, None))
                    # Reset for the next block
                    current_paper = {key: None for key in data.keys()}
                    current_paper["references"] = []
            elif line.startswith("#*"):
                current_paper["title"] = line[2:].strip()
            elif line.startswith("#@"):
                current_paper["authors"] = line[2:].strip().split(",")
            elif line.startswith("#t"):
                current_paper["year"] = int(line[2:].strip()) if line[2:].strip().isdigit() else None
            elif line.startswith("#c"):
                current_paper["venue"] = line[2:].strip()
            elif line.startswith("#index"):
                current_paper["index"] = int(line[6:].strip())
            elif line.startswith("#%"):
                current_paper["references"].append(int(line[2:].strip()))
            elif line.startswith("#!"):
                current_paper["abstract"] = line[2:].strip()

        # Add the last paper if EOF is reached without a blank line
        if current_paper["index"] is not None:
            for key in data.keys():
                data[key].append(current_paper.get(key, None))

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # some data cleaning
    df = df.drop(columns=["index"])

    return df