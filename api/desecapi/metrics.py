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

set('desecapi_d')

#.py metrics
#.py metrics
#.py metrics
#.py metrics
#.py metrics
