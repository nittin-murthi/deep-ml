import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    data = np.array(data)

    values, counts = np.unique(data, return_counts=True)

    max_val, max_count = values[0], counts[0]

    for i in range(1, len(values)):
        if counts[i] > max_count:
            max_val = values[i]
            max_count = counts[i]
        elif counts[i] == max_count and values[i] < max_val:
            max_val = values[i]
            max_count = counts[i]
        else:
            continue

    return {'mean': data.mean(), 'median': np.median(data), 'mode': max_val, 'variance': np.var(data), 'standard_deviation': data.std(), '25th_percentile': np.percentile(data, 25), '50th_percentile': np.percentile(data, 50), '75th_percentile': np.percentile(data, 75), 'interquartile_range': (np.percentile(data, 75) - np.percentile(data, 25))}