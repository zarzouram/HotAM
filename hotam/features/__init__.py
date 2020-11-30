

def get_feature(feature_name):

    for fm in __all__:
        
        if fm == get_feature or fm == FeatureSet:
            continue
        
        if  feature_name.lower() in fm.name().lower():
            return fm

    raise KeyError(f'"{fm}" is no a supported model"')


from hotam.features.bow import OneHot
from hotam.features.embeddings import Embeddings
from hotam.features.document_positions import DocPos

__all__ = [
            OneHot,
            Embeddings,
            DocPos,
        ]