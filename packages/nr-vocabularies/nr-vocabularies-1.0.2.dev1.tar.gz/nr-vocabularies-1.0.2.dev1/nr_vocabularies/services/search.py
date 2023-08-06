from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


def _(x):
    """Identity function for string extraction."""
    return x


class NRVocabulariesSearchOptions(InvenioSearchOptions):
    """NRVocabulary search options."""

    facets = {
        "relatedURI_COAR": facets.relatedURI_COAR,
        "relatedURI_CrossrefFunderID": facets.relatedURI_CrossrefFunderID,
        "relatedURI_ROR": facets.relatedURI_ROR,
        "relatedURI_URL": facets.relatedURI_URL,
        "marcCode": facets.marcCode,
        "dataCiteCode": facets.dataCiteCode,
        "alpha3Code": facets.alpha3Code,
        "alpha3CodeENG": facets.alpha3CodeENG,
        "alpha3CodeNative": facets.alpha3CodeNative,
        "acronym": facets.acronym,
        "RID": facets.RID,
        "ICO": facets.ICO,
        "coarType": facets.coarType,
        "dataCiteType": facets.dataCiteType,
        "nameType": facets.nameType,
        "nonpreferredLabels_cs": facets.nonpreferredLabels_cs,
        "nonpreferredLabels_en": facets.nonpreferredLabels_en,
        "pair": facets.pair,
        "contexts": facets.contexts,
        "tags": facets.tags,
        "relatedURI_COAR": facets.relatedURI_COAR,
        "relatedURI_CrossrefFunderID": facets.relatedURI_CrossrefFunderID,
        "relatedURI_ROR": facets.relatedURI_ROR,
        "relatedURI_URL": facets.relatedURI_URL,
        "marcCode": facets.marcCode,
        "dataCiteCode": facets.dataCiteCode,
        "alpha3Code": facets.alpha3Code,
        "alpha3CodeENG": facets.alpha3CodeENG,
        "alpha3CodeNative": facets.alpha3CodeNative,
        "acronym": facets.acronym,
        "RID": facets.RID,
        "ICO": facets.ICO,
        "coarType": facets.coarType,
        "dataCiteType": facets.dataCiteType,
        "nameType": facets.nameType,
        "nonpreferredLabels_cs": facets.nonpreferredLabels_cs,
        "nonpreferredLabels_en": facets.nonpreferredLabels_en,
        "pair": facets.pair,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
        "uuid": facets.uuid,
        "indexed_at": facets.indexed_at,
        "type_pid_type": facets.type_pid_type,
        "type_id": facets.type_id,
        "pid_pk": facets.pid_pk,
        "pid_pid_type": facets.pid_pid_type,
        "pid_obj_type": facets.pid_obj_type,
        "pid_status": facets.pid_status,
        "title_sort": facets.title_sort,
        "icon": facets.icon,
        "hierarchy_level": facets.hierarchy_level,
        "contexts": facets.contexts,
        "tags": facets.tags,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }


from oarepo_vocabularies.services.search import OARepoVocabulariesSearchOptionsBase


class NRVocabulariesSearchOptions(
    OARepoVocabulariesSearchOptionsBase, InvenioSearchOptions
):
    """NRVocabulary search options."""

    facets = {
        "relatedURI_COAR": facets.relatedURI_COAR,
        "relatedURI_CrossrefFunderID": facets.relatedURI_CrossrefFunderID,
        "relatedURI_ROR": facets.relatedURI_ROR,
        "relatedURI_URL": facets.relatedURI_URL,
        "marcCode": facets.marcCode,
        "dataCiteCode": facets.dataCiteCode,
        "alpha3Code": facets.alpha3Code,
        "alpha3CodeENG": facets.alpha3CodeENG,
        "alpha3CodeNative": facets.alpha3CodeNative,
        "acronym": facets.acronym,
        "RID": facets.RID,
        "ICO": facets.ICO,
        "coarType": facets.coarType,
        "dataCiteType": facets.dataCiteType,
        "nameType": facets.nameType,
        "nonpreferredLabels_cs": facets.nonpreferredLabels_cs,
        "nonpreferredLabels_en": facets.nonpreferredLabels_en,
        "pair": facets.pair,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
        "contexts": facets.contexts,
        "tags": facets.tags,
        "relatedURI_COAR": facets.relatedURI_COAR,
        "relatedURI_CrossrefFunderID": facets.relatedURI_CrossrefFunderID,
        "relatedURI_ROR": facets.relatedURI_ROR,
        "relatedURI_URL": facets.relatedURI_URL,
        "marcCode": facets.marcCode,
        "dataCiteCode": facets.dataCiteCode,
        "alpha3Code": facets.alpha3Code,
        "alpha3CodeENG": facets.alpha3CodeENG,
        "alpha3CodeNative": facets.alpha3CodeNative,
        "acronym": facets.acronym,
        "RID": facets.RID,
        "ICO": facets.ICO,
        "coarType": facets.coarType,
        "dataCiteType": facets.dataCiteType,
        "nameType": facets.nameType,
        "nonpreferredLabels_cs": facets.nonpreferredLabels_cs,
        "nonpreferredLabels_en": facets.nonpreferredLabels_en,
        "pair": facets.pair,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
        "contexts": facets.contexts,
        "tags": facets.tags,
    }
    sort_options = {
        **OARepoVocabulariesSearchOptionsBase.sort_options,
    }
