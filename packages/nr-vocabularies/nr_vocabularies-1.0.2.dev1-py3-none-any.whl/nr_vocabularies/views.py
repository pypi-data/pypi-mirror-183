from flask import Blueprint


def create_blueprint_from_app(app):
    """Create  blueprint."""
    if app.config.get("NR_VOCABULARIES_REGISTER_BLUEPRINT", True):
        blueprint = app.extensions["nr-vocabularies"].resource.as_blueprint()
    else:
        blueprint = Blueprint(
            "nr-vocabularies", __name__, url_prefix="/empty/nr-vocabularies"
        )
    blueprint.record_once(init)
    return blueprint


def init(state):
    """Init app."""
    app = state.app
    ext = app.extensions["nr-vocabularies"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(ext.service, service_id="nr-vocabularies")

    # Register indexer
    iregistry = app.extensions["invenio-indexer"].registry
    iregistry.register(ext.service.indexer, indexer_id="nr-vocabularies")
