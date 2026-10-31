"""Deliberately flawed synthetic candidate, not an actual AI output."""
def reconcile(events):
    return {f"{event['tenant']}/{event['key']}":event['value'] for event in events}
