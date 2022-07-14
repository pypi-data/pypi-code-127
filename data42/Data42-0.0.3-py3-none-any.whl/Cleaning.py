import pandas
import numpy

def remove_all_characters(df, filter, filter2 = None, filter3 = None, filter4 = None):
   
    """
    Function to remove all special characters in Dataframe. You can choose a specific character/wordl or remove all special characters. 
    Syntax:
        df = Dataframe 
        Filter = a character o list of character to remove in dataframe, you can use "all" for remove all character special
        You can use list with diferents things to remove in dataframe
        Filter2,  Filter3 and filter 4 is and aditional filters

    Libraries used:
        import pandas as pd
        import numpy as pd
        import re    
    """
    if filter == "all":
        df = df.replace(r"[\s\-\/;'`^¨_-]", "", regex=True)
    elif filter2 != None:
        df = df.replace(filter2, "", regex=True)
    elif filter3 != None:
        df = df.replace(filter3, "", regex=True)
    elif filter4 != None:
        df = df.replace(filter4, "", regex=True)
    else:
        df = df.replace(filter, "", regex=True)
    return df


def filter_by_value(df, filter_column, element, inverse = False, option=1, columns_select = None):
    '''
    To filter a dataframe by an specific element. 
    Input: 
        - df: dataframe
        - filter_column
        - element: filter element
        - option: to choose output, default: 1.
        - columnas_select: if opcion = 2, enter a list with the columns you want to get.
                           ejemplo: [col1, col2, col3]
        - filtro_inverso: default False --> to select the rows where the filter element appears.
                          True --> to select the rows where the filter element doesn't appear.
    Output:
        If opcion=1 --> complete dataframe filtered by the given element and column
        If opcion=2 --> dataframe with the columns in 'columnas select', filtered by the element and column given.   
    
    Libraries used:
        import pandas as pd
        import numpy as pd
    '''
    
    df_filtro = df[df[filter_column] == element]
    df_filtro_inverso = df[~(df[filter_column] == element)]
    
    if inverse == False:

        # Opcion 1 --> devuelve el df solo con las filas donde aparezca el element dado
        if option == 1:
            return df_filtro

        # Opcion 2 --> devuelve las columnas seleccionadas con las filas donde la columna filtro == element
        elif option == 2:
            return df_filtro[columns_select]

    elif inverse == True:

        # Opcion 1 --> devuelve el df filtrado 
        if option == 1:
            return df_filtro_inverso

        # Opcion 2 --> devuelve las columnas seleccionadas filtradas
        elif option == 2:
            return df_filtro_inverso[columns_select]
    else:
        print('''El parámetro inverso solo admite los valores True o False.
                False, por defecto, devuelve todas las columnas del dataframe.
                True, devuelve solo las columnas dadas''') 


def decoding(url):

  encodings=['utf-8','utf8', 'latin-1', 'latin1','iso-8859-1', 'iso8859-1', 'mbcs' , 'ascii', 'us-ascii', 'utf-16', 'utf16', 'utf-32', 'utf32']

  for i in encodings:
    try:
      df = pd.read_csv(url, encoding=i)
      return (df,i)

    except:pass


def detect_outlier(df,column):
    """
    You can use this function (IQR), several quartile values,
    and an adjustment factor to calculate
    boundaries for what constitutes minor and major outliers
    """
    sort_data = df[column].sort_values()
    quantile_1,quantile_3 = np.percentile(sort_data,[25,75])
    iqr_value = quantile_3 - quantile_1
    print('iqr value : ',iqr_value)
    
    ## Find the lower bound value and the  higher bound value
    lower_bound = quantile_1 - (1.5 * iqr_value)
    upper_bound = quantile_3 + (1.5 * iqr_value)

    #printing upper bound and lower_bound
    print('lower vale :',lower_bound,', higher value :',upper_bound)
    
    # Return all the data value that are outlier
    global outliers 
    outliers =  df[(df[column] > upper_bound) | (df[column] < lower_bound)][column]

    # % outliers
    print("Outliers (%):", round(len(outliers) / len(df[column]) * 100, 2))

    print("This are your outliers")
    print(outliers)
    print("Your outliers are stored in the variable : outliers, if you want to remove them you can use : df = df.drop(df.YOUR_COLUMN_NAME[outliers], axis = 0)")


def missings(df):
    '''
    Function that checks the missings 
    of the entire dataset and return the quantity and the percentage that are in each column
    parameters:
            -df:dataframe
    Libraries:
            - import pandas as pd
            - import numpy as pd       
    '''

    if df.isnull().sum().sum() > 0:  # the first sum calculates how many there are per column, and the second is the total of the dataset
        miss_total = df.isnull().sum().sort_values(ascending=False) 
        total = miss_total[miss_total > 0]

        miss_percent = df.isnull().mean().sort_values(ascending=False)
        percent = miss_percent[miss_percent > 0] *100

        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent %'])

        print(f'Total and Percentage of Missings:\n {missing_data}')
    else: 
        print('No missings found.')


def replace_missings(df, col):
    '''
    Function to eliminate or replace missings. This version is for dataframes that have not been separated into train and test.
    The user is asked for the dataframe and the column that they want to act on, and they are given options to choose what they want to
    do with the missings.

    Parameters:
        - df: dataframe
        - col: column you want to modify
        
    Libraries used:
        import pandas as pd
        import numpy as pd               
    '''

    print("Your column has :", df[col].isnull().sum(), "missings, and is of type: ", df[col].dtype)
    m = df[col].isnull().sum()
    if m > 0:
        select = input("Enter Delete to remove your missings or Change to see the change options")
        if select.lower() == "delete":
            select2 = input("Enter rows to delete all your rows that contains missings, enter column to delete the column that contains missings")
            if select2.lower() == "rows":
                df = df.dropna(axis = 0, inplace = True)
                print("Your rows with missings have been removed")
            if select2.lower() == "column":
                df = df.drop(col, axis = 1, inplace = True)
                print("Your columns with missings have been removed")
    
        elif select.lower() == "change":
            tipo = str(df[col].dtype)
            if 'int' in tipo or 'float' in tipo:
                op = str(input("Enter Mean to change your missings to the mean or Median to change them to the median"))
                if op.lower() == "mean":
                    df[col] = df[col].fillna(df[col].mean())
                    print("The missings of your column have been replaced by the mean")
                elif op.lower() == "median":
                    df[col] = df[col].fillna(df[col].median())
                    print("The missings of your column have been replaced by the median")
            else:
                print("Your variable is not numerical, changing the missings by the mode...")
                df[col] = df[col].fillna(df[col].mode().iloc[0])
                print("The missings of your column have been replaced by the mode")
    else:
        print("There are no missings to deal with")