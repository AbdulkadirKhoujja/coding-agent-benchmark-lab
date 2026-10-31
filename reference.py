"""Reference solution for versioned multi-tenant event reconciliation."""
def reconcile(events):
    latest = {}
    for event in events:
        if not isinstance(event, dict) or not {"tenant","key","version","value"} <= event.keys():
            raise ValueError("Malformed event")
        tenant, key, version = event["tenant"], event["key"], event["version"]
        if not isinstance(tenant, str) or not tenant or not isinstance(key, str) or not key:
            raise ValueError("Invalid identity")
        if type(version) is not int or version < 0:
            raise ValueError("Invalid version")
        identity = (tenant,key)
        old = latest.get(identity)
        if old is None or version > old[0]:
            latest[identity] = (version,event["value"])
        elif version == old[0] and event["value"] != old[1]:
            raise ValueError("Conflicting version")
    return {f"{tenant}/{key}":value for (tenant,key),(_,value) in sorted(latest.items())}
