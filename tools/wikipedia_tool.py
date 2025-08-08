from langchain_community.document_loaders import WikipediaLoader

def wikiLoader(query:str): 
    '''Search any topic on wikipedia'''
    loader = WikipediaLoader(query=query,load_max_docs=2).load()
    return loader
