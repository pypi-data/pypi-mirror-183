from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import AnyUser, SystemProcess


class NRVocabulariesPermissionPolicy(RecordPermissionPolicy):
    """nr_vocabularies.records.api.NRVocabulary permissions."""

    can_search = [SystemProcess()]
    can_read = [SystemProcess()]
    can_create = [SystemProcess()]
    can_update = [SystemProcess()]
    can_delete = [SystemProcess()]
    can_manage = [SystemProcess()]
