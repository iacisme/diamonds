
def freedmanDiaconisRule(dfSeries):
    """
        Function that returns a bin width and recommended number of bins based on the Freedman-Diaconis Rule. 
        Suitable for data with outliers and when you want a balance between resolution and noise reduction.
        
        Pros: Robust to outliers, adapts to data spread
        Cons: May result in larger bin widths for small datasets
    """
    
    # Extract the 25% and 75% percentiles
    q1, q3 = dfSeries.quantile(
        q = [0.25, 0.75],
    )
    # Calculate the interquartile range of the data
    iqr = q3 - q1
    # Number of data points
    n = dfSeries.shape[0]
    # Recommended bin width 
    binWidth = round(2 * iqr * n**(-1/3), 3)
    # Calculate the number of bins
    numBins = int((dfSeries.max() - dfSeries.min()) / binWidth)

    return binWidth, numBins

def sturgesRule(dfSeries):
    """
        Function that returns the recommended number of bins based on Sturge's Rule.
        Good for smaller datasets and normally distributed data.
        
        Pros: Simple, quick to compute.
        Cons: Can underestimate the number of bins for large datasets.
    """

    # Required Libraries
    import numpy as np

    # Determine the number of records
    numberOfRecords = len(dfSeries)
    # Calculate the number of bins
    numBins = int(np.ceil(1 + np.log(numberOfRecords)))

    # Passing None to help in parsing results
    binWidth = None

    return binWidth, numBins

def scottsRule(dfSeries):
    """
        Function that returns a recommended bin width and number of bins based on Scott's Rule.
        Best for normally distributed data.
        
        Pros: Takes into account data spread via standard deviation.
        Cons: Sensitive to non-normality and outliers.
    """

    # Required libraries
    import numpy as np

    # Calculate the standard deviation
    stdDeviationValue = dfSeries.std()
    # Calculate the range
    dataRange = dfSeries.max() - dfSeries.min()
    # Determine the number of records in the dataset
    numberOfRecords = len(dfSeries)
    # Recommended bin width
    binWidth = round(3.5 * stdDeviationValue / numberOfRecords**(1/3), 3)
    # Calculate the number of bins
    numBins = int(np.ceil(dataRange / binWidth))

    return binWidth, numBins

def manualMethod(dfSeries):
    """
        Function that returns a recommended number of bins manually, using a square root to determine the initial number of bins
        Quick and simple, often used as a default or starting point.
        
        Pros: Easy to compute, generally reasonable for many distributions.
        Cons: Can be too simplistic for datasets with complex distributions.
    """
    
    # Required libraries
    import numpy as np

    # Determine the number of records in the dataset
    numberOfRecords = len(dfSeries)
    # Calculate the number of bins
    numBins = int(np.ceil(np.sqrt(numberOfRecords)))

    # Passing None to help in parsing results
    binWidth = None

    return binWidth, numBins