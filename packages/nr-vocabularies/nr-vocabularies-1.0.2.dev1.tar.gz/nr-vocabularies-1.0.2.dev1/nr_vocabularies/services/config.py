from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from nr_vocabularies.records.api import NRVocabulary
from nr_vocabularies.services.permissions import NRVocabulariesPermissionPolicy
from nr_vocabularies.services.schema import NRVocabularySchema
from nr_vocabularies.services.search import NRVocabulariesSearchOptions
from oarepo_vocabularies.services.config import OARepoVocabulariesServiceConfigBase


class NRVocabulariesServiceConfig(InvenioRecordServiceConfig):
    """NRVocabulary service config."""

    url_prefix = "/v/"

    permission_policy_cls = NRVocabulariesPermissionPolicy
    schema = NRVocabularySchema
    search = NRVocabulariesSearchOptions
    record_cls = NRVocabulary

    components = [
        *InvenioRecordServiceConfig.components,
        *OARepoVocabulariesServiceConfigBase.components,
        *OARepoVocabulariesServiceConfigBase.components,
        *OARepoVocabulariesServiceConfigBase.components,
        *InvenioRecordServiceConfig.components,
    ]

    model = "nr_vocabularies"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
