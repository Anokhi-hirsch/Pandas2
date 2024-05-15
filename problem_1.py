# 

#using drop_duplicates
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]
    #filter out all the rows where autor_id matches viewer_id
    
    df = df.drop_duplicates(subset = ['author_id'], inplace= False)
    #remove the duplicate rows with same author_id
    
    df.sort_values(by = ['author_id'], inplace= True)
    #sorts author_id in ascending order
    
    df = df[['author_id']]
    #selects only author_id
    
    #renamed author_id to id as needed
    return df.rename(columns= {'author_id' : 'id'})


#other solution is to use unique()
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to find rows where author_id is equal to viewer_id
    df = views[views['author_id'] == views['viewer_id']]

    # Extract unique author_ids who viewed their own articles
    df = df['author_id'].unique()

    # Sort the result in ascending order
    df = pd.DataFrame({'id': sorted(df)})

    # Display the result
    return df
