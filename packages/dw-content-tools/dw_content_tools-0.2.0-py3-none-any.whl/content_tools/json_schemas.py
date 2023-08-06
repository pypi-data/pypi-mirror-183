metadata_schema = {
    "type": "object",
    "additionalProperties": False,
    "required": ["title", "collection", "module"],
    "properties": {
        "title": {
            "type": "object",
            "additionalProperties": True,
            "required": [
                "name",
            ],
            "properties": {
                "name": {"type": "string"},
            },
        },
        "collection": {
            "type": "object",
            "additionalProperties": True,
            "required": [
                "name",
            ],
            "properties": {
                "name": {"type": "string"},
            },
        },
        "module": {
            "type": "object",
            "additionalProperties": True,
            "required": ["name", "difficulty", "type", "tags"],
            "properties": {
                "name": {"type": "string"},
                "difficulty": {"type": "string"},
                "type": {"type": "string"},
                "tags": {"type": ["string"]},
            },
        },
    },
}

docker_compose_device_schema = {
    "type": "object",
    "additionalProperties": True,
    "required": ["image"],
    "properties": {
        "image": {"type": "string"},
        "build": {"type": "string"},
        "ports": {
            "type": "array",
            "minItems": 0,
            "items": {"type": "string"},
        },
        "volumes": {
            "type": "array",
            "minItems": 0,
            "items": {"type": "string"},
        },
        "environment": {
            "type": "array",
            "minItems": 0,
            "items": {"type": "string"},
        },
        "command": {"type": "string"},
        "x-views": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["name", "url", "port"],
                "properties": {
                    "name": {"type": "string"},
                    "url": {"type": "string"},
                    "port": {"type": "string"},
                },
            },
        },
        "x-envvars": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["name", "value"],
                "properties": {
                    "name": {"type": "string"},
                    "value": {"type": ["string", "number"]},
                },
            },
        },
    },
}
