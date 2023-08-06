def map_service_config(service_config, payload_key_name, payload):
    mapped_config = {**service_config, payload_key_name: payload}
    service_config = {"config": {}, "script_config": {"config": mapped_config }}
    return service_config