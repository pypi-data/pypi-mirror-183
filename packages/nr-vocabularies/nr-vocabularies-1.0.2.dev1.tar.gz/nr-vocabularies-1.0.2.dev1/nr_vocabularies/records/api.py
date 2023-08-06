from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record as InvenioBaseRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from nr_vocabularies.records.dumper import NRVocabulariesDumper
from nr_vocabularies.records.models import NRVocabulariesMetadata
from oarepo_vocabularies.records.api import OARepoVocabularyBase
from oarepo_vocabularies.records.system_fields.pid_hierarchy import VocabularyHierarchyPIDFieldContext
class NRVocabulary(OARepoVocabularyBase,InvenioBaseRecord):
    model_cls = NRVocabulariesMetadata
    schema = ConstantField("$schema", "local://nr-vocabularies-1.0.0.json")
    index = IndexField("nr_vocabularies-nr-vocabularies-1.0.0")

    # pid = PIDField(
    #     create=True, provider=RecordIdProviderV2, context_cls=VocabularyHierarchyPIDFieldContext
    # )

    dumper_extensions = []
    dumper = NRVocabulariesDumper(extensions=dumper_extensions)
