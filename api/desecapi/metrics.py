from prometheus_client import Counter, Histogram


metrics = {}


def get(name):
    return metrics.get(name)


def set_counter(name, *args, **kwargs):
    metrics[name] = Counter(name, *args, **kwargs)


def set_histogram(name, *args, **kwargs):
    metrics[name] = Histogram(name, *args, **kwargs)


#models.py metrics

set_counter('desecapi_pdns_keys_fetched', 'number of pdns keys fetched')
set_counter('desecapi_captcha_content_created', 'number of times captcha content created')
set_counter('desecapi_autodelegation_created', 'number of autodelegations added')
set_counter('desecapi_autodelegation_deleted', 'number of autodelegations deleted')

#views.py metrics

set_counter('desecapi_dynDNS12_domain_not_found', 'number of times dynDNS12 domain is not found')

#crypto.py metrics

set_counter('desecapi_key_encryption_success', 'number of times key encryption was successful')
set_counter('desecapi_key_decryption_success', 'number of times key decryption was successful')

#exception_handlers.py metrics

set_counter('desecapi_database_unavailable', 'number of times database was unavailable')

#pdns.py metrics

set_counter('desecapi_pdns_request_success', 'number of times pdns request was successful')
set_counter('desecapi_pdns_keys_fetched', 'number of times pdns keys were fetched')

#pdns_change_tracker.py metrics

set_counter('desecapi_pdns_catalog_updated', 'number of times pdns catalog was updated successfully')

#mail_backends.py metrics

set_histogram('desecapi_messages_sent', 'distribution of number of messages sent', buckets=[0, 1, float("inf")])

#throttling.py metrics

set_counter('desecapi_throttle_failure', 'number of requested throttled')

#serializers.py metrics

set_counter('desecapi_rrset_list_serializer', 'number of times RRsetListSerializer was initialized')
