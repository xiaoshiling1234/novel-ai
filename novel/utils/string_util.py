import uuid


def generate_uuid():
    new_uuid = str(uuid.uuid4().hex)[:16]
    return new_uuid

