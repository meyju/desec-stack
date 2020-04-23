from prometheus_client import Counter


metrics = {}


def get(name):
    return metrics.get(name)


def set(name, *args, **kwargs):
    metrics[name] = Counter(name, *args, **kwargs)


#models.py metrics

set('desecapi_pdns_keys_fetched', 'number of keys fetched')
set('desecapi_captcha_content_created', 'number of times of retrieval')
set('desecapi_delegation_updated', 'number of times of update')

#views.py metrics

set(('desecapi_dynDNS12_domain_not_found', 'number of times dynDNS12 domain is not found '))

#crypto.py metrics

set('desecapi_key_encryption_success', 'number of times key encryption was successfull')
set('desecapi_key_decryption_success', 'number of times key decryption was successfull')

#exception_handlers.py metrics

set('desecapi_database_unavailability_count', 'number of times database was unavailable')

#pdns.py metrics

set('desecapi_pdns_request_successfull', 'number of times pdns request was successfull')
set('desecapi_dnssec_key_information_dict_created', 'number of times dnssec key information dictionary was created')

#pdns_change_tracker.py metrics

set('desecapi_pdns_catalog_updated', 'number of times pdns catalog was updated successfully')

#mail_backends.py metrics

set('desecapi_sent_messages_count', 'number of messages sent')

#throttling.py metrics

set('desecapi_throttle_failure_occurence', 'number of times throttling failed')

#serializers.py metrics

set('desecapi_RRsetSerializer_many_init', 'number of times many_init function is triggerd in RRsetSerializer')